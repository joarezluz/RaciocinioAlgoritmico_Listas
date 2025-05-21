#1.	Desenvolva um programa que leia uma matriz quadrada de números inteiros de dimensão (4×4),
# e então coloque em um outro vetor de 4 posições o maior valor encontrado na coluna da matriz cujo índice é o mesmo do vetor,
# ou seja, o maior valor da coluna zero da matriz na posição zero do vetor e assim por diante.
# Mostre então a matriz, o vetor e a média aritmética do vetor.

m=[ [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]
   ]
v=[0,0,0,0]
linhas = 4
colunas = 4

for i in range(linhas):
    for ii in range(colunas):
       m[i][ii] = int(input(f'Insira um numero {i} {ii} :'))
       if i==0:
           v[i]=m[i][ii]
       elif m[i][ii]>=v[i]: v[i]=m[i][ii]

media=(v[0]+v[1]+v[2]+v[3])/4
print(f'Vetor: {v}\n Média: {media}' )