#A Amplitude amostral é uma médida de dispersão, ela é calculada como a diferença entre o valor
#máximo e o valor mínimo de uma amostra. Elabore um programa que leia um vetor de 10 posições
#inteiras e então mostre o valor máximo, o valor mínimo e a amplitude amostral do conjunto
#fornecido.

n1=[]
for i in range(10): #Solicitar 10 valores
    n1.append(int(input("Insira um numero: ")))
print(f"O valor maximo e {max(n1)}")
print(f"O valor minimo e {min(n1)}")
print(f"A amplitude amostral e {max(n1)-min(n1)}")