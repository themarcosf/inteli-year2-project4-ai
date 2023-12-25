# Inteli - Instituto de Tecnologia e Liderança 

<p align="center">
  <img src="https://i.imgur.com/aIfBsxk.png" alt="Inteli logo" border="0" width="312px">
</p>

# Projeto de arquitetura de software - Classificação e Taxonomia em Sourcing

## Grupo 4 - Meta+3

<br>

### 🚀 Integrantes
- <a href="https://www.linkedin.com/in/bruno-omeira/
">Bruno Meira </a>
- <a href="https://www.linkedin.com/in/lu%C3%ADsa-vit%C3%B3ria-leite-silva-681443230/
">Luisa Vitória Leite Silva </a>
- <a href="https://www.linkedin.com/in/marcos-florencio-n/">Marcos Florencio</a>
- <a href="https://www.linkedin.com/in/marcos-moura-02ab0a258/">Marcos Moura</a>
- <a href="https://www.linkedin.com/in/pedro-gattai-096678227/">Pedro Gattai</a>
- <a href="https://www.linkedin.com/in/priscila-falc%C3%A3o-3435a1244/">Priscila Falcão</a>

## 🔍 Sumário
* [Descrição](#-descrição)
* [Como começar](#-como-começar)
* [Estrutura de pastas](#-estrutura-de-pastas)
* [Instalação](#-instalação)
* [Tecnologias](#-Tecnologias)
* [Histórico de lançamentos](#-histórico-de-lançamentos)
* [Licença/License](#-licençalicense)
* [Referências](#-referências)


## 📜 Descrição

O projeto desenvolvido para a Meta teve como objetivo aplicar melhorias na arquitetura existente e atender a requisitos de qualidade, como tempo de resposta, disponibilidade e segurança. Além disso, o projeto buscou aprimorar o processo de classificação de invoices dentro da área de sourcing. Com o intuito de otimizar a eficiência do fluxo de trabalho, foram implementadas soluções tecnológicas que permitiram uma classificação mais precisa e automatizada das invoices, reduzindo erros e agilizando a tomada de decisões. Essas melhorias contribuíram para aumentar a produtividade e a eficácia do departamento de sourcing, resultando em uma operação mais eficiente e assertiva.

**Principais Recursos:**

- **Requisitos de segurança:** o projeto prevê sugestões, simulações e testes de segurança para garantir a integridade dos dados e a proteção das informações dentro do sistema. Sugere-se principalmente a utilização de criptografia para a proteção dos dados, além de testes de segurança para garantir a integridade do sistema.

- **Requisitos de disponibilidade:** para a disponibilidade, o projeto propõe alguns mecanismos arquiteturais, como o uso de escalabilidade horizontal, sistema de mensageria com tecnologias como Kafka. Além disso, também é sugerido testes de carga recorrentes para o monitoramento da disponibilidade do sistema.

- **Requisitos de tempo de resposta:** o projeto também faz sugestões para o aperfeiçoamento do tempo de resposta do sistema, principalmente voltado para o processo de classificação, mas também abordando comandos de pesquisa e envio de novas invoices.

- **Requisitos de escalabilidade:** para a escalabilidade, o projeto propõe o uso de escalabilidade horizontal, e o start de instâncias automaticamente, para que o sistema possa se adaptar a demanda de processamento.

- **Requisitos de acuracidade:** para a acuracidade, o projeto propõe a utilização de um sistema de NLP para a classificação das invoices, além de um sistema de mensageria para o envio de mensagens de erro e alertas para os usuários.


## 📍 Como Começar:

1. Clone este repositório.
2. Instale as dependências necessárias.
3. Execute as simulações e testes.
4. Explore as documentações geradas para o projeto.


## 📁 Estrutura de pastas
📂 Grupo-04

  |--> Documentos

    📁 Apresentações

    📄 README.md
    
    📄 DocSistemaAtual.md
    
    📄 DocSistemaNovo.md
    
  |--> Front

    📄 app.js

    📄 estilo.css

    📄 index.html

    📄 logo.png

  |--> nn

    📁 data

    📄 1-preprocessing.ipynb

    📄 2-pipeline.ipynb

    📄 3-first-level-classification.ipnyb

    📄 4-second-level-classification.ipnyb

    📄 5-model-loader.ipnyb

  |--> Simulacao

    📁 assets

    📁 data_assets_simulation

    📁 documentation

    📁 RNF-01

    📁 RNF-02

    📁 RNF-03

    📁 RNF-04

    📁 RNF-05

    📁 RNF-06

    📁 RNF-07

    📁 RNF-08

    📁 RNF-09 and 10

    📁 RNF-11

    📄 data_tracebility.py

    📄 system_critical_points.py

  |--> SistemaAtual

    📁 assets

  |--> SistemaNovo

    📁 assets

    📁 src

      📁 alert-backend

      📁 app

      📁 Fila

      📁 ModeloAI

      📁 natural_language_processing

      📁 tests
      

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

- <b>front</b>: arquivos relacionado com a tela da IA.

- <b>documentos</b>: aqui estão todos os documentos do projeto e os slids das apresentações das sprints. 

- <b>nn</b>: arquivos relacionados com a IA.

- <b>Simulacao</b>: pastas com as simulações de cada requisito não funcional.

- <b>SistemaAtual</b>: documentação relacionado ao sistema atual.

- <b>SistemaNovo</b>: documentação relacionada ao sistema novo.

## 🔧 Instalação

Para a instalação desse projeto, é necessário ter alguns recursos instalados na máquina que irá executar. Nota-se que além das instalações necessárias, também destaca-se que é relevante a versão de cada uma dessas tecnologias, haja vista que podem ocorrer falhas na execução, devido a configuração do projeto.

## 👨‍💻 Tecnologias
- Jupyter Notebook
- Python
- JavaScript

## 📖 Histórico de lançamentos

**Versão 1.0 — 26/10/2023 (Sprint I)**

* Arquitetura do sistema atual

* Arquitetura do sistema novo

* Modelagem das simulações


**Versão 2.0 — 10/11/2023 (Sprint II)**

* Avaliação dos mecanismos de engenharia e de tecnologia utilizados no sistema atual

* Especificação da solução técnica do novo

* Simulação do sistema novo, incluindo as táticas e os componentes


**Versão 3.0 — 24/11/2023 (Sprint III)**

* Testes automatizados não funcionais

* Revisão do modelo de simulação novo


**Versão 4.0 — 08/12/2023 (Sprint IV)**

* Ajustes de implementação

* Evidências de testes não funcionais

* Identificação de Tradeoffs

* Medição do novo sistema
  

**Versão 5.0 — 21/12/2023 (Sprint V)**

* Últimos ajutes gerais

* Revisão do repositório do GitHub

* Arquivo de resumo do projeto


## 📋 Licença/License

<p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="#">Meta+3</a> by <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="#">Inteli, Bruno Meira, Luisa Vitória Leite Silva, Marcos Florencio
Marcos Moura
Pedro Gattai
Priscila Falcão</a> is 
licensed under <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"></a></p>

## 🎓 Referências

Natural Language Processing with Transformers, Chapter 1, L. Tunstall et al.

A recipe for training neural networks - Andrej Karpathy

The most common neural net mistakes - Andrej Karpathy @ Twitter

Yes you should understand backprop - Andrej Karpathy
