
#PROGRAMA PARA CALCULAR AS RAÍZES DE UMA EQUAÇÃO DE 2° GRAU!#
#DESENVOLVIDO POR @MATHMEDEIROS#
print('Programa para calcular as raízes de uma equação de 2° grau.')
print()
a=float(input('Digite o coeficiente A: '))
b=float(input('Digite o coeficiente B: '))
c=float(input('Digite o coeficiente C: '))
delta=(b**2)-(4*a*c)
if delta <= 0:
    print('Essa equação não possui raízes reais.')
else:
    raiz1=-b+delta**(1/2)
    raiza=raiz1/ (2*a)
    raiz2=-b-delta**(1/2)
    raiza2=raiz2/ (2*a)
    print()
    print('A primeira raíz é:%5.2f' % raiza)
    print('A segunda raiz é:%5.2f' % raiza2)
input()      
