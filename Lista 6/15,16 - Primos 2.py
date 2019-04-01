a=int(input('Digite o primeiro número a partir dele veremos os primos, PS: (Maior que 2):'))
b=int(input('Digite o último numero: '))
divisores=0
while a<=b: # se a for menor q b o while vai rodar
    for i in range(1,a+1): #a ganha 1
        if a%i==0:
            divisores+=1
    if divisores==2:
        print(a)
    divisores=0
    a+=1
