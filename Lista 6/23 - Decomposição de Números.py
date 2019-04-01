
#Escreva um algoritmo leia um número inteiro positivo do teclado e obtenha a sua#
#decomposição em fatores primos. Por exemplo, 360 = 23×32×5. #
num=int(input('Digite o número a ser decomposto: '))
x=2 #NOSSO PRIMO DIVISOR INICIAL
divisores=[] #AQUI NESSA LISTA VAI SER GUARDADO NOSSOS PRIMOS
while num>1: # ENQUANTO NOSSO NUMERO FOI MAIS Q 1 (SUA MAIOR FATORAÇÃO) CONTINUAREMOS PEGANDO PRIMOS.
    if num%x==0: # SE O RESTO DO NOSSO NUMERO DIVIDIDO PELO PRIMEIRO PRIMO DER 0 ...
        num=num/x # NOSSO NUMERO VAI SER DIVISIVEL POR X.
        divisores.append(x) # ENTÃO GUARDAMOS O X SENDO UM PRIMO EM NOSSA LISTA
    else:
        x+=1 # SE NÃO, TUDO AQUILO É PULADO E ENTÃO NOSSO NOVO PRIMO É 3.
print('Os fatores primos são: ')
print(divisores) # NO FINAL MOSTRAMOS NOSSA LISTA COM OS PRIMOS DENTRO.
