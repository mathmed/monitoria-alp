# Escreva um programa em Python que gere aleatoriamente uma matriz 5 × 5 de números
#inteiros positivos e crie uma nova matriz, a partir da matriz original, com os elementos
#ordenados em ordem crescente. Exiba a matriz original e a matriz ordenada.

import random
matriz=[]
for i in range(5):
    matriz.append([])
    for j in range(5):
        matriz[i].append(random.randint(0,20))

print('A sua matriz gerada aleatóriamente é: ')       
for i in range(5):
    print(' | ' , end = '')
    for j in range (5):
        print(matriz[i][j], end = '  ')
    print(' | ')

print()
print()
print()
print('Sua matriz ordenada é: ')
print()
for i in range(5):
    matriz[i].sort()

for i in range(5):
    print(' | ' , end = '')
    for j in range (5):
        print(matriz[i][j], end = '  ')
    print(' | ')
