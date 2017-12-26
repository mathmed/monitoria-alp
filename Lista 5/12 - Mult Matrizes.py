#Escreva um programa em Python que leia duas matrizes 3 × 3 de elementos inteiros e
#calcule a matriz produto M = A x B. Dica: Atente para o procedimento de multiplicação de matrizes.

matriz1=[[],[],[]]
for i in range(3):
    for j in range(3):
            a=int(input('Adicione um inteiro para matriz 1:'))  # CRIANDO A PRIMEIRA MATRIZ
            matriz1[i].append(a)
print(matriz1)

matriz2=[[],[],[]]
for i in range(3):
    for j in range(3):
        a=int(input('Adicione um inteiro para matriz 2:')) # CRIANDO A SEGUBDA MATRIZ
        matriz2[i].append(a)
print(matriz2)
print()

mult=[[],[],[]]            # MATRIZ DA MULTIPLICAÇÃO
for i in range (3):
    a=0
    for j in range(3):
        soma=(matriz1[0][j])*(matriz2[j][i])     # PRIMEIRA LINHA DA MATRIZ DE MULT
        a+=soma
    mult[0].append(a)
for i in range (3):
    a=0
    for j in range(3):
        soma=(matriz1[1][j])*(matriz2[j][i])    # SEGUNDA LINHA DA MATRIZ DE MULT
        a+=soma
    mult[1].append(a)
for i in range (3):
    a=0
    for j in range(3):
        soma=(matriz1[2][j])*(matriz2[j][i])    # TERCEIRA LINHA DA MATRIZ DE MULT
        a+=soma
    mult[2].append(a)
print(mult)
