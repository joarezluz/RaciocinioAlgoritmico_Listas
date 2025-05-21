#2.	Implemente um programa que permita multiplicar
# uma matriz de ordem (3×3) de números inteiros fornecida pelo
# usuário por um número também fornecido pelo usuário.

#Lembrete: para multiplicar uma matriz Am×n por um escalar k,
# basta multiplicar cada entrada aij de A por k.
# Assim, a matriz resultante B será também da ordem (m×n) e bij = k * aij.

A=[[0,0,0],
   [0,0,0],
   [0,0,0]]  #3x3
K=0
B=[[0,0,0],
   [0,0,0],
   [0,0,0]]

k=int(input('Insira um numero para multiplicar: '))
print('Insira os numeros da matriz')
for i in range (3):
    for ii in range (3):
        A[i][ii]=int(input(f'Numero inteiro: {i}::{ii}: '))
        B[i][ii]=k*A[i][ii]

print(B)