x=0
lista=[]
while x<10:
    num=int(input('Digite um número inteiro: '))
    lista.append(num)
    x+=1
print('Lista na ordem:' )
print(lista)
x=lista[::-1]
print(x)
print()
lista.sort()
print(lista)
lista.reverse()
print(lista)
