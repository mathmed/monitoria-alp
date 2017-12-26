#Escreva um programa em Python que leia uma matriz 3 × 3 de elementos inteiros, crie e
#exiba a matriz transposta. Ou seja, o elemento A[1][2] é trocado pelo A[2][1]; o A[1][3] pelo
#A[3][1]; o A[2][5] pelo A[5][2] e assim por diante.

m=[[],[],[]]
for i in range(3):
    for j in range(3):
        a=int(input('Adicione para linha %.0d posição %.0d:' %(i+1,j+1)))  # CRIANDO A MATRIZ
        m[i].append(a)
print('Sua matriz está feita: ')
for i in range(3):
    print(' | ', end = '  ')
    for j in range(3):
        print(m[i][j] , end = '  ')
    print(' | ')
print()
print()
print('A matriz transposta é: ')
for i in range(3):
    print(' | ' , end = '  ')
    for j in range(3):
        print(m[j][i] , end = '  ')
    print( " | ")
    

