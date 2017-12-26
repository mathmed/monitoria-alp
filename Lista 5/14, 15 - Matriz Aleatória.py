#Escreva um programa em Python que gere e exiba uma matriz 5 × 5 a partir de números
#inteiros positivos gerados aleatoriamente dentro do intervalo de 1 a 99. Use a função              
#random.randint(a,b)​ para gerar os números aleatoriamente
# Modifique o programa anterior de forma que ele exiba as posições (linha e coluna) do maior
#e do menor elemento da matriz que foi gerada aleatoriamente. 
import random
lista=[]
for i in range(5):
    lista.append([])
    for j in range(5):
        lista[i].append(random.randint(1,99))

for i in range(5):
    print(' | ' , end = '')
    for j in range (5):
        print(lista[i][j], end = '  ')
    print(' | ')



        
maior = 0
for i in range(5):
    for j in range(5):
        if lista[i][j] > maior:
            maior=lista[i][j]
            linha=i+1
            coluna=j+1
            
print(' O maior número da matriz é %d, e sua posição é: Linha %d, Coluna %d !! ' % (maior,linha,coluna))


menor=0
for i in range(5):
    for j in range(5):
        if lista[i][j] < maior:
            menor=lista[i][j]
            maior=menor
            linha=i+1
            coluna=j+1
            
print(' O menor número da matriz é %d, e sua posição é: Linha %d, Coluna %d !! ' % (menor,linha,coluna))




