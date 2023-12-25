import pandas as pd
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

def verify_class(first_class, description):
    y = pipeline_text(description)
    y = np.array(y)
    y_bert = vetorizadorTransformers.encode(y)

    response = calculate_similiarity(vector_desc,y_bert)

    a, b = encontrar_max(response)

    portal = df['type'][b]
    if first_class == df['type'][b]:
        return("A descrição inserida parece ser da classificação selecionada")
    else:
        return(f"A descrição inserida não parece ser da classificação selecionada, que tal verificar a taxonomia {portal}")


df = pd.read_csv('./desc_types.csv')

df_desc_new = df.applymap(pipeline_dataframe)
df_desc_new = df_desc_new.drop('type', axis=1)
df_desc_new

vector_desc = Vetorizacao(df_desc_new['desc'], vetorizadorTransformers)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/health", methods=['GET'])
def health_check():
    return "API está rodando sem erros", 200

# Rota para processar a entrada de class no pln
@app.route("/process_desc_class", methods=['POST'])
def process_desc_class():
    try:
        data = request.get_json()
        if data is not None and 'class' in data and 'description' in data:
            class_value = data['class']
            desc_value = data['description']

            response_post = verify_class(class_value, desc_value)
            
            return response_post, 200
        else:
            return jsonify({"erro": "Dados JSON inválidos"}), 400
    except Exception as e:
        return jsonify({"erro": str(e)}), 500

if __name__ == '__main__':
    app.run(port=3001)