print('Programa para decifrar formas geométricas. ')
print()
nome=input('Qual seu nome jogador: ')
x=0
print( 'Responda as questões utilizando 1,2, 3 ou 4 para uma alternativa.')
print()
print('Qual é a figura abaixo: ')
print('      * * * *         ')
print('    *        *        ')
print('   *          *       ')
print('   *          *       ')
print('    *        *        ')
print('      * * * *         ')
print()
print('1 - Quadrado . ')
print('2 - Triângulo . ')
print('3 - Círculo . ')
print('4 - Losango . ')
q1=int(input())
if q1 ==3:
    x=x+0.625
    print('Acertou.')
    print()
    print('Digite a área da circuferência, sendo seu diâmetro 2,4 metros. ')
    print('1 - 5,34 Metros')
    print('2 - 2 Metros')
    print('3 - 4,52 Metros')
    print('4 - 6,15 Metros')
    v1=int(input())
    if v1==4:
        x=x+0.625
        print('Você acertou.')
    else:
        print('Você errou.')       
else:
    print('Errou, a resposta certa seria Círculo.')
    print('Vou te dar mais uma chance, o diâmetro do círculo é 2,4 metros, qual sua área?')
    print()
    print('1 - 5,34 Metros')
    print('2 - 2 Metros')
    print('3 - 4,52 Metros')
    print('4 - 6,15 Metros')
    v1=int(input())
    if v1==4:
        x=x+0.625
        print('Você acertou.')
    else:
        print('Você errou.')
    
print()
print('Qual é a figura abaixo: ')
print('               ')
print('       *        ')
print('      * *       ')
print('     *   *      ')
print('    *     *     ')
print('   *********    ')
print()
print('1 - Quadrado . ')
print('2 - Triângulo . ')
print('3 - Retângulo . ')
print('4 - Trapézio . ')
q2=int(input())
if q2 ==2:
    x=x+0.625
    print('Acertou.')
    print()
    print('Qual a área do triângulo sendo sua base 1,2m e altura 2,5m? ')
    print()
    print('1 - 2,34 Metros')
    print('2 - 1,50 Metros')
    print('3 - 1,52 Metros')
    print('4 - 1,15 Metros')
    v2=int(input())
    if v2==2:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')
    
else:
    print('Errou, a resposta certa seria Triângulo.')
    print('Vou dar outra chance, Qual a área do triângulo sendo sua base 1,2m e altura 2,5m? ')
    print()
    print('1 - 2,34 Metros')
    print('2 - 1,5 Metros')
    print('3 - 1,52 Metros')
    print('4 - 1,15 Metros')
    v2=int(input())
    if v2==2:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')
    
print()
print('Qual é a figura abaixo: ')
print('               ')
print('   *********            ')
print('   *       *      ')
print('   *       *      ')
print('   *       *    ')
print('   *********    ')
print()
print('1 - Quadrado . ')
print('2 - Círculo . ')
print('3 - Retângulo . ')
print('4 - Trapézio . ')
q3=int(input())
if q3 ==1:
    x=x+0.625
    print('Acertou.')
    print('Qual a área do quadrado sendo um de seus lados 4m? ')
    print()
    print('1 - 24 Metros')
    print('2 - 14 Metros')
    print('3 - 20 Metros')
    print('4 - 16 Metros')
    v3=int(input())
    if v3==4:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')
    
else:
    print('Errou, a resposta certa seria Quadrado..')
    print('Vou te dar mais uma chance, Qual a área do quadrado sendo um de seus lados 4m? ')
    print()
    print('1 - 24 Metros')
    print('2 - 14 Metros')
    print('3 - 20 Metros')
    print('4 - 16 Metros')
    v3=int(input())
    if v3==4:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')
    
print()
print('Qual é a figura abaixo: ')
print('               ')
print('       *******    ')
print('      *       *       ')
print('     *         *      ')
print('    *           *     ')
print('   ***************    ')
print()
print('1 - Quadrado . ')
print('2 - Retângulo . ')
print('3 - Círculo . ')
print('4 - Trapézio . ')
q4=int(input())
if q4 ==4:
    x=x+0.625
    print('Acertou.')
    print('Qual a área do trapézio sendo sua base menor 2.2m, base maior 3.4m e altura 4.6m? ')
    print()
    print('1 - 12,88 Metros')
    print('2 - 12,48 Metros')
    print('3 - 14,88 Metros')
    print('4 - 14,48 Metros')
    v4=int(input())
    if v4==1:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')
    
else:
    print('Errou, a resposta certa seria Trapézio.')
    print('Vou te dar outra chance, Qual a área do trapézio sendo sua base menor 2,2m, base maior 3,4m e altura 4,6m? ')
    print()
    print('1 - 12,88 Metros')
    print('2 - 12,48 Metros')
    print('3 - 14,88 Metros')
    print('4 - 14,48 Metros')
    v4=int(input())
    if v4==1:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')
