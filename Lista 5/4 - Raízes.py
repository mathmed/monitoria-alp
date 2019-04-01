n=int(input('Digite um número real para extrair a raiz: '))
if n>=0:
    import  math
    a=math.sqrt(n)
    print('A raiz do seu número é %d. ' %a)
else:
    print('Esse número não possui raíz real.')
