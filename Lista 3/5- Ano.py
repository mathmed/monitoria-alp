ano=int(input('Digite o ano: '))
if ano%100==0:
    print('Ano Bissexto.')
elif ano % 4==0:
    if ano%100!=0:
        print('Ano Bissexto.')
    else:
        print('Não é um ano bissexto.')
else:
    print('Não é um ano bissexto.')
