#PROGRAMA DESENVOLVIDO POR @MATHMEDEIROS#
print('Programa para calcular custo de energia.')
custo=float(input('Digite o custo de energia elétrica no seu município em R$ (exemplo, 0.25):'))
consumo=float(input('Digite o consumo do seu aparelo em KW/h: '))
tempo=int(input('Digite quanto tempo ele fica ligado por dia: '))
print()
print('Vamos calcular.')
print()
diario=custo*consumo*tempo
print('O Custo diário de seu aparelho é R$%5.2f. ' % diario)
print()
mensal=diario*30
print('O Custo mensal em um mês de 30 dias é R$%5.2f . ' % mensal)

            
