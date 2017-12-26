#Escreva um algoritmo leia dois números inteiros positivos a partir do teclado e determine o #
#máximo multiplo comum (mmc) desses números.#
n1=int(input('Digite o primeiro numero inteiro: '))
n2=int(input('Digite o segundo numero inteiro: '))
x=2
mmc=[]
while n1>1:
    if n1%x==0:
        n1=n1/x
        mmc.append(x)
    else:
        x+=1
x=2
while n2>1:
    if n2%x==0:
        n2=n2/x
        mmc.append(x)
    else:
        x+=1
lista=len(mmc)
if lista ==1:
    print(mmc)
elif lista ==2:
    a,b = mmc[0],mmc[1]
    print(a*b)
elif lista==3:
    a,b,c=mmc[0],mmc[1],mmc[2]
    print(a*b*c)
elif lista ==4:
    a,b,c,d=mmc[0],mmc[1],mmc[2],mmc[3]
    print(a*b*c*d)
elif lista==5:
    a,b,c,d,e=mmc[0],mmc[1],mmc[2],mmc[3],mmc[4]
    print(a*b*c*d*e)
    

