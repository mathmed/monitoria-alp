#Escreva um programa em Python que leia duas matrizes A e B, cada uma possuindo 3 × 3
#elementos inteiros, calcule e exiba a matriz soma S = A + B. Faça o mesmo para a matriz
#diferença D = A - B.
matriz1=[[],[],[]]
for i in range(3):
    for j in range(3):
        a=int(input('Digite um valor matriz 1 : '))
        matriz1[i].append(a)
print()
print('A primeira matriz é : ')
print(matriz1[0])
print(matriz1[1])
print(matriz1[2])

print()

matriz2=[[],[],[]]
for i in range(3):
    for j in range(3):
        a=int(input('Digite um valor matriz 2 : '))
        matriz2[i].append(a)
print()
print('A segunda matriz é: ')
print(matriz2[0])
print(matriz2[1])
print(matriz2[2])
print()
msoma=[[],[],[]]
for i in range(3):
    for j in range(3):
        soma=matriz1[i][j]+matriz2[i][j]
        msoma[i].append(soma)
print('A soma  das duas matrizes é: ')
print(msoma[0])
print(msoma[1])
print(msoma[2])

mdif=[[],[],[]]
for i in range(3):
    for j in range(3):
        sub=(matriz1[i][j])-(matriz2[i][j])
        mdif[i].append(sub)
print('A diferença das duas matrizes é: ')
print(mdif)
