# Descrição do RNF-03:
# O sistema deve apresentar um número acima de 95% em confiabilidade nas classificações taxonômicas unitárias.

import numpy as np
import matplotlib.pyplot as plt

# Simulação sistema atual:

transition_matrix_current = np.array([[0.65, 0.175, 0.175],
                                     [0.175, 0.65, 0.175],
                                     [0.175, 0.175, 0.65]])


current_state = np.array([1, 0, 0])

transition_matrix = np.array([[0.7, 0.3, 0.0],
                             [0.2, 0.7, 0.1],
                             [0.1, 0.1, 0.8]])

states = ['Technology/Telecom', 'Energy & Utilities', 'Logistics']

state_1_values_current = []
state_2_values_current = []
state_3_values_current = []
max_states_current = []

for i in range(10):
    print(f"Interação {i + 1} da cadeia de Markov - Sistema atual")
    new_state_vector = np.dot(current_state, transition_matrix_current)
    state_1_values_current.append(new_state_vector[0])
    state_2_values_current.append(new_state_vector[1])
    state_3_values_current.append(new_state_vector[2])

    max_state_index = np.argmax(new_state_vector)
    max_state = states[max_state_index]
    max_states_current.append(max_state)
    print(f"Novo estado: {max_state}")
    print(f"Mudança de probabilidade: {new_state_vector}")
    print("-------------------------------------------------------------")
    current_state = new_state_vector

plt.plot(state_1_values_current, label='Technology/Telecom')
plt.plot(state_2_values_current, label='Energy & Utilities')
plt.plot(state_3_values_current, label='Logistics')
plt.xlabel('Iteração')
plt.ylabel('Probabilidade')
plt.title('Comportamento da probabilidade Cadeia de Markov')
plt.legend()
plt.xticks(range(0, len(max_states_current), 1))
plt.show()

# Simulação sistema novo:

transition_matrix_new = np.array([[0.95, 0.025, 0.025],
                                 [0.025, 0.95, 0.025],
                                 [0.025, 0.025, 0.95]])


new_state = np.array([1, 0, 0])

states = ['Technology/Telecom', 'Energy & Utilities', 'Logistics']

state_1_values_new = []
state_2_values_new = []
state_3_values_new = []
max_states_new = []

for i in range(10):
    print(f"Interação {i + 1} da cadeia de Markov - Sistema novo")
    new_state_vector = np.dot(new_state, transition_matrix_new)
    state_1_values_new.append(new_state_vector[0])
    state_2_values_new.append(new_state_vector[1])
    state_3_values_new.append(new_state_vector[2])
    max_state_index = np.argmax(new_state_vector)
    max_state = states[max_state_index]
    max_states_new.append(max_state)
    print(f"Novo estado: {max_state}")
    print(f"Mudança de probabilidade: {new_state_vector}")
    print("-------------------------------------------------------------")
    new_state = new_state_vector


plt.plot(state_1_values_new, label='Technology/Telecom')
plt.plot(state_2_values_new, label='Energy & Utilities')
plt.plot(state_3_values_new, label='Logistics')
plt.xlabel('Iteração')
plt.ylabel('Probabilidade')
plt.title('Comportamento da probabilidade Cadeia de Markov')
plt.legend()
plt.xticks(range(0, len(max_states_new), 1))
plt.show()
