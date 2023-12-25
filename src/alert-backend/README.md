# Integração Kafka-Discord para Alertas

## Descrição do Projeto
Este código consiste em um script Node.js que consome mensagens de um tópico Kafka e envia alertas para um canal Discord usando webhooks. O código utiliza a biblioteca `kafkajs` para interagir com clusters Kafka e `dotenv` para carregar variáveis de ambiente.

## Dependências
- `kafkajs`: Biblioteca para interação com clusters Kafka em Node.js.
- `dotenv`: Carrega variáveis de ambiente a partir de um arquivo .env.

## Configuração e Uso

1. **Configuração do Kafka:**
   - O código cria uma instância do objeto `Kafka`, especificando o ID do cliente como "app" e os endereços dos brokers Kafka.

2. **Configuração do Consumidor:**
   - Um consumidor Kafka é criado associado a um grupo com o ID "back-alert".

3. **Conexão e Subscrição:**
   - A função assíncrona `run` estabelece a conexão do consumidor com o cluster Kafka e se inscreve no tópico "alert" desde o início.

4. **Processamento de Mensagens:**
   - A função `eachMessage` é configurada para ser chamada a cada mensagem recebida no tópico Kafka. Ela converte a mensagem para uma string e a envia para um canal Discord usando um webhook.

5. **Execução:**
   - A função `run` é chamada assincronamente, e quaisquer erros são capturados e registrados no console.

## Configuração Adicional
Certifique-se de configurar corretamente as variáveis de ambiente, especialmente o URL do webhook do Discord, o IP do Broker e o ID do Client, antes de executar o script.
