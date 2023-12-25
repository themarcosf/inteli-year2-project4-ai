const { Kafka } = require("kafkajs");
var moment = require('moment'); // require
moment().format(); 
const avro = require('avsc');

require("dotenv").config();

const kafka = new Kafka({
  clientId: process.env.CLIENTID,
  brokers: [process.env.BROKERS],
});

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

const consumer = kafka.consumer({ groupId: "back-alert" });

export const run = async () => {
  await consumer.connect();
  await consumer.subscribe({ topic: "alert", fromBeginning: true });

  await consumer.run({
    eachMessage: async ({ topic, partition, message }) => {
      const decodedMessage = type.fromBuffer(message.value);
      console.log(decodedMessage);

      const { datetime, failureIn, instanceReservation, lastActivity } = decodedMessage;

      let now = moment().format('llll');

      const embed = {
        title: 'ALERT',
        description: `Error datetime ${now}`,
        color: 16711680,
        author: {
          name: 'System Classifier Meta',
          icon_url: 'https://cdn-icons-png.flaticon.com/512/6033/6033716.png',
        },
        fields: [
          { name: 'Failure in', value: `${failureIn}`, inline: true },
          { name: 'Instance reservation', value: `${instanceReservation}`, inline: true },
          { name: 'Last activity', value: `${lastActivity}`, inline: true },
        ],
        timestamp: datetime,
      };

      const payload = JSON.stringify({
        content: "",
        embeds: [embed],
      });

      const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: payload,
      };

      try {
        const response = await fetch(process.env.URL_WEBHOOk_DISCORD, options);
        console.log("Alerta enviado com sucesso");
        console.log(response);
      } catch (err) {
        console.error("Erro ao enviar alerta:", err);
      }
    },
  });
};

run().catch(console.error);
