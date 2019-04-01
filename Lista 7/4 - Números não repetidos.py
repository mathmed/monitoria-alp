#4. Escreva um programa em Python que leia um conjuntos de N valores inteiros até que seja
#suficiente para construir um conjunto com 10 elementos. Lembre-se que conjuntos não
#devem possuir elementos repetidos, assim os elementos repetidos devem ser descartados.
#Os elementos devem ser armazenados em uma lista, que deverá ser exibida no final do  programa.

lista=[]
cont=0
while cont <10:
    a=int(input('Digite um valor inteiro: '))
    if a not in lista:
        lista.append(a)
        cont+=1
    cont=cont
print(lista)
   
