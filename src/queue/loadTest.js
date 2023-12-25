import { check, sleep } from 'k6';
import { Writer, Reader } from 'k6/x/kafka';
import { b64decode } from 'k6/encoding';  // Importing the b64decode function

const brokers = ['kafka:9092'];
let producer, consumer;

export const options = {
    vus: 1, // Número de usuários virtuais (virtual users)
    duration: '1s', // Duração do teste
};

export default function () {
    producer = new Writer({ brokers: brokers, topic: 'test' });
    consumer = new Reader({ brokers: brokers, topic: 'test' });

    // Produza mensagens
    const event = { category: 'CAT', name: 'Gato' };
    producer.produce({ messages: [{ key: 'key', value: JSON.stringify(event) }] });

    // Consume mensagens
    const messages = consumer.consume({ limit: 1 });
    messages.forEach((msg) => {
        const decodedValue = b64decode(msg.value, 'rawurl'); // Decoding the message
        const eventData = JSON.parse(decodedValue); // Parsing the JSON string
        console.log(`Received message: ${JSON.stringify(eventData)}`);
    });

    check(messages, { 'Consumed messages': (msgs) => msgs.length === 1 });

    producer.close();
    consumer.close();
}
