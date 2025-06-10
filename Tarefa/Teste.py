def calcular_Ntroco(vTotal, vPago):
    NotasC = [
        ['R$ 200,00',20000],
        ['R$ 100,00',10000],
        ['R$ 50,00',5000],
        ['R$ 20,00',2000],
        ['R$ 10,00',1000],
        ['R$ 5,00',500],
        ['R$ 2,00',200],
        ['R$ 1,00',100],
        ['R$ 0,50',50],
        ['R$ 0,25',25],
        ['R$ 0,10',10],
        ['R$ 0,05',5]
    ]

    # Tranformando em centavos
    troco = round(vPago * 100 - vTotal * 100)

    resultado = {}
    restante = troco

    for nome, valor_centavos in NotasC:
        quantidade = restante // valor_centavos
        if quantidade > 0:
            resultado[nome] = quantidade
            restante -= quantidade * valor_centavos
        if restante == 0:
            break

    return troco / 100, resultado


# Exemplo de uso
valor_total = 100.3
valor_pago = 200.00

troco, moedas_notas = calcular_Ntroco(valor_total, valor_pago)
print(f"Troco total: R$ {troco:.2f}")
print("Detalhamento:")
for NotasC, quantidade in moedas_notas.items():
    print(f"{quantidade} x {NotasC}")