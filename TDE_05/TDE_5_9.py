#Desenvolva um programa que leia 10 números inteiros e armazene-os em um vetor chamado vLido.
#Depois, crie dois outros vetores: vPares, contendo somente os números pares de vLido, e vImpares
#contendo somente os números ímpares de vLido. Os vetores vPares e vLido não deverão conter
#zeros. Mostre então os três vetores

vLido=[]
vPares=[]
vImpares=[]
for i in range(10): #Solicitar 10 valores
    vLido.append(int(input(f"Insira um número na posisão {i}: ")))
for i in range(10):
    if vLido[i]%2==0:
        vPares.append(vLido[i])
    else:
        vImpares.append(vLido[i])
print(f"Os números pares são {vPares}")
print(f"Os números impares são {vImpares}")
print(f"Os números Lidos são {vLido}")
