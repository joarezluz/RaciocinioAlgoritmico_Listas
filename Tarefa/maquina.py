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

admSel=[0,0,0,0,0,0,0]

def admin():
    print('#################################\n'
          'Modo Administrativo')
    admSel[0] = int(input('0 -> Alterar produto \n1-> Inserir produto \n2-> Sair do modo Administrativo\n'))

    while admSel[0]<2:

        if admSel[0]==0:
            print('Alteracao de produto')
            if admSel[0] == 0:
                for lin in M:
                    print(lin)
            admSel[1] = int(input('0-> Quantidade\n1-> Valor\n2->Voltar\n'))

            if admSel[1]==0: #quantidade

                for l in M:
                    print(l) #mostrar estoque
                admSel[2]=int(input('Selecione o produto:'))
                print(M[admSel[2]])
                M[admSel[2]][3]=int(input('Insira um novo valor de estoque: '))
                print('Quantidade  alterada com sucesso!')
                print(M[admSel[2]])
            if admSel[1]==1: #valor
                for l in M:
                    print(l) #mostrar estoque
                admSel[2] = int(input('Selecione o produto:'))
                M[admSel[2]][2] = int(input('Insira um novo valor de estoque: '))
                print('Valor  alterado com sucesso!')
                print(M[admSel[2]])
            if admSel[1] == 2:
                admSel[0] = int(input('0 -> Alterar produto \n1-> Inserir produto \n2-> Sair do modo Administrativo\n'))
        if admSel[0]==1:
            admSel[3]= str(input('Insira o NOME do produto: '))
            admSel[4]=float(input('Insira o VALOR do produto: '))
            admSel[5]=int(input('Insira a QUANTIDADE do produto: '))
            admSel[6]=len(M) #Cria um novo c[odigo
            linhaTemp=[admSel[6],admSel[3],admSel[4],admSel[5]] #gera um vetor o produto
            M.append(linhaTemp)
            print('Produto cadastrado com sucesso!')
            for li in M:
                print(li)
            admSel[0]=-1
            admSel[0] = int(input('0 -> Alterar produto \n1-> Inserir produto \n2-> Sair do modo Administrativo\n'))


    print('Saindo do modo administrativo\n#################################')


def calcular_Ntroco(vTotal, vPago):
    NotasC = [
        ['R$ 200,00',20000,100],
        ['R$ 100,00',10000,100],
        ['R$ 50,00',5000,100],
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

    troco = round(vPago * 100 - vTotal * 100) # Tranformando em centavos
    templi=[]

    resultado = {}
    restante = troco

    for nome, valor_centavos, qN in NotasC:
        if qN >0:
            temTroco =1
            quantidade = restante // valor_centavos
            if quantidade > 0 and qN >0 :
                resultado[nome] = quantidade
                restante -= quantidade * valor_centavos
                #templi[0]=nome
                #templi[0]=valor_centavos
                #print(templi)
                #print(NotasC[nome][int(valor_centavos)][2])# -= 1  # subtrai as notas
            if restante == 0:
                break
            #NotasC[valor_centavos][2] -= 1  # subtrai as notas
        elif (troco/100)>0.04:
            temTroco = 0
    #for nots in NotasC:
    #    print(nots)
    return troco / 100, resultado , temTroco


qtProd=len(M) # Quantidade de tipos de produtos
while lig == 1:  # apenas para loop
    if 0 <= sel <= (qtProd-1): # lida apenas com os produtos cadastrados indice 0
        print('##########----Bem Vindo---##########\n'
              '#####---Selecione o codigo do produto----####')
        print("Produtos\nCódigo | Babida | Valor em R$ | Quantidade")
        for l in M:
            print(l)
        sel = int(input("Selecione um produto digitando seu código: "))
    elif 99> sel >0:
        sel = int(input("Selecione um produto digitando seu código CORRETO: "))
    if sel == 99:
        admin()
    if 0 <= sel <= (qtProd-1):
        print(M[sel][1])
        if M[sel][3] > 0:
            print(f"Valor: R${M[sel][2]}")
            pag = float(input('Insira o valor:'))
            if (pag >= M[sel][2]):
                troco, notas, tem= calcular_Ntroco(M[sel][2], pag)
                print(f"Troco :{troco:.2f}")
                if tem==1:#verifica se tem notas
                    for NotasC, quantidade in notas.items():
                        print(f"{quantidade} x {NotasC}")
                    M[sel][3] -= 1
                else: print('Compra cancelada por falta de troco\n '
                            '##############################################')
            else:
                print("Insira um valor maior ou igual ao do produto")

        else:
            print("Sem estoque\n"
                  "##############################################")


