#PROGRAMA DESENVOLVIDO POR @MATHMEDEIROS#
#PROGRAMA PARA CALCULAR A TINTA NECESSÁRIA PARA PINTAR UM CILINDRO.#
import math
print('Programa desenvolvido por @MathMedeiros para calcular a tinta necessária para pintar um Tonél.')
print()
altura=float(input('Digite aqui a altura do tonél em metros (por exemplo 1.40): '))
raio=float(input('Digite aqui o raio do tonél em metros (por exemplo 0.5): '))
qntd=int(input('Quantos tonéis você deseja pintar: '))
tinta=float(input('Digite o preço da unidade da lata de tinta: '))
print('Vamos calcular!')
print()
area=2*3.14*raio*(altura+raio)
total=area*qntd
print('A área de seu(s) Tonél(is) é:%5.2f metros quadrados ' % total)
print()
print('Uma lata de tinta pinta aproximadamente 10,24m²')
print()
x=total/10.24
if x < 1:
    print('Você precisará apenas de uma lata de tinta.')
elif x>=1:
    print('Você precisará de %5.2f latas de tinta!' % x)
print()
print('Vamos calcular quanto você irá gastar!')
c=math.ceil(x)
valor= c*tinta
print('Arredondando para %d latas de tinta. ' % c)
print('Você gastará R$%5.2f ! ' % valor)
input()
