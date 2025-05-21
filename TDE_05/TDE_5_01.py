#1)Construa a tabela de multiplicação de 1 a 10. (Ex: 1x1 = 1, 1x2=2, 10x10 =100)

m=[0,1,2,3,4,5,6,7,8,9,10]

for i in range(len(m)): #primeira tabela
    for ii in range(11):
        if ii!=0: print(i,' X ', m[ii], '=',i*m[ii])
    print("__")
