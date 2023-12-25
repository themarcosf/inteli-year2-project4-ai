import time
import threading
import json
import requests

timeResponsePost = [] # Tempo de resposta da requisição - Futuro API
responseCodePost = [] # Resposta da requisição - Futuro API
errorWithRigthCode = 0 # Numero de vezes que a requisição deu erro e retornou code 200
minAcceptResponse = 0


url = 'http://127.0.0.1:5000/process_class'

dataPost = {
  "class": 'Tax',
  "description": 'pagamento para marketing e sales para eventos, despesas de publicidade, eventos promocionais, materiais de marketing e patrocínios pro novo evento',
}

data_json = json.dumps(dataPost)
headers = {'Content-type': 'application/json'}


def requisicaoPost():
    global errorWithRigthCode
    aux = 0

    start = time.time()
    response = requests.post(url, data=data_json, headers=headers)
    end = time.time()

    timeResponsePost.append("%.2f" % (end - start))
    responseCodePost.append(response.status_code)

    print("Status: %s."%(response))
    print("Resposta: %s."%(response.text))

    if 'error' in response.text.lower() and response.status_code == 200:
      errorWithRigthCode += 1
      print(response.text)

threadsPost = []

# Defina o número de testes para criar
num_threads_Posts = 1000

# Crie e inicie as threads de testes assincronos
for i in range(num_threads_Posts):
    print(f'abrindo thread {i}')
    t = threading.Thread(target=requisicaoPost)
    t.start()
    threadsPost.append(t)

# for que espera todos os threads terminarem
for t in threadsPost:
    t.join()


valoresTimePost = [float(x) for x in timeResponsePost]
mediaTime = sum(valoresTimePost) / len(valoresTimePost)
valMinTime = min(valoresTimePost)
valMaxTime = max(valoresTimePost)
print("Média das timeResponses ", "%.2f" % (mediaTime))
print("Min das timeResponses ", valMinTime)
print("Max das timeResponses ", valMaxTime)

# Considerando que o tempo maximo aceitavel para essa requisição é de 5.00 segundos
for i in valoresTimePost:
  if i > 5.00:
    minAcceptResponse += 1

availability_percentage = (responseCodePost.count(200) / num_threads_Posts) * 100
print(f'Teste de disponibilidade {availability_percentage}%')
print("Numero de vezes que a requisição passou do tempo minimo: ",minAcceptResponse)
print("Numero de vezes que a requisição deu erro e retornou code 200: ",errorWithRigthCode)