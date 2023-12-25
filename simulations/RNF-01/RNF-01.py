# Descrição do RNF-01:
# O sistema deve apresentar acurácia acima de 95% em acurácia nas classificações taxonômicas. 

import numpy as np
import matplotlib.pyplot as plt

# Simulação sistema atual:

transition_matrix_atual = np.array([[0.6, 0.3, 0.1],
                             [0.2, 0.7, 0.1],
                             [0.1, 0.2, 0.7]])


initial_state_atual = np.array([0.4, 0.5, 0.1])


states_atual = []
states_atual.append(initial_state_atual)


current_state_atual = initial_state_atual
for i in range(1, 11):
    current_state_atual = np.dot(current_state_atual, transition_matrix_atual)
    states_atual.append(current_state_atual)


# Simulação sistema novo:

transition_matrix_novo = np.array([[0.9, 0.08, 0.02],
                             [0.1, 0.8, 0.1],
                             [0.05, 0.15, 0.8]])


initial_state_novo = np.array([0.1, 0.2, 0.7]) 

states_novo = []
states_novo.append(initial_state_novo)


current_state_novo = initial_state_novo
for i in range(1, 11):
    current_state_novo = np.dot(current_state_novo, transition_matrix_novo)
    states_novo.append(current_state_novo)

states_atual = np.array(states_atual)
states_novo = np.array(states_novo)

# Gerar Gráficos:

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(states_atual)
plt.title('Sistema Atual - Evolução da Acurácia')
plt.xlabel('Iterações')
plt.ylabel('Probabilidade')
plt.legend(['Baixa Acurácia', 'Média Acurácia', 'Alta Acurácia'])

plt.subplot(1, 2, 2)
plt.plot(states_novo)
plt.title('Sistema Novo - Evolução da Acurácia')
plt.xlabel('Iterações')
plt.ylabel('Probabilidade')
plt.legend(['Baixa Acurácia', 'Média Acurácia', 'Alta Acurácia'])

plt.tight_layout()
plt.show()
