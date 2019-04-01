# Programa para calcular a nota do aluno no sisu a partir das notas aqui escritas #
# Programa desenvolvido em 21/02/2017 #
# Desenvolvido por Mateus Medeiros #

print('Programa para calcular  a sua nota no SISU! ')
print('Informe suas notas abaixo de acordo com as fornecidas pelo ENEM. ')
print()
notal= float(input('Digite aqui a sua nota na área de Linguagens e Códigos: '))
notam= float(input('Digite aqui a sua nota na área de Matemática: '))
notach= float(input('Digite aqui a sua nota na área de Ciências Humanas: '))
notacn= float(input('Digite aqui a sua nota na área de Ciências da Natureza: '))
notar= float(input('Digite aqui a sua nota na Redação: '))
print()
print('Digite a área que deseja ingressar abaixo, sendo elas: Biomédica, Humanística 1, Humanística 2, Tecnológica 1, Tecnológica 2.')
print()
print('Para Biomédica,     digite 1')
print('Para Humanística 1, digite 2')
print('Para Humanística 2, digite 3')
print('Para Tecnológica 1, digite 4')
print('Para Tecnológica 2, digite 5')
area=input('Digite o número correspondente a sua área: ')
if area =="1":
    somapesobiomedica=1.0+1.0+15+3+1.5
    pesobiomedica=(notal*1.0+notam*1.0+notach*15+notacn*3+notar*1.5) / somapesobiomedica
    print('Sua nota nessa área é:%.2f ' % pesobiomedica)
elif area == "2":
    somapesohumanistica1=2.0+2.0+2.0+1.0+1.5
    pesohumanistica1=(notal*2.0+notam*2.0+notach*2.0+notacn*1.0+notar*1.5) / somapesohumanistica1
    print('Sua nota nessa área é:%.2f ' % pesohumanistica1)
elif area == "3":
    somapesohumanistica2= 2.5+1.0+2.5+1.0+1.5
    pesohumanistica2= (notal*2.5+notam*1.0+notach*2.5+notacn*1.0+notar*1.5) / somapesohumanistica2
    print('Sua nota nessa área é:%.2f ' % pesohumanistica2)
elif area == "4":
    somapesotecnologica1=1.0+2.0+2.0+2.0+1.5
    pesotecnologica1= (notal*1.0+notam*2.0+notach*2.0+notacn*2.0+notar*1.5) / somapesotecnologica1
    print('Sua nota nessa área é:%.2f ' % pesotecnologica1)
elif area == "5":
    somapesotecnologica2= 1.0+3.0+1.0+2.0+1.5
    pesotecnologica2= (notal*1.0+notam*3.0+notach*1.0+notacn*2.0+notar*1.5) / somapesotecnologica2
    print('Sua nota nessa área é:%.2f ' % pesotecnologica2)
else:
    print('Não foi possível identificar a sua área, por favor digite novamente de acordo com o que foi pedido')
print('Para ver a nota em outras áreas, digite novamente o código correspondente a área')
print()
area=input('Digite o número correspondente a sua área: ')
if area =="1":
    somapesobiomedica=1.0+1.0+15+3+1.5
    pesobiomedica=(notal*1.0+notam*1.0+notach*15+notacn*3+notar*1.5) / somapesobiomedica
    print('Sua nota nessa área é:%.2f ' % pesobiomedica)
elif area == "2":
    somapesohumanistica1=2.0+2.0+2.0+1.0+1.5
    pesohumanistica1=(notal*2.0+notam*2.0+notach*2.0+notacn*1.0+notar*1.5) / somapesohumanistica1
    print('Sua nota nessa área é:%.2f ' % pesohumanistica1)
elif area == "3":
    somapesohumanistica2= 2.5+1.0+2.5+1.0+1.5
    pesohumanistica2= (notal*2.5+notam*1.0+notach*2.5+notacn*1.0+notar*1.5) / somapesohumanistica2
    print('Sua nota nessa área é:%.2f ' % pesohumanistica2)
elif area == "4":
    somapesotecnologica1=1.0+2.0+2.0+2.0+1.5
    pesotecnologica1= (notal*1.0+notam*2.0+notach*2.0+notacn*2.0+notar*1.5) / somapesotecnologica1
    print('Sua nota nessa área é:%.2f ' % pesotecnologica1)
elif area == "5":
    somapesotecnologica2= 1.0+3.0+1.0+2.0+1.5
    pesotecnologica2= (notal*1.0+notam*3.0+notach*1.0+notacn*2.0+notar*1.5) / somapesotecnologica2
    print('Sua nota nessa área é:%.2f ' % pesotecnologica2)
else:
    print('Não foi possível identificar a sua área, por favor digite novamente de acordo com o que foi pedido')
print('Para ver a nota em outras áreas, digite novamente o código correspondente a área')
print()
area=input('Digite o número correspondente a sua área: ')
if area =="1":
    somapesobiomedica=1.0+1.0+15+3+1.5
    pesobiomedica=(notal*1.0+notam*1.0+notach*15+notacn*3+notar*1.5) / somapesobiomedica
    print('Sua nota nessa área é:%.2f ' % pesobiomedica)
