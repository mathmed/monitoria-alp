#TEMPERATURAS PYTHON#
lista_temp=[]
hora=00
for i in range (24):
    temp=int(input('Digite a temperatura em celsius ás %d horas: ' % hora))
    lista_temp.append(temp)
    hora+=1
soma=sum(lista_temp)
print('A média de temperatura nesse dia foi de %d º . ' % (soma/24))
media=soma/24
vezes=[]
for x in (lista_temp):
    if x > media:
        vezes.append(x)
a=len(vezes)
print('A temperatura ficou acima da média %d vezes. ' % a)
        
