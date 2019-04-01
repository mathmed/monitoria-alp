dados={}
lista=[]
x=1
qnt=len(lista)
if qnt <=0:
    qnt=int(input('Quantos cadastros deseja fazer: '))
    for i in range(qnt):
        lista.append([])
        nome=input('Digite o nome da pessoa %d: ' %(i+1))
        peso=float(input('Digite o peso: '))
        idade=int(input('Digite a idade: '))
        altura=float(input('Digite a altura: '))
        sexo=input('Digite o sexo (M) ou (F): ')
        lista[i]+=[nome,peso,idade,altura,sexo]
        dados[nome]=lista[i]
        print()
    print(lista)
       
while x==1:
    print('O que deseja: ')
    print('1- Cadastro dos dados biométricos de novos usuários.')
    print('2- Exibição dos dados dos usuários organizados na tela.')
    print('3- Cálculo do peso médio do grupo de usuários.')
    print('4- Cálculo da idade média do grupo de usuários.')
    print('5- Cálculo da altura média do grupo de usuários.')
    print('6- Contagem do número de usuários de cada sexo.')
    print('7- Identificação do nome do usuário mais magro e do mais gordo do grupo.')
    print('8- Identificação do nome do usuário mais alto e do mais baixo do grupo.')
    print('9- Identificação do nome do usuário mais novo e do mais velho do grupo.')
    print()
    print('Digite 0 (zero) para sair.')
    print()
    escolha=int(input('Digite sua escolha: '))
    print()
    if escolha ==0:
        break
    elif escolha ==1:
        qnt=int(input('Quantos cadastros deseja fazer: '))
        for i in range(qnt):
            lista.append([])
            nome=input('Digite o nome da pessoa %d: ' %(i+1))
            peso=float(input('Digite o peso: '))
            idade=int(input('Digite a idade: '))
            altura=float(input('Digite a altura: '))
            sexo=input('Digite o sexo (M) ou (F): ')
            lista[i]+=(nome,peso,idade,altura,sexo)
            dados[nome]=lista[i]
            print()
        print()
        x=int(input('Digite 1 (Um) para voltar para o menu. '))
    elif escolha==2:
        yy=input('Digite o nome da pessoa que deseja vizualizar: ')
        for i in dados:
            if yy.lower()==i.lower():
                print('Nome:' ,dados[i][0],'\nPeso:',dados[i][1],'\nIdade:',dados[i][2],'\nAltura:',dados[i][3],'\nSexo:',dados[i][4])
                print()
            elif yy not in dados:
                print('Não existe nenhum usuário cadastrado com esse nome, tende novamente.')
        x=int(input('Digite 1 (Um) para voltar para o menu. '))
    elif escolha ==3:
        soma=0
        cont=0
        for i in dados:
            soma+=dados[i][1]
            cont+=1
        media=soma/cont
        print('A média de peso dos usuários cadastrados é: %.2f Kilos.' % media)
        print()
        x=int(input('Digite 1 (Um) para voltar para o menu. '))
    elif escolha==4:
        soma=0
        cont=0
        for i in dados:
            soma+=dados[i][2]
            cont+=1
        media=soma/cont
        print('A média de idade dos usuários cadastrados é: %.2f anoss.' % media)
        print()
        x=int(input('Digite 1 (Um) para voltar para o menu. '))
    elif escolha==5:
        soma=0
        cont=0
        for i in dados:
            soma+=dados[i][3]
            cont+=1
        media=soma/cont
        print('A média de altura dos usuários cadastrados é: %.2f metro(s).' % media)
        print()
        x=int(input('Digite 1 (Um) para voltar para o menu. '))
    elif escolha==6:
        contF=0
        contM=0
        for i in dados:
            if dados[i][4]=='m' or dados[i][4]=='M':
                contM+=1
            else:
                contF+=1
        print('Existem %d pessoas do sexo masculino.\nExistem %d pessoas do sexo feminimo.' % (contM,contF))
        print()
        x=int(input('Digite 1 (Um) para voltar para o menu. '))
    elif escolha==7:
        maior=0
        for i in dados:
            if dados[i][1]>maior:
                maior=dados[i][1]
                name=dados[i][0]
        menor =100000000000
        for j in lista:
            if dados[i][1]<menor:
                menor=dados[i][1]
                name1=dados[i][0]
        print('A pessoa com maior peso é %s, que pesa %5.2F kilos. ' % (name,maior))
        print('A pessoa com menor peso é %s, que pesa %5.2F kilos.' % (name1,menor))
        print()
        x=int(input('Digite 1 (Um) para voltar para o menu. '))
    elif escolha==8:
        maior=0
        for i in dados:
            if dados[i][3]>maior:
                maior=dados[i][3]
                name=dados[i][0]
        menor =100000000000
        for j in lista:
            if dados[j][3]<menor:
                menor=dados[j][3]
                name1=dados[j][0]
        print('A pessoa mais alta  é %s, com %5.2f metros de altura. ' % (name,maior))
        print('A pessoa mais baixa  é %s, com %5.2f metros de altura.' % (name1,menor))
        print()
        x=int(input('Digite 1 (Um) para voltar para o menu. '))
        print()
        
    elif escolha==9:
            maior=0
            for i in dados:
                if dados[i][2]>maior:
                    maior=dados[i][2]
                    name=dados[i][0]
            menor =100000000000
            for j in lista:
                if dados[i][2]<menor:
                    menor=dados[i][2]
                    name1=dados[i][0]
            print('A pessoa mais velha é %d, com %d anos. ' % (name,maior))
            print('A pessoa mais nova é %d, com %d anos..' % (name1,menor))
            print()
            x=int(input('Digite 1 (Um) para voltar para o menu. '))
            print()

                    
                
                
                    
                
            

