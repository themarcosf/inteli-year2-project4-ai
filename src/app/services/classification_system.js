const { PrismaClient } = require("@prisma/client");
const uuid = require("uuid").v4;
const prisma = new PrismaClient();
const CircuitBreaker = require('opossum');
const { Semaphore } = require('async-mutex');

// initializes the semaphore with a maximum count of 100
const sem = new Semaphore(100);
const semPLn = new Semaphore(100);

// counter to track the number of concurrent calls
let concurrentRequests = 0;
let concurrentRequestsPLn = 0;
let auxTeste = 0;

function reportFallbackEvent() {
  return `This is the second service`;
}


async function classifier(invoiceInfo) {
  return new Promise(async (resolve, reject) => {
    // checks whether the limit of 95 concurrent requests has been reached
    if (concurrentRequests >= 95) {
      // reject(new Error('Limite máximo de requisições concorrentes atingido.'));
      console.log('Maximum limit of concurrent requests reached, redirecting to the secondary service');
      reportFallbackEvent();
      return;
    }

    // wait for semaphore permission
    const release = await sem.acquire();

    try {
      // increments the concurrent requests counter
      concurrentRequests++;
      console.log('concurrentRequests:', concurrentRequests)

      // checks whether the limit of 80 concurrent requests has been reached
      if (concurrentRequests >= 80) {
        // reduces the number of concurrent calls allowed
        console.log('the limit of 80 requests has been reached, freeing up resources')
        sem.release();
      }

      const classifierUrl = 'classifierUrl';

      try {
        const response = await fetch(classifierUrl, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(invoiceInfo),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        const classificationResult = await response.json();
        console.log('Classification result:', classificationResult);

        const newInvoice = await prisma.invoice.create({
          data: {
            id: uuid(),
            class: classificationResult,
          },
        });

        resolve(newInvoice);
      } catch (error) {
          console.error('Error making POST request to the classifier API:', error);
          throw error;
      }
    } catch (error) {
      reject(error);
    } finally {
      // decrements the concurrent requests counter
      concurrentRequests--;

      // release the traffic light
      sem.release();
    }
  });
}

async function circuitClassifier(invoiceInfo) {
  const options = {
    timeout: 7000, // If our function takes longer than 7 seconds, trigger a failure
    errorThresholdPercentage: 50, // When 50% of requests fail, trip the circuit
    resetTimeout: 30000 // After 30 seconds, try again.
  };
  
  function reportFallbackEvent(result) {
    if (result.toString() == 'Error: Timed out after 7000ms') {
      return `Sorry this is taking longer than expected, please wait a few seconds`;
    } else{
      return `Sorry, out of service right now, result was: ${result}`;
    }
  }
  
  const breaker = new CircuitBreaker(async () => {
    try {
      return await classifier(invoiceInfo);
    } finally {
      console.log('Releasing classifier semaphore');
    }
  }, options);
  
  breaker.fire()
    .then(console.log)
    .catch(console.error)
  
  breaker.fallback((result) => reportFallbackEvent(result));
}


async function ProcessDescription(userDescription) {
  return new Promise(async (resolve, reject) => {
    // checks whether the limit of 95 concurrent requests has been reached
    if (concurrentRequestsPLn >= 95) {
      reject(new Error('Limite máximo de requisições concorrentes atingido.'));
      return;
    }

    // wait for semaphore permission
    const release = await semPLn.acquire();

    try {
      // increments the concurrent requests counter
      concurrentRequestsPLn++;

      // checks whether the limit of 80 concurrent requests has been reached
      if (concurrentRequestsPLn >= 80) {
        // reduces the number of concurrent calls allowed
        semPLn.release();
      }

      const PLNUrl = 'PLNUrl';

      try {
        const response = await fetch(PLNUrl, {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify(userDescription),
        });

        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }

        const ProcessDescriptionResult = await response.json();
        console.log('Classification result:', ProcessDescriptionResult);

        resolve(ProcessDescriptionResult);
      } catch (error) {
          console.error('Error making POST request to the PLN API:', error);
          throw error;
      }
    } catch (error) {
      reject(error);
    } finally {
      // decrements the concurrent requests counter
      concurrentRequestsPLn--;

      // release the traffic light
      semPLn.release();
    }
  });
}

async function circuitProcessDescription(userDescription) {
  const options = {
    timeout: 2000, // If our function takes longer than 2 seconds, trigger a failure
    errorThresholdPercentage: 50, // When 50% of requests fail, trip the circuit
    resetTimeout: 30000 // After 30 seconds, try again.
  };
  
  function reportFallbackEvent(result) {
    if (result.toString() == 'Error: Timed out after 2000ms') {
      return `Sorry this is taking longer than expected, please wait a few seconds`;
    } else{
      return `Sorry, out of service right now, result was: ${result}`;
    }
  }
  
  const breaker = new CircuitBreaker(async () => {
    try {
      return await ProcessDescription(userDescription);
    } finally {
      console.log('Releasing PLN semaphore');
    }
  }, options);
  
  breaker.fire()
    .then(console.log)
    .catch(console.error);
  
    breaker.fallback((result) => reportFallbackEvent(result));
}

async function getAllInvoices() {
  try {
    const invoicesList = await prisma.invoice.findMany();
    return invoicesList;
  } catch (error) {
    throw new Error("Error getting invoice list: " + error.message);
  }
}

async function removeInvoice(invoiceId) {
  const removeInvoice = await prisma.invoice.findUnique({
    where: {
      invoiceId: invoiceId,
    },
  });

  if (!removeInvoice) {
    throw new Error("That invoice is not in this database");
  }

  await prisma.invoice.delete({
    where: {
      invoiceId: invoiceId,
    },
  });

  return {
    message: "Invoice removed successfully",
  };

}

module.exports = {
  getAllInvoices,
  removeInvoice,
  circuitClassifier,
  circuitProcessDescription
};