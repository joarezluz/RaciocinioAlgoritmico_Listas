# 3.	Elabore um programa que preencha uma matriz quadrada
# (4x4) de números inteiros, sorteados dentro do intervalo 100 a 999,
# garantindo que não haverá nenhuma repetição (os 16 números devem ser únicos).
# Encontre então o valor do menor elemento da linha em que se encontra o maior elemento da matriz.
# Mostre a matriz e os dois valores encontrados.
from typing import List

import random
M =[
   [0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 0, 0, 0],
   [0, 0, 0, 0]
]

k=[]
for i in range(4):
   for ii in range(4):
         M[i][ii]=random.choice(range(100,999))
         if M[i][ii] not in k: k.append(M[i][i])
         else:
            M[i][ii] = random.choice(range(100, 999))


print(M)