elif area == "2":
    somapesohumanistica1=2.0+2.0+2.0+1.0+1.5
    pesohumanistica1=(notal*2.0+notam*2.0+notach*2.0+notacn*1.0+notar*1.5) / somapesohumanistica1
    print('Sua nota nessa área é:%.2f ' % pesohumanistica1)
elif area == "3":
    somapesohumanistica2= 2.5+1.0+2.5+1.0+1.5
    pesohumanistica2= (notal*2.5+notam*1.0+notach*2.5+notacn*1.0+notar*1.5) / somapesohumanistica2
    print('Sua nota nessa área é:%.2f ' % pesohumanistica2)
elif area == "4":
    somapesotecnologica1=1.0+2.0+2.0+2.0+1.5
    pesotecnologica1= (notal*1.0+notam*2.0+notach*2.0+notacn*2.0+notar*1.5) / somapesotecnologica1
    print('Sua nota nessa área é:%.2f ' % pesotecnologica1)
elif area == "5":
    somapesotecnologica2= 1.0+3.0+1.0+2.0+1.5
    pesotecnologica2= (notal*1.0+notam*3.0+notach*1.0+notacn*2.0+notar*1.5) / somapesotecnologica2
    print('Sua nota nessa área é:%.2f ' % pesotecnologica2)
else:
    print('Não foi possível identificar a sua área, por favor digite novamente de acordo com o que foi pedido')
print('Para ver a nota em outras áreas, digite novamente o código correspondente a área')
print()
area=input('Digite o número correspondente a sua área: ')
if area =="1":
    somapesobiomedica=1.0+1.0+15+3+1.5
    pesobiomedica=(notal*1.0+notam*1.0+notach*15+notacn*3+notar*1.5) / somapesobiomedica
    print('Sua nota nessa área é:%.2f ' % pesobiomedica)
elif area == "2":
    somapesohumanistica1=2.0+2.0+2.0+1.0+1.5
    pesohumanistica1=(notal*2.0+notam*2.0+notach*2.0+notacn*1.0+notar*1.5) / somapesohumanistica1
    print('Sua nota nessa área é:%.2f ' % pesohumanistica1)
elif area == "3":
    somapesohumanistica2= 2.5+1.0+2.5+1.0+1.5
    pesohumanistica2= (notal*2.5+notam*1.0+notach*2.5+notacn*1.0+notar*1.5) / somapesohumanistica2
    print('Sua nota nessa área é:%.2f ' % pesohumanistica2)
elif area == "4":
    somapesotecnologica1=1.0+2.0+2.0+2.0+1.5
    pesotecnologica1= (notal*1.0+notam*2.0+notach*2.0+notacn*2.0+notar*1.5) / somapesotecnologica1
    print('Sua nota nessa área é:%.2f ' % pesotecnologica1)
elif area == "5":
    somapesotecnologica2= 1.0+3.0+1.0+2.0+1.5
    pesotecnologica2= (notal*1.0+notam*3.0+notach*1.0+notacn*2.0+notar*1.5) / somapesotecnologica2
    print('Sua nota nessa área é:%.2f ' % pesotecnologica2)
else:
    print('Não foi possível identificar a sua área, por favor digite novamente de acordo com o que foi pedido')
print('Para ver a nota em outras áreas, digite novamente o código correspondente a área')
print()
area=input('Digite o número correspondente a sua área: ')
if area =="1":
    somapesobiomedica=1.0+1.0+15+3+1.5
    pesobiomedica=(notal*1.0+notam*1.0+notach*15+notacn*3+notar*1.5) / somapesobiomedica
    print('Sua nota nessa área é:%.2f ' % pesobiomedica)
elif area == "2":
    somapesohumanistica1=2.0+2.0+2.0+1.0+1.5
    pesohumanistica1=(notal*2.0+notam*2.0+notach*2.0+notacn*1.0+notar*1.5) / somapesohumanistica1
    print('Sua nota nessa área é:%.2f ' % pesohumanistica1)
elif area == "3":
    somapesohumanistica2= 2.5+1.0+2.5+1.0+1.5
    pesohumanistica2= (notal*2.5+notam*1.0+notach*2.5+notacn*1.0+notar*1.5) / somapesohumanistica2
    print('Sua nota nessa área é:%.2f ' % pesohumanistica2)
elif area == "4":
    somapesotecnologica1=1.0+2.0+2.0+2.0+1.5
    pesotecnologica1= (notal*1.0+notam*2.0+notach*2.0+notacn*2.0+notar*1.5) / somapesotecnologica1
    print('Sua nota nessa área é:%.2f ' % pesotecnologica1)
elif area == "5":
    somapesotecnologica2= 1.0+3.0+1.0+2.0+1.5
    pesotecnologica2= (notal*1.0+notam*3.0+notach*1.0+notacn*2.0+notar*1.5) / somapesotecnologica2
    print('Sua nota nessa área é:%.2f ' % pesotecnologica2)
else:
    print('Não foi possível identificar a sua área, por favor digite novamente de acordo com o que foi pedido')
input()

