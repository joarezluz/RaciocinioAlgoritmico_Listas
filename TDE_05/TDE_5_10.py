#screva um programa que leia um vetor de números inteiros de 10 posições, aceitando apenas
#valores positivos. Modifique então o vetor de forma que, tenhamos primeiro todos os números pares,
#depois, os números impares. Mostre o vetor antes de depois da modificação.

n1=[]
for i in range(10): #Solicitar 10 valores
    n1.append(int(input(f"Insira um número na posisão {i}: ")))
for i in range(10):
    if n1[i]%2==0:
        n1[i]=n1[i]*2
print(f"O vetor antes de ser modificado é {n1}")
for ii in range(10):
    if n1[ii]%2!=0:
        n1[ii]=n1[ii]*2