//const Kafka = require("kafkajs").Kafka;
import { Kafka } from "kafkajs"

const kafka = new Kafka({
    clientId: 'my-producer',
    brokers: ['localhost:9092']
});

const producer = kafka.producer();

async function queueMessage(producer) {
    const event = { category: 'Logistica', name: 'META' };

    try {
        await producer.send({
            topic: 'test',
            messages: [{ value: JSON.stringify(event) }]
        });
        console.log('Message wrote successfully to test topic');
    } catch (error) {
        console.error('Something went wrong...', error);
    }
}

const run = async () => {
    await producer.connect();

    const intervalId = setInterval(() => {
        queueMessage(producer);
    }, 3000);

    return () => clearInterval(intervalId);
};

// run().catch(console.error);

//module.exports = { queueMessage, producer, run };
export { queueMessage, producer, run };