print()
print('Qual é a figura abaixo: ')
print('               ')
print('               ')
print('   ************       ')
print('   *          *' )
print('   *          * ' )
print('   ************    ')
print()
print('1 - Quadrado . ')
print('2 - Triângulo . ')
print('3 - Retângulo . ')
print('4 - Paralelograma . ')
q5=int(input())
if q5 ==3:
    x=x+0.625
    print('Acertou.')
    print('Qual a área do triângulo sendo sua base 6,5m e sua altura 3,4m? ')
    print()
    print('1 - 23,7 Metros')
    print('2 - 22,1 Metros')
    print('3 - 21,8 Metros')
    print('4 - 22,2 Metros')
    v5=int(input())
    if v5==2:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')
else:
    print('Errou, a resposta certa seria Retângulo.')
    print('Vou te dar outra chance, Qual a área do triângulo sendo sua base 6,5m e sua altura 3,4m? ')
    print()
    print('1 - 23,7 Metros')
    print('2 - 22,1 Metros')
    print('3 - 21,8 Metros')
    print('4 - 22,2 Metros')
    v5=int(input())
    if v5==2:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')
    
print()
print()
print('Qual é a figura abaixo: ')
print('               ')
print('          *          ')
print('        *   *         ')
print('       *     *     ' )
print('        *   *      ' )
print('          *               ')
print()
print('1 - Losango . ')
print('2 - Triângulo . ')
print('3 - Retângulo . ')
print('4 - Trapézio . ')
q6=int(input())
if q6 ==1:
    x=x+0.625
    print('Acertou.')
    print('Qual a área do losango sendo dia diagonal maior 5m e sua sua diagonal menor 2,5m? ')
    print()
    print('1 - 6,35 Metros')
    print('2 - 5,25 Metros')
    print('3 - 6,25 Metros')
    print('4 - 7,35 Metros')
    v6=int(input())
    if v6==3:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')       
else:
    print('Errou, a resposta certa seria Losango.')
    print('Vou te dar outra chance, Qual a área do losango sendo dia diagonal maior 5m e sua sua diagonal menor 2,5m? ')
    print()
    print('1 - 6,35 Metros')
    print('2 - 5,25 Metros')
    print('3 - 6,25 Metros')
    print('4 - 7,35 Metros')
    v6=int(input())
    if v6==3:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')
print()
print('Qual é a figura abaixo: ')
print('               ')
print('               ')
print('       ************       ')
print('      *          *' )
print('     *          * ' )
print('    ************    ')
print()
print('1 - Quadrado . ')
print('2 - Paralelograma . ')
print('3 - Retângulo . ')
print('4 - Trapézio . ')
q7=int(input())
if q7 ==2:
    x=x+0.625
    print('Acertou.')
    print('Qual a área do paralelogramo sendo sua base 3,3m e altura 6,5m? ')
    print()
    print('1 - 21,45 Metros')
    print('2 - 22,56 Metros')
    print('3 - 20,45 Metros')
    print('4 - 19,50 Metros')
    v7=int(input())
    if v7==1:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')       
else:
    print('Errou, a resposta certa seria Paralelograma.')
    print()
    print('Vou te dar outra chance, Qual a área do paralelogramo sendo sua base 3,3m e altura 6,5m? ')
    print()
    print('1 - 21,45 Metros')
    print('2 - 22,56 Metros')
    print('3 - 20,45 Metros')
    print('4 - 19,50 Metros')
    v7=int(input())
    if v7==1:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')
        
print('Qual é a figura abaixo: ')
print('             *       ')
print('           *   *           ')
print('          *     *         ')
print('         *       *               ' )
print('        *         *   '      )
print('        *         *              ')
print('         * * * * *                 ')
print('1 - Quadrado . ')
print('2 - Triângulo . ')
print('3 - Cone . ')
print('4 - Trapézio . ')
q8=int(input())
if q8 ==3:
    x=x+0.625
    print('Acertou.')
    print('Quais são, respectivamente as áreas laterais e total do cone, sendo seu raio 30cm e geratriz 1,2m? ')
    print()
    print('1 - 1,13m e 1,41m')
    print('2 - 1,43m e 1,23m ')
    print('3 - 2,15m e 3,43m ')
    print('4 - 1,22m e 1,67m')
    v8=int(input())
    if v8==1:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')       
else:
    print('Errou, a resposta certa seria Cone.')
    print('Vou te dar otura chance.')
    print('Quais são, respectivamente as áreas laterais e total do cone, sendo seu raio 30cm e geratriz 1,2m? ')
    print()
    print('1 - 1,13m e 1,41m')
    print('2 - 1,43m e 1,23m ')
    print('3 - 2,15m e 3,43m ')
    print('4 - 1,22m e 1,67m')
    v8=int(input())
    if v8==1:
        print('Acertou.')
        x=x+0.625
    else:
        print('Você errou.')       
    
print('%s sua nota final foi %5.2f. ! ' % (nome,x))
