import { Kafka } from "kafkajs";

const kafka = new Kafka({
    clientId: 'my-consumer',
    brokers: ['localhost:9092']
});

const consumer = kafka.consumer({ groupId: 'kafka' });

const run = async () => {
    try {
        await consumer.connect();
        console.log('Consumer pronto...');

        await consumer.subscribe({ topic: 'test' });

        await consumer.run({
            eachMessage: async ({ topic, partition, message }) => {
                try {
                    const receivedMessage = JSON.parse(message.value.toString()); // Deserializar a mensagem JSON
                    console.log(`Received message: ${JSON.stringify(receivedMessage)}`);
                } catch (parseError) {
                    console.error(`Erro ao processar a mensagem: ${parseError.message}`);
                }
            },
        });
    } catch (error) {
        console.error(`Erro ao iniciar o consumer: ${error.message}`);
        // Processo adicional conforme necessário, como reconexão ou saída
    }
};

// Chamada da função run
run().catch(e => console.error(`Erro na execução: ${e.message}`));

export { consumer, run };
