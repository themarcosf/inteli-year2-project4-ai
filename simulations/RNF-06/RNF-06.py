import pandas as pd
import random
import numpy as np
import matplotlib.pyplot as plt
import math
from unidecode import unidecode
import re
import spacy
import nltk
nltk.download('punkt')
from sentence_transformers import SentenceTransformer
nltk.download('rslp')
stemmer = nltk.stem.RSLPStemmer()
nlp = spacy.cli.download('pt_core_news_sm')
nlp = spacy.load('pt_core_news_sm')
import time
import threading
import json
import requests

# Funções de pré-processamento
## Remoção de acentos
def remove_accents(text):
    return unidecode(text)

## Transformar texto em minusculo
def lowercase_text(text):
  return text.lower()

## Remover caracteres não alfanumericos
def remove_marks(text):
    if isinstance(text, str):
        return re.sub(r'[^\w\s]|_', '', text)
    else:
        return text

# Tecnicas de PLN
## Remoção de StopWords
def stopWords(dados):
    if isinstance(dados, str):
        dados = [dados]

    resultado = [' '.join([token.text for token in nlp(texto) if not token.is_stop]) for texto in dados]

    return resultado

## Lematização do texto
def lematizar(dados):
    resultado = []
    for texto in dados:
        # Processa o texto com o modelo do Spacy
        doc = nlp(texto)
        # Lematiza o documento
        lemmas = [token.lemma_ for token in doc]
        # Junta tudo de volta a um texto
        textoLemmatizado = ' '.join(lemmas)
        resultado.append(textoLemmatizado)
    return resultado

## Tokenização do texto
def tokenizar_texto(texto):
    doc = nlp(texto)
    tokens = [token.text for token in doc]
    return tokens

# Pipelines para tratamento dos textos

def pipeline_text(text):
  array_phrase = []
  text = remove_accents(text)
  text = lowercase_text(text)
  text = remove_marks(text)
  text = stopWords(text)
  text = lematizar(text)
  text = tokenizar_texto(str(text)[1:-1].strip("'"))
  array_phrase.append(text)

  return array_phrase

def pipeline_dataframe(text):
  text = remove_accents(text)
  text = lowercase_text(text)
  text = remove_marks(text)
  text = stopWords(text)
  text = lematizar(text)
  text = tokenizar_texto(str(text)[1:-1].strip("'"))
  return text



#função para vetorização
def Vetorizacao(dataframe,modelo):
  # Calcula os embeddings para a coluna de texto
  embeddings_liz = modelo.encode(dataframe.tolist())
  # Cria um novo DataFrame com os embeddings
  embeddings_df = pd.DataFrame(embeddings_liz)

  return embeddings_df

vetorizadorTransformers = SentenceTransformer('distiluse-base-multilingual-cased')

#Função para calculo da similaridade do coseno
def calculate_similiarity(vectors: list, phrase_vector: list) -> float:
    text_similarity_array = []

    if str(type(phrase_vector)) != "<class 'numpy.ndarray'>":
      phrase_vector = phrase_vector.values
    else:
      pass

    for index, row in vectors.iterrows():
        np_vector_row = row.values
        np_vector_text = phrase_vector

        product_sum = np.sum(np_vector_row * np_vector_text)

        squared_frase_um = np.square(np_vector_row)
        squared_frase_dois = np.square(np_vector_text)

        sum_of_squares_array1 = np.sum(squared_frase_um)
        sum_of_squares_array2 = np.sum(squared_frase_dois)

        modulo = math.sqrt(sum_of_squares_array1) * math.sqrt(sum_of_squares_array2)

        text_similarity = product_sum / modulo

        text_similarity_array.append(text_similarity)
    return text_similarity_array

def encontrar_max(array):
    if not array:
        return "Array vazio"

    maior_numero = array[0]
    index = 0

    for i in range(1, len(array)):
        if array[i] > maior_numero:
            maior_numero = array[i]
            index = i

    return maior_numero, index

def req_post():
    global errorWithRigthCode

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

def verify_class(first_class, description):
    start = time.time()
    
    y = pipeline_text(description)
    y = np.array(y)
    y_bert = vetorizadorTransformers.encode(y)

    response = calculate_similiarity(vector_desc,y_bert)

    a, b = encontrar_max(response)

    portal = df['type'][b]
    if first_class == df['type'][b]:
        print("A descrição inserida parece ser da classificação selecionada")
    else:
        print(f"A descrição inserida não parece ser da classificação selecionada, que tal verificar a taxonomia {portal}")
    
    end = time.time()
    timeResponsePln.append("%.2f" % (end - start))	

if __name__ == '__main__':
    df = pd.read_csv('./desc_types.csv')

    df_desc_new = df.applymap(pipeline_dataframe)
    df_desc_new = df_desc_new.drop('type', axis=1)
    df_desc_new

    vector_desc = Vetorizacao(df_desc_new['desc'], vetorizadorTransformers)

    test_case_one_a = 'Tax'
    test_case_one_b = 'obrigações fiscais, como consultoria tributária, preparação de impostos, custos regulatórios e outros encargos associados a conformidade fiscal'

    test_case_sec_a = 'Sales, Marketing & Events'
    test_case_sec_b = 'pagamento para marketing e sales para eventos, despesas de publicidade, eventos promocionais, materiais de marketing e patrocínios pro novo evento'

    # verify_class(test_case_one_a,test_case_one_b)
    # verify_class(test_case_sec_a,test_case_sec_b)

    url = ''

    dataPost = {
    "class": '',
    "description": '',
    }

    data_json = json.dumps(dataPost)
    headers = {'Content-type': 'application/json'}

    threadsPost = []
    timeResponsePln = []
    timeResponsePost = [] # Tempo de resposta da requisição - Futuro API
    responseCodePost = [] # Resposta da requisição - Futuro API
    errorWithRigthCode = 0 # Numero de vezes que a requisição deu erro e retornou code 200
    minAcceptResponse = 0
    

    # Número de testes para criar - mudar conforme a necessidade do número de testes
    num_threads_Posts = 1000

    # Cria e inicia as threads de testes assincronos
    for i in range(num_threads_Posts):
        print(f'abrindo thread {i}')
        t = threading.Thread(target=verify_class(test_case_one_a,test_case_one_b))
        t.start()
        threadsPost.append(t)

    # for que espera todos os threads terminarem
    for t in threadsPost:
        t.join()

    # Métricas para PLN - Local  
    print('# Métricas para PLN - Local') 
    valoresTimePln = [float(x) for x in timeResponsePln]
    mediaTime = sum(valoresTimePln) / len(valoresTimePln)
    valMinTime = min(valoresTimePln)
    valMaxTime = max(valoresTimePln)
    print("Média das timeResponses ", "%.2f" % (mediaTime))
    print("Min das timeResponses ", valMinTime)
    print("Max das timeResponses ", valMaxTime)


    # Métricas para API - Nuvem (TO-DO)
    print('# Métricas para API - Nuvem (TO-DO)') 

    valoresTimePost = [float(x) for x in timeResponsePost]
    for i in valoresTimePost:
        if i > 0.50:
            minAcceptResponse += 1

    availability_percentage = (responseCodePost.count(200) / num_threads_Posts) * 100
    print(f'Teste de disponibilidade {availability_percentage}%')
    print("Numero de vezes que a requisição passou do tempo minimo: ",minAcceptResponse)
    print("Numero de vezes que a requisição deu erro e retornou code 200: ",errorWithRigthCode)