# Implemente uma máquina de venda de bebidas em Python,

M = [
    [0, "Coca-Cola", 3.75, 2],  # M[0]
    [1, "Pepsi", 3.67, 5],  # M[1]
    [2, "Monster", 9.96, 1],  # M[2]
    [3, "Café", 1.25, 100],  # M[3]
    [4, "Redbull", 13.99, 2]  # M[4]
]

lig = 1
sel = 0

def calcular_Ntroco(vTotal, vPago):
    NotasC = [
        ['R$ 200,00',20000,10],
        ['R$ 100,00',10000,50],
        ['R$ 50,00',5000,50],
        ['R$ 20,00',2000,100],
        ['R$ 10,00',1000,100],
        ['R$ 5,00',500,100],
        ['R$ 2,00',200,100],
        ['R$ 1,00',100,100],
        ['R$ 0,50',50,100],
        ['R$ 0,25',25,100],
        ['R$ 0,10',10,100],
        ['R$ 0,05',5,100]
    ]

    # Tranformando em centavos
    troco = round(vPago * 100 - vTotal * 100)

    resultado = {}
    restante = troco

    for nome, valor_centavos, qN in NotasC:
        quantidade = restante // valor_centavos
        if quantidade > 0:
            resultado[nome] = quantidade
            restante -= quantidade * valor_centavos
        if restante == 0:
            break

    return troco / 100, resultado



while lig == 1:  # apenas para loop
    if 0 <= sel <= 4:
        print("Produtos\nCódigo | Babida | Valor em R$ | Quantidade")
        for l in M:
            print(l)
        sel = int(input("Selecione um produto digitando seu código: "))
    else:
        sel = int(input("Selecione um produto digitando seu código CORRETO: "))
    if 0 <= sel <= 4:
        print(M[sel][1])
        if M[sel][3] > 0:
            print(f"Valor: R${M[sel][2]}")
            pag = float(input('Insira o valor:'))
            if (pag >= M[sel][2]):
                troco, notas = calcular_Ntroco(M[sel][2], pag)
                print(f"Troco :{troco:.2f}")
                for NotasC, quantidade in notas.items():
                    print(f"{quantidade} x {NotasC}")
                M[sel][3] -= 1
            else:
                print("Insira um valor maior ou igual ao do produto")

        else:
            print("Sem estoque")


