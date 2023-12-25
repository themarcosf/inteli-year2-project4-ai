const Kafka = require('node-rdkafka');
const avro = require('avsc');
// Schema Avro
const schema = {
  type: 'record',
  name: 'Event',
  fields: [
    { name: 'datetime', type: 'string' },
    { name: 'failureIn', type: 'string' },
    { name: 'instanceReservation', type: 'string' },
    { name: 'lastActivity', type: 'string' },
  ],
};

const type = avro.Type.forSchema(schema);

// Kafka Producer Settings
const producer = new Kafka.Producer({
  'metadata.broker.list': '127.0.0.1:9092',
  'dr_cb': true, // enables producer delivery confirmation
});

module.exports.produceMessage = function(p1, p2, p3) {
  producer.connect();

  producer.on('ready', () => {
    console.log('Producer está pronto');

    const timestamp = Date.now();
    const dataFormatada = new Date(timestamp).toLocaleDateString();
    const numeroFormatado = Number(dataFormatada.replace(/\/+/g, ''));
    const event = { 
      datetime: dataFormatada, 
      failureIn: p1, 
      instanceReservation: p2,
      lastActivity: p3 
    };

    console.log('Objeto event:', event['datetime']);

    try {
      const buffer = type.toBuffer(event);
      producer.produce('alert', null, buffer, null, numeroFormatado);

      console.log('Mensagem enviada com sucesso para o tópico');
    } catch (error) {
      console.error('Erro ao enviar a mensagem para o tópico:', error.message);
    }
  });

  // Print errors reports
  producer.on('event.error', (error) => {
    console.error('Erro do produtor:', error);
  });

  // Print delivery reports, errors, or stats
  producer.on('delivery-report', (err, report) => {
    console.log('Confirmação de entrega:', report);
  });

  // Print interruption disconect reports
  process.on('SIGINT', () => {
    console.log('Desconectando o produtor...');
    producer.disconnect();
  });
}