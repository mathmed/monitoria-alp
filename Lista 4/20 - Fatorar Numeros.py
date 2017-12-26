#PROGRAMA DESMENTRAR NUMERO, SOMAR E MULTIPLICAR.#
for i in range (1000,10000):
    prim=(i//100)
    seg=(i%100)
    if(prim+seg)*(prim+seg)==i:
        print(i)

    
