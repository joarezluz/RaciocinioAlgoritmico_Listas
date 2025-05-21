#Leia três números do teclado e verificar se o primeiro é maior que a soma dos outros dois.

n1 = input("Insira o primeiro numero: ")
n2 = input("Insira o segundo numero: ")
n3 = input("Insira o terceiro numero: ")

a=n3+n2
if n1>a:
    print("O primeiro numero e maior")
else:
    print("O primeiro numero nao e maior")