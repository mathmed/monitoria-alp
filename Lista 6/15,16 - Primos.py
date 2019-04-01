import math #PARA UTILIZAR RAIZ QUADRADA
def isPrime(num):
    if num<2:
        return False # se for menor 
    i=2                               
    for i in range(2,int(math.sqrt(num)+1)): 
        if (num % i ==0):
            return False
    return True
def primo():
    a=int(input('Digite o primeiro número a partir dele veremos os primos, PS: (Maior que 2):'))
    b=int(input('Digite o último numero: '))
    for i in range(a,b):
        if isPrime(i):
            print(i)
primo()
            
  

