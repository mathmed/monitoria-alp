ano=int(input('Digite um ano: '))
mes=int(input('Digite um mês: '))
dia=int(input('Digite um dia: '))
if ano>0:
    if mes>=1 and mes<=12:
        if dia>=1 and dia<=31:
            print('Data válida.')
        else:
            print('Data inválida.')
    else:
            print('Data inválida.')
else:
    print('Data inválida.')
print()
if ano%100==0:
    print('Ano Bissexto.')
elif ano % 4==0:
    if ano%100!=0:
        print('Ano Bissexto.')
    else:
        print('Não é um ano bissexto.')
else:
    print('Não é um ano bissexto.')
