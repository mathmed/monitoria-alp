print('Informe o primeiro horário.')
hora1=input('Formato : hh:mm:ss: ')
h1=int(hora
m1=int
s1=int

print('Informe o segundo horário: ')
h2=int(input('Valor das horas 2: '))
m2=int(input('Valor das minutos 2: '))
s2=int(input('Valor das segundos 2: '))

difHor= h2-h1
difMin= m2- m1
difSeg= s2-s1

qdeSeg= difSeg+difMin*60+difHor*3600
print('Os segundos decorridos nesse períodos foi %d seg. ' % qdeSeg)
