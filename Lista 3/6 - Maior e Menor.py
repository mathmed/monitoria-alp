n1=int(input('Digite o primeiro número inteiro: '))
n2=int(input('Digite o segundo numero inteiro: '))
n3=int(input('Digite o terceiro número inteiro: '))
def maior ():
    if n1 > n2 and n1 > n3:
        print('%d é o maior número. ' % n1)
    elif n2 > n1 and n2 > n3:
        print('%d é o maior número. ' % n2)
    elif n3> n1 and n3>n2:
        print('%d é o maior número. ' % n3)
    #números iguais#
    elif n1==n2 and n1>n3 and n2 > n3:
        print('%d, %d são os maiores números. ' % (n1,n2))
    elif n1==n3 and n1>n2 and n3>n2:
        print('%d, %d são os maiores números. ' % (n1,n3))
    elif n2==n3 and n2>n1 and n3>n1:
        print('%d, %d são os maiores números. ' % (n2,n3))
    elif n1== n2 and n1 ==n3 and n2==n3:
        print('Todos são iguais.')
def menor():
    if n1<n2 and n1 <n3:
        print('%d é o menor número. ' % n1)
    elif n2<n1 and n2<n3:
        print('%d é o menor número. ' % n2)
    elif n3<n1 and n3<n2:
        print('%d é o menor número. ' % n3)
        #números iguais#
    elif n1==n2 and n1<n3 and n2<n3:
        print('%d7 %d são os menores números. ' % (n1,n2))
    elif n1==n3 and n1<n2 and n3<n2:
        print('%d, %d são os menores números. ' % (n1,n3))
    elif n2==n3 and n2<n1 and n3<n1:
        print('%d, %d são os menores números. ' % (n2,n3))
    elif n1==n2 and n1==n3 and n2==n3:
        print('Todos são iguais.')
maior()
menor()
        
    
        
        
