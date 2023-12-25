const express = require('express');
const bodyParser = require('body-parser');
const fs = require('fs');
const { DateTime } = require('luxon');

const app = express();
const port = 3002;

app.use(bodyParser.json());

function formatLogEntry(info, request) {
    const time = DateTime.utc().toISO();
    const error = info.error ? `- [${info.error}]` : '';
    const stackTrace = info.stackTrace ? `- [${info.stackTrace}]` : '';
    const clientIp = request.ip || '';

    return `[${clientIp}] - [${time}] [${info.level}] - ${info.message} ${error} ${stackTrace}`;
}

function saveLog(logEntry) {
    const logFilePath = 'metaplus3.log';

    fs.appendFileSync(logFilePath, logEntry.replace(/[\r\n]/g, ' ') + '\n');
}

app.post('/logs', (req, res) => {
    const now = DateTime.utc();
    const logEntry = formatLogEntry(req.body, req);

    try {
        saveLog(logEntry);
        res.json({ status: 'success', message: 'Log saved successfully' });
    } catch (err) {
        console.error(`Error saving log: ${err}`);
        res.status(500).json({ status: 'error', message: 'Failed to save log' });
    }
});

app.get('/', (req, res) => {
    res.json({ status: 'success', message: 'Server is running' });
});

app.listen(port, () => {
    console.log(`Started on http://localhost:${port}`);
});
