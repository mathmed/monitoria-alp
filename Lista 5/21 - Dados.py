import random
x=1
while x==1:    
    a=input('Dê enter para continuar. ')
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
    x=int(input('Deseja sortear novamente? Digite 1 para SIM ou 2 para NÃO: '))
    print()
