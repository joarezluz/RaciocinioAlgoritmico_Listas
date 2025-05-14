#Construa a tabela de multiplicação de 1 a 10 utilizando apenas um laço de repetição.

m=[0,1,2,3,4,5,6,7,8,9,10]

for i in range(len(m)):
    for ii in range(11):
        print(i,' X ', m[ii], '=',i*m[ii])
    print("__")
