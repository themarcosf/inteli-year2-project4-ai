import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
    stages: [
        { duration: '30s', target: 20 }, // Simula 20 usuários durante 30 segundos
        { duration: '1m', target: 50 },  // Aumenta para 50 usuários ao longo de 1 minuto
        { duration: '30s', target: 0 },  // Reduz para 0 usuários durante 30 segundos
    ],
};

export default function () {
    let res = http.post('http://localhost:3001/send-message');
    check(res, { 'status was 200': (r) => r.status === 200 });
    sleep(1);
}
