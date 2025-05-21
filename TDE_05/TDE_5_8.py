#Elabore um programa que leia um vetor de 10 posições inteiras. Depois, solicite para o usuário um
#número que ele gostaria de pesquisar neste vetor, caso o número exista no vetor, mostre em qual(is)
#posição(ões) ele foi encontrado e quantas ocorrências foram detectadas.

m=[]
n2=[]
for i in range(10): #Solicitar 10 valores
    m.append(int(input(f"Insira um número na posisão {i}: ")))
n1=input("Insira um número para pesquisar: ")
for ii in range(10):
    if m[ii]==int(n1):
        n2.append(ii)
print(f"O número {n1} foi encontrado nas posições {n2}")
