##########################################################################
#### PROGRAMA PARA CALCULAR NÚMERO DE DIAGONAIS DE UM POLÍGONO REGULAR ###
###            DESENVOLVIDO POR @MATEUSMEDEIROS                        ###
###                   23/02/2017                                       ###
##########################################################################

print('Desenvolvido por Mateus Medeiros!')
print()
print('Programa para calcular número de diagonais de um polígono regular!')
print()
print('Polígonos suportados: Triângulo, Quadrilátero, Pentágono, Hexágono, Heptágono, Octógono, Eneágono, Decágono, Hendecágono, Dodecágono.')
poligono=input('Digite aqui o polígono que deseja saber o número de diagonais: ')
a=poligono
if a == 'Triângulo' or a == 'triângulo' or a== 'Triangulo' or a== 'triangulo':
    diagonais= 3*(3-3)/2
    print('O triângulo possui %d Diagonais! ' % diagonais)
elif a== 'Quadrilátero' or a== 'quadrilátero' or a== 'Quadrilatero' or a== 'quadrilatero':
    diagonais=4*(4-3)/2
    print('O Quadrado possui %d Diagonais! ' % diagonais)
elif a== 'Pentágono' or a== 'pentágono' or a=='Pentagono' or a== 'pentagono':
    diagonais= 5*(5-3)/2
    print('O Pentágono possui %d Diagonais! ' % diagonais)
elif a== 'Hexágono' or a == 'hexágono' or a== 'Hexagono' or a== 'hexagono':
    diagonais= 6*(6-3)/2
    print('O Hexágono possui %d Diagonais! ' % diagonais)
elif a== 'Heptágono' or a== 'heptágono' or a== 'Heptagono' or a== 'heptagono':
    diagonais= 7*(7-3)/2
    print('O Heptágono possui %d Diagonais! ' % diagonais)
elif a== 'Octógono' or a=='octógono' or a== 'Octogono' or a == 'octogono':
    diagonais= 8*(8-3)/2
    print('O Octógono possui %d Diagonais! ' % diagonais)
elif a== 'Eneágono' or a== 'eneágono' or a== 'Eneagono' or a== 'eneagono':
    diagonais= 9*(9-3)/2
    print('O Eneágono possui %d Diagonais! ' % diagonais)
elif a== 'Decágono' or a== 'decágono' or a== 'Decagono' or a== 'decagono':
    diagonais= 10*(10-3)/2
    print('O Decágono possui %d Diagonais! ' % diagonais)
elif a== 'Hendecágono' or a== 'hendecágono' or a== 'Hendecagono' or a== 'hendecagono':
    diagonais= 11*(11-3)/2
    print('O Hendecágono possui %d Diagonais! ' % diagonais)
elif a== 'Dodecágono' or a== 'dodecágono' or a== 'Dodecagono' or a== 'dodecagono':
    diagonais= 12*(12-3)/2
    print('O Dodecágono possui %d Diagonais! ' % diagonais)
else:
    print('Polígono não encontrado, tem certeza que digitou o nome cero?!')
input()
