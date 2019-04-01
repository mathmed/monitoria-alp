print('A primeira deta deve ser antes da segunda daa.')
dia1=int(input('Digite o primeiro dia: '))
mes1=int(input('Digite o primeiro mês: '))
ano1=int(input('Digite o primeiro ano: '))
dia2=int(input('Digite o segundo dia: '))
mes2=int(input('Digite o segundo mês: '))
ano2=int(input('Digite o segundo ano: '))

difAno = ano2-ano1
difMes=mes2-mes1
difDia= dia2-dia1

diftotal=(difAno*365.2)+(difMes*30.5)+(difDia)
print('Nesse período se passaram %d dias! ' % diftotal)
print()

