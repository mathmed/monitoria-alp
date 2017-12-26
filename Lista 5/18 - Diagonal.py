#. Escreva um programa em Python que gere aleatoriamente uma matriz 5 × 5 de números
#inteiros positivos. Em seguida, exiba a matriz original, seguido dos elementos da diagonal
#principal e dos elementos da diagonal secundária.

import random
lista=[]
for i in range(5):
    lista.append([])
    for j in range(5):
        lista[i].append(random.randint(0,9))
print()
print('A sua matriz gerada aleatóriamente é: ')
print()
for i in range(5):
    print(' | ' , end = '')
    for j in range (5):
        print(lista[i][j], end = '  ')
    print(' | ')

print("Os numeros da diagonal principal são:")
for i in range(5):
    print(lista[i][i], end=",")
print()
print('Os números da diagonal secundária são: ')
for i in range(5):
    lista[i].reverse()
for i in range(5):
    print(lista[i][i], end = ',')
    
