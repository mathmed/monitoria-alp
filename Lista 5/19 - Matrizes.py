 #Escreva um programa em Python que gere aleatoriamente e exiba uma matriz M × N de
 #números inteiros positivos. Em seguida, o programa deve possibilitar que o usuário efetue, à
 #sua livre escolha, a seguintes operações sobre a matriz gerada: a) Trocar a posição da linha L​1​ pela linha L​2​;
 #b) Multiplicar uma determinada linha L​1​ por um valor inteiro e armazene o resultado em L​1​;
 #c) Multiplicar uma determinada linha L​1 por um valor inteiro e some com outra linha L​2​,
 #armazenando o resultado em L​2​;
import random
matriz=[]
copia=matriz[:]
linhas=random.randint(2,6)
colunas=random.randint(2,6)
print('A matriz conterá %d linhas e %d colunas (Gerado aleatóriamente). ' % (linhas,colunas))
for i in range(linhas):
    matriz.append([])
    for j in range(colunas):
        matriz[i].append(random.randint(0,9))
print()
print('Abaixo sua matriz.')
for i in range(linhas):
    print(' | ' , end = '')
    for j in range (colunas):
        print(matriz[i][j], end = '  ')
    print(' | ')

print('Agora você poderá brincar com ela! Digite 1 para trocar a posição da linha L​1​ pela linha L​2.')
print()
print('Digite 2 para multiplicar uma determinada linha L​1​ por um valor inteiro e armazene o resultado em L​1​.')
print()
print('Digite 3 para multiplicar uma determinada linha L​1 por um valor inteiro e some com outra linha L​2​, armazenando o resultado em L​2​.!')
escolha=int(input())

if escolha ==1:
    a=matriz[0]
    matriz[0]=matriz[1]
    matriz[1]=a
    print('Abaixo sua matriz nova!')
    print()
    for i in range(linhas):
        print(' | ' , end = '')
        for j in range (colunas):
            print(matriz[i][j], end = '  ')
        print(' | ')
elif escolha ==2:
    b=int(input('Qual linha deseja multiplicar: '))
    valor=int(input('Digite um valor inteiro para multiplicar a linha: '))
    print()
    for j in range(colunas):
        x=matriz[b-1][j]
        x=x*valor
        matriz[b-1][j]=x
    print()
    print('Sua nova matriz:')
    for i in range(linhas):
            print(' | ' , end = '')
            for j in range (colunas):
                print(matriz[i][j], end = '  ')
            print(' | ')

elif escolha==3:
    b=int(input('Qual linha deseja multiplicar: '))
    valor=int(input('Digite um valor inteiro para multiplicar a linha: '))
    c=int(input('Agora escolha uma linha que, sua multiplicação será somada à ela: '))
    print()
    for j in range(colunas):
        x=matriz[b-1][j]
        x=x*valor
        y=matriz[c-1][j]
        y+=x
        matriz[c-1][j]=y
    print()
    print('Sua nova matriz:')
    for i in range(linhas):
        print(' | ' , end = '')
        for j in range (colunas):
            print(matriz[i][j], end = '  ')
        print(' | ')
else:
    print('Você digitou algo que não corresponde.')



            
