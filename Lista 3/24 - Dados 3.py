import random
x=1
while x==1:
    print('Programa de dados.')
    print()
    print('Você precisa jogar dois dados e a soma ser 7 ou 11 para vencer.')
    nome=input('Digite o seu nome:')
    print('Vamos ao sorteio.')
    sort=random.randint(1,6)
    if sort==1:
        print('#########')
        print('#       #')
        print('#   *   #')
        print('#       #')
        print('#########')
    if sort==2:
        print('#########')
        print('# *     #')
        print('#       #')
        print('#     * #')
        print('#########')
    if sort ==3:
        print('#########')
        print('# *     #')
        print('#   *   #')
        print('#     * #')
        print('#########')
    if sort ==4:
        print('#########')
        print('# *   * #')
        print('#       #')
        print('# *   * #')
        print('#########')
    if sort==5:
        print('#########')
        print('# *   * #')
        print('#   *   #')
        print('# *   * #')
        print('#########')
    if sort==6:
        print('#########')
        print('# *   * #')
        print('# *   * #')
        print('# *   * #')
        print('#########')
    print()
    print()
    sort2=random.randint(1,6)
    if sort2==1:
        print('#########')
        print('#       #')
        print('#   *   #')
        print('#       #')
        print('#########')
    if sort2==2:
        print('#########')
        print('# *     #')
        print('#       #')
        print('#     * #')
        print('#########')
    if sort2 ==3:
        print('#########')
        print('# *     #')
        print('#   *   #')
        print('#     * #')
        print('#########')
    if sort2 ==4:
        print('#########')
        print('# *   * #')
        print('#       #')
        print('# *   * #')
        print('#########')
    if sort2==5:
        print('#########')
        print('# *   * #')
        print('#   *   #')
        print('# *   * #')
        print('#########')
    if sort2==6:
        print('#########')
        print('# *   * #')
        print('# *   * #')
        print('# *   * #')
        print('#########')
    print()
    print()
    lol=sort+sort2
    if lol == 7 or lol ==11:
        print('Você venceu.' )
    else:
        print('Você perdeu.')
print()
x=int(input('Digite 1 para jogar novamente ou 2 para sair:' ))        
