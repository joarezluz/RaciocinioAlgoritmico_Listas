#Escreva um programa que preencha uma matriz quadrada de números inteiros de dimensão (5×5)
#com valores inteiros (dentro do intervalo 10 a 99). Para cada uma das figuras abaixo (elabore quatro
#versões do programa): mostre a matriz original, mostre a matriz apenas com os valores que estão na
#parte hachurada e mostre a soma destes valores:

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

B=[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

C=[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

D=[
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]



for i in range(5):
    for ii in range(5):
        M[i][ii]=random.choice(range(10,99))
        if i % 2 == 0 and ii % 2 != 0: D[i][ii]=M[i][ii]
        if i % 2 != 0 and ii % 2 == 0: D[i][ii] = M[i][ii]


print("Matriz D")
for i in D:
    print(i)


