import random
lista=[]
for i in range(20):
    a=random.randint(1,100)
    lista.append(a)
lista_pares=[]
lista_impares=[]
for x in lista:
    if x%2==0:
        lista_pares.append(x)
    else:
        lista_impares.append(x)

print('Lista com os números sorteados: ')
print(lista)
print()
print('Números sorteados pares: ')
print(lista_pares)
a=len(lista_pares)
print('A lista tem tem %d elementos. ' % a)
print()
print('Números sorteados ímpares: ')
print(lista_impares)
y=len(lista_impares)
print('A lista tem %d elementos. ' % y)
