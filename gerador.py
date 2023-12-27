import matplotlib.pyplot as plt

aux = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # lista com a quantidade de números em cada coluna
vetor = []  # lista com os números gerados
M = 2147483647  # módulo
n = 10000  # tamanho do vetor
a = 19  # multiplicador
seed = 2  # semente
e = n / 10  # esperado
qui_square = 0

for i in range(n):
    num_aleatorio = (seed * a) % M
    seed = num_aleatorio
    num_aleatorio = float(num_aleatorio / M)
    vetor.append(num_aleatorio)

# Teste de qui-quadrado
for i in range(n):
    if 0 <= vetor[i] < 0.1:
        aux[0] += 1
    elif 0.1 <= vetor[i] < 0.2:
        aux[1] += 1
    elif 0.2 <= vetor[i] < 0.3:
        aux[2] += 1
    elif 0.3 <= vetor[i] < 0.4:
        aux[3] += 1
    elif 0.4 <= vetor[i] < 0.5:
        aux[4] += 1
    elif 0.5 <= vetor[i] < 0.6:
        aux[5] += 1
    elif 0.6 <= vetor[i] < 0.7:
        aux[6] += 1
    elif 0.7 <= vetor[i] < 0.8:
        aux[7] += 1
    elif 0.8 <= vetor[i] < 0.9:
        aux[8] += 1
    else:
        aux[9] += 1

# Cálculo do qui-quadrado
for i in range(10):
    qui_square += ((aux[i] - e) ** 2) / e

print("Valor do qui-quadrado:", qui_square)

# Visualização do histograma
plt.bar([f"{i/10:.1f}-{(i+1)/10:.1f}" for i in range(10)], aux)
plt.show()
