#Escreva um algoritmo leia dois números inteiros positivos a partir do teclado e determine o #
#máximo multiplo comum (mmc) desses números.#
n1=int(input('Digite o primeiro numero inteiro: '))
n2=int(input('Digite o segundo numero inteiro: '))
mdc1=[]                 # LISTA VAZIA
mdc2=[]                 # LISTA VAZIA
x=1                     # PRIMEIRO DIVISOR
while x<=n1:            # ENQUANTO NOSSO DIVISOR FOR IGUAL OU MENOR QUE NOSSO NUMERO, ELE AINDA VAI PODER SER UM DIVISOR
    if n1%x==0:     
        mdc1.append(x) # SE NOSSO NUMERO FOR DIVISIVEL, GUARDAMOS O DIVIDENDO NA LISTA
        x+=1           
    else:              # EM TODO CASO, X(DIVISOR) GANHA UM.
        x+=1
x=1
while x<=n2:
    if n2%x==0:                  #MESMA COISA AQUI
        mdc2.append(x)
        x+=1
    else:
        x+=1
print('Os divisores do seu primeiro número são: ')
print(mdc1)
print()                                                 #PRINTS MOSTRANDO NOSSOS DIVISORES.
print('Os divisores do seu segundo número são: ')
print(mdc2)
print()
i = 1                                              #VARIÁVEL PARA FACILITAR A OBTENÇÃO DE NÚMEROS DA LISTA
while True:                                        # ENQUANTO A CONDIÇÃO FOR VERDADEIRA, CONTINUAMOS
    if mdc1[-i] in mdc2:                         # SE -i(-1 NO CASO, NOSSO ULTIMO NÚMERO DA LISTA 1) ESTIVER NA LISTA 2....
        print('O maior divisor comum é:')
        print(mdc1[-i])                          # JÁ ENCONTRAMOS O NOSSO MAIOR DIVISOR.
        break                                   # PROGRAMA ACABA AQUI
    else:
        i=i+1   #CASO CONTRARIO, NOSSO i GANHA +1, FICANDO -2 POR CONTA DA FORMULA, ASSIM PROCURANDO O PENULTIMO NUMERO DA LISTA.
    
    

int(input())

    
    

