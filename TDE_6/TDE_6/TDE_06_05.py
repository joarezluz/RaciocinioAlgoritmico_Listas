#Escreva um programa que popule uma matriz (15×7) de números inteiros sorteados dentro do
#intervalo 10 a 99. Modifique então a matriz de forma que, caminhando da esquerda para a direita, de
#cima para baixo, tenhamos primeiro todos os números pares, depois, os números impares. Mostre a
#matriz antes e depois da modificação.

import random
M =[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

A=[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]





#Matriz M
for i in range(15):
    for ii in range(7):
        M[i][ii]=random.choice(range(10,99))

print("Matriz M")
for i in M:
    print(i)
#_______________________________________


print("_______________________________")
#Matriz A
for i in range(5):
    for ii in range(5):
        if i == 0 and ii == 2: A[i][ii]=M[i][ii]
        if i == 1 and ii == 2: A[i][ii] = M[i][ii]
        if i == 2: A[i][ii] = M[i][ii]
        if i == 3 and ii == 2: A[i][ii] = M[i][ii]
        if i == 4 and ii == 2: A[i][ii] = M[i][ii]
        #if i % 2 != 0 and ii % 2 == 0: D[i][ii] = M[i][ii]

print("Matriz A")
for i in A:
    print(i)