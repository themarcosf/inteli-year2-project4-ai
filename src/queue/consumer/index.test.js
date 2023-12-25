const { consumer, run } = require('./index.js');
jest.mock("kafkajs", () => {
    const mockConsumer = {
        connect: jest.fn(),
        subscribe: jest.fn(),
        run: jest.fn().mockImplementation((config) => {
            // Pode chamar config.eachMessage aqui se necessário para simular recebimento de mensagens
        }),
        on: jest.fn(), // Adicione se precisar simular eventos
    };

    return {
        Kafka: jest.fn().mockImplementation(() => {
            return {
                consumer: () => mockConsumer,
            };
        }),
    };
});

describe("Kafka Consumer Tests", () => {
    beforeAll(async () => {
        await run();
    });

    // Adicione testes específicos aqui
    test("Consumer should connect, subscribe, and run", () => {
        expect(consumer.connect).toHaveBeenCalled();
        expect(consumer.subscribe).toHaveBeenCalledWith({ topic: 'test' });
        expect(consumer.run).toHaveBeenCalled();
    });

    // Testes adicionais conforme necessário
});
