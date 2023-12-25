import express from 'express';
import { queueMessage, producer } from './index.js'; // substitua 'seuScriptKafka' pelo nome do seu arquivo

const app = express();
const port = 3001; // você pode escolher outra porta

// Inicie o produtor do Kafka
producer.connect().catch(console.error);

// Endpoint para enviar mensagens
app.post('/send-message', async (req, res) => {
    try {
        await queueMessage(producer);
        res.status(200).send('Mensagem enviada com sucesso');
    } catch (error) {
        console.error('Erro ao enviar mensagem:', error);
        res.status(500).send('Erro ao enviar mensagem');
    }
});

app.listen(port, () => {
    console.log(`Servidor rodando na porta ${port}`);
});
