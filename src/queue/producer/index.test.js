const { Kafka } = require("kafkajs");
const { queueMessage, producer, run } = require("./index");

jest.mock("kafkajs", () => {
    return {
        Kafka: jest.fn().mockImplementation(() => {
            return {
                producer: () => ({
                    connect: jest.fn(),
                    send: jest.fn().mockResolvedValue(true),
                    disconnect: jest.fn(),
                }),
            };
        }),
    };
});

describe("Kafka Producer Tests", () => {
    let cancelRun;

    beforeEach(async () => {
        await producer.connect();
        cancelRun = await run();
    });

    afterEach(async () => {
        cancelRun();
        await producer.disconnect();
    });

    test("queueMessage should send a message to the 'test' topic", async () => {
        await queueMessage(producer);
        expect(producer.send).toHaveBeenCalledWith({
            topic: 'test',
            messages: expect.any(Array),
        });
    });
});
