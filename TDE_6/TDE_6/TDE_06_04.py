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


#Matriz M
for i in range(5):
    for ii in range(5):
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
print("_______________________________")

#Matriz B
for i in range(5):
    for ii in range(5):
        if i == 0 : B[i][ii]=M[i][ii]
        if i == 1 and (ii == 0 or ii == 4): B[i][ii] = M[i][ii]
        if i == 2 and (ii == 0 or ii == 4): B[i][ii] = M[i][ii]
        if i == 3 and (ii == 0 or ii == 4): B[i][ii] = M[i][ii]
        if i == 4: B[i][ii] = M[i][ii]
        #if i % 2 != 0 and ii % 2 == 0: D[i][ii] = M[i][ii]

print("Matriz B")
for i in B:
    print(i)
print("_______________________________")





#Matriz C
for i in range(5):
    for ii in range(5):
        if i == 0 and ii == 1: C[i][ii]=M[i][ii]
        if i == 1 and (ii == 0 or ii == 2): C[i][ii] = M[i][ii]
        if i == 2 and (ii == 1 or ii == 3): C[i][ii] = M[i][ii]
        if i == 3 and (ii == 2 or ii == 3): C[i][ii] = M[i][ii]
        if i == 4 and ii == 3: C[i][ii] = M[i][ii]
        #if i % 2 != 0 and ii % 2 == 0: D[i][ii] = M[i][ii]

print("Matriz C")
for i in C:
    print(i)
print("_______________________________")


#___________________________________
for i in range(5):
    for ii in range(5):
        if i % 2 == 0 and ii % 2 != 0: D[i][ii]=M[i][ii]
        if i % 2 != 0 and ii % 2 == 0: D[i][ii] = M[i][ii]

print("Matriz D")
for i in D:
    print(i)


