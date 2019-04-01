
n1=float(input('Digite a primeira nota: '))
n2=float(input('Digite a segunda nota: '))
n3=float(input('Digite a terceira nota: '))
media=(n1+n2+n3)/3
print('Sua média é %5.2f. ' % media)
if media>=7:
    print('Você está aprovado.')
elif media<7:
    if n1>=5 and n2>=5 and n3>=5:
        print('Você está aprovado.')
    else:
        print('Você irá fazer uma prova para subistituir a pior nota.')
        print()
        n4=float(input('Digite a nota da prova de recuperação:'))
        if n1<n2 and n1<n3:
            media=(n4+n2+n3)/3
            print('Sua média é %5.2f. ' % media)
            if media >=7:
                print('Você está aprovado.')
            elif media <7:
                print('Você está reprovado.')
        elif n2<n1 and n2<n3:
            media=(n1+n4+n3)/3
            print('Sua média é %5.2f. ' % media)
            if media >=7:
                print('Você está aprovado.')
            elif media<7:
                print('Você está reprovado.')
        elif n3<n1 and n3<n2:
            media=(n1+n2+n4)/3
            print('Sua média é %5.2f. ' % media)
            if media >=7:
                print('Você está aprovado.')
            elif media< 7:
                print('Você está reprovado.')
        elif n1==n2 and n1<n3 and n2<n3:
            media=(n4+n2+n3)/3
            print('Sua média é %5.2f. ' % media)
            if media >=7:
                print('Você está aprovado.')
            elif media<7:
                print('Você está reprovado.')
        elif n1==n3 and n1<n2 and n3<n2:
            media=(n4+n2+n3)/3
            print('Sua média é %5.2f. ' % media)
            if media >=7:
                print('Você está aprovado.')
            elif media<7:
                print('Você está reprovado.')
        elif n2==n3 and n2<n1 and n3<n1:
            media=(n1+n4+n3)/3
            print('Sua média é %5.2f. ' % media)
            if media >=7:
                print('Você está aprovado.')
            elif media <7:
                print('Você está reprovado.')
        elif n1==n2 and n1==n3 and n2==n3:
            media=(n1+n2+n4)/3
            print('Sua média é %5.2f. ' % media)
            if media >=7:
                print('Você está aprovado.')
            elif media<7:
                print('Você está reprovado.')
        
        
        

