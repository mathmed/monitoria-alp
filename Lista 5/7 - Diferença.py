 #Escreva um programa em Python que leia dois conjuntos de valores inteiros, cada um com
 #10 elementos, e armazene-os em duas listas A e B. Em seguida, o programa deve construir
 #o conjunto DIFERENÇA, que inclui apenas os elementos que estão na lista A e não estão na
 #lista B. Lembre-se que conjuntos não devem possuir elementos repetidos.
lista1=[]
cont1=0
while cont1 <10:
    a=int(input('Digite um valor inteiro para lista 1: '))
    if a not in lista1:
        lista1.append(a)
    cont1+=1
print()
print()
lista2=[]
cont2=0
while cont2 <10:
    b=int(input('Digite um valor inteiro para lista 2: '))
    if b not in lista2:
        lista2.append(b)
    cont2+=1
    
listafinal=[]
for a in lista1:
    if a not in lista2:
        listafinal.append(a)
    
print(listafinal)
