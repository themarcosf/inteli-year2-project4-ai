# Sistema de Processamento de Texto e Classificação

A fim de realizar uma pré-verificação da taxonomia atribuída pelo usuário no momento da criação da requisição de compra, desenvolvemos um processo de processamento de linguagem natural. O objetivo desse processo é analisar o texto livre fornecido pelo usuário e compará-lo com uma base de dados pré-definida contendo as descrições de cada taxonomia. Essa comparação resulta em um número que representa a similaridade com cada uma das taxonomias, sendo selecionada a maior pontuação.

Se a taxonomia de maior similaridade corresponder àquela escolhida pelo usuário durante a criação da requisição de compra, nenhum procedimento adicional será realizado. No entanto, se não houver correspondência, será exibido um pequeno alerta abaixo do campo de descrição, indicando que a descrição fornecida parece não estar alinhada com a taxonomia escolhida.

Essa abordagem visa evitar possíveis erros na pré-classificação, contribuindo para a melhoria da precisão do sistema. Além disso, essa medida é crucial para garantir que a classificação na inteligência artificial não seja prejudicada, proporcionando uma experiência mais eficiente e livre de ambiguidades.

Este código consiste em uma API para processamento de texto utilizando técnicas de Processamento de Linguagem Natural (PLN) e classificação de dados textuais. O código está estruturado em diversas seções, cada uma cumprindo uma função específica no pipeline de processamento de texto e classificação.

## Bibliotecas Importadas

- **pandas (pd):** Biblioteca para manipulação e análise de dados tabulares.
- **numpy (np):** Biblioteca para operações matemáticas eficientes.
- **matplotlib.pyplot (plt):** Biblioteca para visualizações gráficas.
- **math:** Biblioteca padrão para operações matemáticas.
- **unidecode:** Biblioteca para remover acentos de caracteres.
- **re:** Módulo para manipulação de expressões regulares.
- **spacy:** Biblioteca para processamento de linguagem natural.
- **nltk:** Biblioteca para processamento de linguagem natural.
- **sentence_transformers:** Biblioteca para geração de embeddings de sentenças.

## Funções de Pré-processamento de Texto

- `remove_accents(text):` Remove acentos de caracteres em um texto.
- `lowercase_text(text):` Converte o texto para minúsculas.
- `remove_marks(text):` Remove caracteres não alfanuméricos do texto.

## Técnicas de PLN

- `stopWords(dados):` Remove as palavras de parada (stop words) de um texto.
- `lematizar(dados):` Realiza a lematização de um texto, reduzindo as palavras à sua forma base.
- `tokenizar_texto(texto):` Divide um texto em tokens (palavras).

## Pipelines para Tratamento dos Textos

- `pipeline_text(text):` Aplica o pipeline completo de pré-processamento em um texto.
- `pipeline_dataframe(text):` Aplica o pipeline completo de pré-processamento em uma coluna de um DataFrame.

## Função de Vetorização

- `Vetorizacao(dataframe, modelo):` Gera embeddings para uma coluna de texto em um DataFrame usando um modelo de embedding pré-treinado.

## Configuração do Modelo de Embedding

- `SentenceTransformer('distiluse-base-multilingual-cased'):` Inicializa um modelo de embedding pré-treinado para geração de embeddings de sentenças multilíngue.

## Função para Cálculo de Similaridade do Coseno

- `calculate_similarity(vectors, phrase_vector):` Calcula a similaridade do cosseno entre os embeddings de um vetor de frases e um vetor de uma frase específica.

## Função para Encontrar Máximo em um Array

- `encontrar_max(array):` Retorna o valor máximo e o índice correspondente em um array.

## Função para Verificar a Classe da Descrição

- `verify_class(first_class, description):` Utiliza o pipeline de processamento para verificar se uma descrição pertence à classe fornecida.

## Leitura dos Dados e Pré-processamento

- `df = pd.read_csv('./desc_types.csv'):` Lê um arquivo CSV contendo dados de descrições e tipos.
- `df_desc_new:` Aplica o pipeline de pré-processamento nas descrições do DataFrame, resultando em um DataFrame processado.

## Vetorização das Descrições

- `vector_desc = Vetorizacao(df_desc_new['desc'], vetorizadorTransformers):` Gera embeddings para as descrições utilizando o modelo de embedding SentenceTransformer.

## Configuração da API Flask

- `Flask, request, jsonify:` Bibliotecas e módulos para a criação de uma API web.
- `app = Flask(__name__):` Inicializa uma aplicação Flask.
- `@app.route("/health", methods=['GET']):` Rota para verificar a saúde da API.
- `@app.route("/process_desc_class", methods=['POST']):` Rota para processar a entrada de classe do usuário.

## Rota de Verificação da Saúde da API

- `/health:` Retorna uma mensagem indicando que a API está rodando sem erros.

## Rota de Processamento de Descrição e Classe

- `/process_desc_class:` Rota que aceita requisições POST com dados JSON contendo uma classe e uma descrição. Usa o modelo de embedding e a função de verificação de classe para retornar se a descrição parece pertencer à classe fornecida.

## Execução da Aplicação

- `if __name__ == '__main__': app.run(port=3001):` Inicia a aplicação Flask na porta 3001.
