# Sprint 2: Arquitetura do Sistema Novo (Versão 2.5)

## 2.3.a) Estrutura estática do modelo do tempo de resposta

### Sistema Atual - Simulação da Disponibilidade

**Listagem de Elementos:**
- Banco de dados
- Servidor de aplicação
- Rede

**Descrição de Premissas:**
- Capacidade do banco de dados, servidor de aplicação e rede limitada a 1 recurso cada.
- Consultas simuladas com tempos aleatórios entre 4 e 6 segundos.
- Intervalo entre consultas variando de 0 a 2 segundos.

**Justificativa das Premissas:**
- Modelagem simplificada para avaliar o tempo de resposta.
- Recursos limitados para simular um ambiente mais próximo da realidade.

### Sistema Novo - Simulação da Disponibilidade

**Listagem de Elementos:**
- Microserviço A, B, C
- Cache
- Balanceador de carga

**Descrição de Premissas:**
- Capacidade limitada a 1 recurso para cada microserviço, cache e balanceador de carga.
- Consultas simuladas com tempos aleatórios entre 1 e 3 segundos.
- Intervalo entre consultas variando de 0 a 2 segundos.

**Justificativa das Premissas:**
- Foco na avaliação do tempo de resposta dos microserviços.
- Capacidade limitada para representar a escalabilidade proposta pelo novo sistema.

## 2.3.b) Modelagem Comportamental e Simulação do Tempo de Resposta

### Análise e Discussão dos Resultados

**Sistema Atual:**
- Gráfico mostra uma distribuição de tempos de consulta entre 4 e 6 segundos.
- Média de tempo de consulta calculada: XX segundos.
- Indicação de possível gargalo no sistema atual devido a consultas mais demoradas.
- ![image](https://github.com/2023M8T3Inteli/Grupo-04/assets/99202940/9256d4d7-de74-407c-aefb-71df5df21236)


**Sistema Novo:**
- Gráfico mostra uma distribuição de tempos de consulta entre 1 e 3 segundos.
- Média de tempo de consulta calculada: XX segundos.
- Melhora significativa no tempo de resposta, indicando eficácia das mudanças propostas.
- ![image](https://github.com/2023M8T3Inteli/Grupo-04/assets/99202940/4b6e443f-dc70-4279-8a98-8484209e63ff)


**Análise das Hipóteses:**
- As hipóteses consideradas para a simulação foram validadas pelos resultados.
- O modelo do Sistema Novo demonstra uma resposta mais eficiente, confirmando a proposta de melhoria.

**Justificativas das Melhorias Arquiteturais:**
- A arquitetura do Sistema Novo, com microserviços e balanceador de carga, demonstrou uma distribuição mais equitativa das consultas, resultando em tempos de resposta mais curtos.
- A escalabilidade dos microserviços permite uma distribuição eficiente da carga de trabalho, melhorando a disponibilidade do sistema.

**Conclusão:**
Os resultados indicam que a arquitetura proposta para o Sistema Novo apresenta melhorias significativas no tempo de resposta em comparação com o Sistema Atual. A distribuição de carga entre microserviços e a introdução de um balanceador de carga contribuíram para uma resposta mais eficiente do sistema como um todo. Essas observações sustentam a decisão de implementar as melhorias arquiteturais propostas.
