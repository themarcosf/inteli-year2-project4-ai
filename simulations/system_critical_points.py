# Modelo de simulação do atual
# Forma de comportamento no tempo os pontos críticos do sistema

import random
import matplotlib.pyplot as plt

num_transacoes = 100
transacoes = [random.randint(50, 150) for _ in range(num_transacoes)]

limiar_vulnerabilidade = 120
pontos_vulnerabilidade = [i for i, valor in enumerate(transacoes) if valor > limiar_vulnerabilidade]

plt.figure(figsize=(12, 6))
plt.plot(range(num_transacoes), transacoes, marker='o', linestyle='-', color='b', label='Transações')
plt.plot(pontos_vulnerabilidade, [transacoes[i] for i in pontos_vulnerabilidade], 'ro', label='Pontos de Vulnerabilidade')
plt.axhline(y=limiar_vulnerabilidade, color='r', linestyle='--', label='Limiar de Vulnerabilidade')
plt.xlabel('Tempo')
plt.ylabel('Valor da Transação')
plt.title('Simulação de Transações com Pontos de Vulnerabilidade')
plt.legend()
plt.show()
