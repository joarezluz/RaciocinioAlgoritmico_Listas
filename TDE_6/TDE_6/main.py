import random

# Gerar 16 números únicos entre 100 e 999
numeros = list(range(100, 1000))
random.shuffle(numeros)
elementos_matriz = numeros[:16]

# Construir a matriz 4x4
matriz = [elementos_matriz[i*4 : (i+1)*4] for i in range(4)]

# Encontrar o maior elemento e sua linha
maior_valor = None
linha_maior = 0

for indice_linha, linha in enumerate(matriz):
    for elemento in linha:
        if maior_valor is None or elemento > maior_valor:
            maior_valor = elemento
            linha_maior = indice_linha

# Encontrar o menor elemento na linha do maior valor
menor_na_linha = min(matriz[linha_maior])

# Exibir a matriz formatada
print("Matriz 4x4:")
for linha in matriz:
    print(" ".join(f"{numero:3}" for numero in linha))

# Exibir os resultados
print(f"\nMaior elemento da matriz: {maior_valor}")
print(f"Menor elemento na linha do maior valor: {menor_na_linha}")