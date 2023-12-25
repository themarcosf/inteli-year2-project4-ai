const { connectToKafka, produceMessage, producer } = require('./alertProducer');

jest.mock("kafkajs", () => {
    const mockProducer = {
        connect: jest.fn(),
        send: jest.fn().mockResolvedValue(true),
        disconnect: jest.fn(),
        on: jest.fn((eventName, callback) => {
            // Você pode adicionar lógica específica aqui se necessário
            // Por exemplo, chamar o callback imediatamente para simular um evento 'ready'
            if (eventName === 'ready') {
                callback();
            }
        }),
    };

    return {
        Kafka: jest.fn().mockImplementation(() => {
            return {
                producer: () => mockProducer,
            };
        }),
    };
});


describe("Kafka Producer Tests", () => {
    beforeAll(async () => {
        await connectToKafka();
    });

    afterAll(async () => {
        await producer.disconnect();
    });

    test("produceMessage should send a message to the 'alert' topic", () => {
        const sendSpy = jest.spyOn(producer, 'send').mockResolvedValue(true);

        produceMessage();

        expect(sendSpy).toHaveBeenCalled();
        sendSpy.mockRestore();
    });
});
