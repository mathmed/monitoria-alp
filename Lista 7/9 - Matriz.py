#. Escreva um programa em Python que gere e exiba uma matriz nula, de ordem N × N, onde o
#valor de N deverá ser fornecido pelo usuário. Lembre-se que a matriz nula é uma matriz
#onde os elementos são iguais a 0.

n=int(input('Digite a ordem da matriz : '))
matriz1=[]
for i in range (n):
    for i in range (n):
        matriz1.append(0)
    print(matriz1)
    matriz1=[]

