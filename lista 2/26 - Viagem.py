#PROGRAMA DESENVOLVIDO POR @MATHMEDEIROS#
print('Programa para calcular quantidade gasta em uma viagem de acordo com circunstâncias pré estabelecidas.')
print()
pessoas=int(input('Digite a quantidade de pessoas: '))
distancia=float(input('Digite a distância a ser percorrida em KM: '))
combustivel=float(input('Digite o preço do combustível em R$ (por exemplo 3.60): '))
consumo=float(input('Digite a quantidade de Kilômetros que seu automóvel faz a cada litro de combustivel: '))
locacao=float(input('Digite o preço da locação do veículo: '))
a=distancia/consumo
b=a*combustivel
c=(b+locacao)
d=c/pessoas
print()
print('O valor total será R$%5.2f !' % c)
print()
print('Cada pessoa pagará R$%5.2f !' % d)
input()
