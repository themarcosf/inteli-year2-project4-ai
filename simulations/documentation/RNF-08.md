## Sprint 2: Arquitetura do Sistema Novo (Versão 2.5) - Simulação do Tempo de Resposta

---

### 2.3.a) Estrutura estática do modelo do tempo de resposta:

**Listagem de elementos envolvidos para a simulação da disponibilidade do sistema atual:**
- Módulos: Sistema, Ambiente de Simulação (Simpy), Random (para introduzir aleatoriedade).
- Componentes: Funcionamento contínuo do sistema, detecção de falhas, e tempo de inatividade simulado.
- Serviços: Timeout para a operação normal do sistema.

**Descrição de premissas envolvidas para a simulação da disponibilidade do sistema atual:**
A premissa fundamental é que o sistema opera normalmente por um período de tempo e pode sofrer falhas com uma probabilidade de 10%.

**Justificativa das premissas envolvidas para a simulação da disponibilidade do sistema atual:**
Essa abordagem reflete uma situação realista em que o sistema pode operar sem falhas durante um intervalo de tempo, mas existe uma chance de ocorrer uma falha, resultando em um tempo de inatividade simulado.

**Descrição de hipóteses consideradas para a simulação da disponibilidade das melhorias do sistema novo:**
Para a simulação das melhorias no sistema novo, hipóteses adicionais foram consideradas, como a introdução de microservices com probabilidades de falha distintas.

**Listagem de elementos envolvidos para a simulação da disponibilidade do sistema novo:**
Além dos elementos do sistema atual, foram incluídos microservices como novos componentes, cada um com suas probabilidades de falha e tempos de manutenção.

**Descrição de premissas envolvidas para a simulação da disponibilidade do sistema novo:**
A premissa central é a introdução de microservices com diferentes probabilidades de falha e manutenção, refletindo uma arquitetura mais complexa.

**Justificativa das premissas envolvidas para a simulação da disponibilidade do sistema novo:**
A complexidade adicional visa representar de maneira mais precisa um ambiente de produção onde diferentes componentes do sistema podem falhar de forma independente.

---

### 2.3.b) Modelagem comportamental e simulação do tempo de resposta:

**Análise e discussão textual de resultados obtidos com a simulação do sistema atual:**
Os resultados da simulação do sistema atual mostram que, ao longo do tempo, o sistema opera normalmente, mas ocasionalmente experimenta falhas. A taxa de falhas foi calculada em 10%, resultando em um tempo total de inatividade durante o período simulado.
![Captura de tela de 2023-11-15 09-22-53](https://github.com/2023M8T3Inteli/Grupo-04/assets/99202940/3ef9db99-dbf8-4d78-bcfd-3a4fb54b545c)


**Análise e discussão textual de resultados obtidos com a simulação do sistema novo:**
A simulação do sistema novo, com a introdução de microservices, revela um comportamento mais complexo. Cada microservice contribui para a disponibilidade geral do sistema, com algumas partes permanecendo operacionais enquanto outras podem falhar. A análise inclui a comparação da porcentagem de disponibilidade em relação ao sistema anterior.
![image](https://github.com/2023M8T3Inteli/Grupo-04/assets/99202940/690f3c7f-3b1b-4bdb-b33b-da5ac0b632fb)


**Análise e discussão textual das hipóteses a partir da comparação dos resultados de simulação do sistema atual e do sistema novo (1.0):**
Comparando os resultados, verifica-se que a introdução de microservices pode melhorar ou deteriorar a disponibilidade, dependendo das probabilidades de falha e dos tempos de manutenção atribuídos a cada componente. As hipóteses iniciais são, portanto, validadas ou ajustadas com base nas observações da simulação.

**Justificativas das melhorias arquiteturais propostas a partir dos resultados da simulação:**
Com base nos resultados, as melhorias arquiteturais propostas incluem ajustes nas probabilidades de falha e tempos de manutenção dos microservices para otimizar a disponibilidade global do sistema. Essas modificações são fundamentadas na busca pelo equilíbrio entre a complexidade do sistema e sua confiabilidade.

---
