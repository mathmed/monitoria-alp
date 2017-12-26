#. Escreva um programa em Python que leia uma matriz 3 × 4 de números inteiros positivos,
#exiba a matriz lida e a soma dos elementos de cada linha da matriz. 
matriz=[]
import random
for i in range(3):
    matriz.append([])
    for j in range(4):
        matriz[i].append(random.randint(0,20))

print('A sua matriz gerada aleatóriamente é: ')       
for i in range(3):
    print(' | ' , end = '')
    for j in range (4):
        print(matriz[i][j], end = '  ')
    print(' | ')
print()
print()
print('A soma dos elementos das linhas é: ')
lista=[]
for i in range(3):
    a=0
    for j in range(4):
        soma=matriz[i][j]
        a=soma+a
    lista.append(a)

for i in range(3):
    print('A soma da linha %d é: ' % (i+1))
    print(lista[i])
