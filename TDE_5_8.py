#Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um
#número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is)
#posição(ões) ele foi encontrado e quantas ocorrências foram detectadas.

m=[]
for i in range(10): #Solicitar 10 valores
    m.append(int(input(f"Insira um numero na posisão {i}: ")))
n1=input("Insira um número para pesquisar: ")
for ii in range(10):
    if m[ii]==int(n1):
        print(f"O numero {n1} foi encontrado na posição {ii}")