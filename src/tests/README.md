# Testes do Sistema Novo

## Sistema de PLN para pŕe-classificação na criação de requisição de compra 

## 1. Introdução

Este script em Python realiza testes de desempenho em requisições HTTP utilizando a biblioteca `requests`. O objetivo principal é medir o tempo de resposta de requisições POST enviadas para um determinado endpoint (`url`). Além disso, o código avalia a disponibilidade do serviço, verificando a quantidade de respostas com código 200 e identifica casos em que ocorreram erros, mas o código de resposta foi 200.

## 2. Configuração Inicial

- `timeResponsePost`: Lista para armazenar os tempos de resposta das requisições POST.
- `responseCodePost`: Lista para armazenar os códigos de resposta das requisições POST.
- `errorWithRigthCode`: Contador de casos em que ocorreram erros, mas o código de resposta foi 200.
- `minAcceptResponse`: Contador de requisições que ultrapassaram o tempo mínimo aceitável.
- `url`: URL do endpoint para as requisições POST.
- `dataPost`: Dados a serem enviados na requisição POST, representando uma classe e sua descrição.
- `data_json`: Dados formatados em JSON para serem enviados na requisição POST.
- `headers`: Cabeçalhos da requisição POST.

## 3. Função `requisicaoPost()`

- Função responsável por realizar uma requisição POST.
- Mede o tempo de início e fim da requisição.
- Adiciona o tempo de resposta e o código de resposta às listas correspondentes.
- Imprime o status e a resposta da requisição.
- Incrementa `errorWithRigthCode` se ocorrer um erro e o código de resposta for 200.

## 4. Criação de Threads

- `threadsPost`: Lista para armazenar as threads de requisições POST.
- `num_threads_Posts`: Número de threads a serem criadas para simular requisições concorrentes.
- Laço que cria e inicia as threads de requisições POST.

## 5. Análise dos Resultados

- Calcula a média, mínimo e máximo dos tempos de resposta das requisições POST.
- Verifica quantas requisições excederam o tempo mínimo aceitável (5 segundos).
- Calcula a porcentagem de disponibilidade com base nos códigos de resposta 200.
- Imprime os resultados, incluindo a média, mínimo e máximo dos tempos, a porcentagem de disponibilidade e contadores de casos específicos.

## 6. Conclusão

O código oferece uma abordagem simples para realizar testes de desempenho em um serviço, fornecendo métricas de tempo de resposta e avaliando a disponibilidade com base nos códigos de resposta. Será adaptado para avaliar outros aspectos do serviço, conforme necessário.
