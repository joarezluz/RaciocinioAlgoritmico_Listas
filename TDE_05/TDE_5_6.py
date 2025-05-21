#Dizemos que um número natural é triangular se ele é produto de três números naturais consecutivos.
#Exemplo: 120 é triangular, pois 4.5.6 = 120. Dado um inteiro não-negativo n, verificar se n é
#triangular.

n1=int(input("Insira um numero: "))
i=1
t=0
while i < n1:
    n2=i* (i-1) * (i-2)
    if n2 == n1:
        print(f"E triangular pois {n1} = {i} x {i-1} x {i-2}")
        t=1
    i+=1
if t==0:
    print("Nao e triangular")