dia=int(input('Digite o dia: '))
mes=int(input('Digite o número correspondente ao mês: '))
if mes ==1 or mes == 2 or mes == 3 or mes == 4 or mes==5 or mes==6:
    if mes ==1:
        print('Verão.')
    elif mes ==2:
        print('Verão.')
    elif mes==3:
        if dia>=20:
            print('Outono.')
        elif dia <20:
            print('Verão.')
    elif mes==4:
        print('Outono')
    elif mes==5:
        print('Outono')
    elif mes==6:
        if dia<21:
            print('Outono')
        elif dia >=21:
            print('Inverno.')
elif mes == 7 or mes ==8 or mes ==9 or mes ==10 or mes==11 or mes==12:
    if mes==7:
        print('Invervo')
    elif mes==8:
        print('Inverno')
    elif mes==9:
        if dia<22:
            print('Inverno.')
        elif dia >=22:
            print('Primavera.')
    elif mes ==10:
        print('Primavera.')
    elif mes==11:
        print('Primavera.')
    elif mes==12:
        if dia <21:
            print('Primavera')
        elif dia>=21:
            print('verão.')
