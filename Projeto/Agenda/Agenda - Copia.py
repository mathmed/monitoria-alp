
#PROGRAMA AGENDA.
def cadastro():
    qnt=int(input('Quantos cadastros deseja fazer: '))
    for i in range(qnt):
        aux.append([])
        fone_contato=input('Digite o número de telefone do contato %s: ' % (i+1))
        nome_contato=input('Digite o nome do contato %s : ' % (i+1))
        email_contato=input('Digite o E-mail do contato %s : ' % (i+1))
        estado_contato=input('Digite o estado do contato %s: ' % (i+1))
        cidade_contato=input('Digite a cidade do contato %s:' % (i+1))
        nasc_contato=input('Digite a data de nascimento do contato no formato dd/mm/aaaa: %s ' % (i+1))
        aux[i]=[fone_contato,nome_contato,email_contato,estado_contato,cidade_contato,nasc_contato]
        dados[fone_contato]=aux[i]
        print()
        
def menu():
    print()
    print('Menu opções.')
    print()
    print('Digite o número correspondente a opção desejada.')
    print('1 - Cadastrar novo contato.')
    print('2 - Exibir dados de contato.')
    print('3 - Alterar dados de um contato.')
    print('4 - Deletar contato.')
    print('5 - Busca avançada.')
    print('0 - Sair.')
    escolha=int(input('Faça sua escolha: '))
    return escolha

def exibir():
    num=input('Digite o número do contato: ')
    print()
    if num in dados:
        print('Telefone:' ,dados[num][0],'\nNome:',dados[num][1],'\nEmail:',dados[num][2],'\nEstado:',dados[num][3],'\nCidade:',dados[num][4], '\nData Nasc: ', dados[num][5])
    else:
        print('Não existe esse número cadastrado')
def alterar(dados):
    num=input('Digite o número do contato: ')
    print()
    if num in dados:
        print('Selecione a opção que deseja alterar: ')
        print('1 - Telefone')
        print('2 - Nome ')
        print('3 - E-mail')
        print('4 - Estado')
        print('5 - Cidade')
        x=int(input())
        if x ==1:
                novo_tel=input('Digite o novo telefone: ')
                dados[num]=novo_tel
                dados[num][0]=novo_tel
        elif x == 2: 
                novo_nome=input('Digite o novo nome: ')
                dados[num][1]=novo_nome
        elif x ==3:
                novo_email=input('Digite o novo email: ')
                dados[num][2]=novo_email
        elif x ==4:
                novo_estado=input('Digite o novo estado: ')
                dados[num][3]=novo_estado
        elif escolhax ==5:
                novo_cidade=input('Digite a nova cidade: ')
                dados=num[4]=novo_cidade
        else:
            print('Você não escolheu uma opção válida.')
    else:
        print('Você não tem esse número cadastrado.')
        
def deletar(dados):
    num=input('Digite o número do contato que deseja deletar.')
    if num in dados:
        del dados[num]
        print('Cadastro deletado.')
    else:
        print('Você não tem esse número cadastrado.')
def busca(dados):
    print('Selecione o método de busca avançada.')
    print('1 - Mês. ')
    print('2 - Cidade.')
    print('3 - Estado. ')
    a=int(input())
    if a ==1:
        cont=0
        mes=int(input('Digite o mês: '))
        for i in dados:
            y=(dados[i][5]).split('/')
            y1=int(y[1])
            if y1 == mes:
                print('Usuário desse mês: ')
                print('Telefone:' ,dados[i][0],'\nNome:',dados[i][1],'\nEmail:',dados[i][2],'\nEstado:',dados[i][3],'\nCidade:',dados[i][4], '\nData Nasc: ', dados[i][5])
                cont+=1
        if cont == 0:
            print('Não existe nenhum contato desse mês.')

    elif a == 2:
        city=input('Digite a cidade da busca:')
        cont=0
        for i in dados:
            if (dados[i][4].lower())== (city.lower()):
                print('Contatos dessa cidade:')
                print('Telefone:' ,dados[i][0],'\nNome:',dados[i][1],'\nEmail:',dados[i][2],'\nEstado:',dados[i][3],'\nCidade:',dados[i][4], '\nData Nasc: ', dados[i][5])
                cont+=1
        if cont == 0:
            print('Não existe nenhum contato dessa cidade.')
    elif a ==3:
        est=input('Digite o estado da busca: ')
        cont=0
        for i in dados:
            if (dados[i][3].lower()) == (est.lower()):
                print('Contatos desse estado: ')
                print('Telefone:' ,dados[i][0],'\nNome:',dados[i][1],'\nEmail:',dados[i][2],'\nEstado:',dados[i][3],'\nCidade:',dados[i][4], '\nData Nasc: ', dados[i][5])
                cont+=1

        if cont == 0:
            print('Não existe nenhum contato desse estado.')
    else:
        print('VocÊ não digitou uma opção válida.')
    
nome_usuario=input('Digite o seu nome: ')
print()
print('Agenda pessoal de %s. ' % (nome_usuario))
aux=[]
dados={}
print('Você não possui nenhum contato ainda, faça o primeiro:')
cadastro()

while True:
    opçao=menu()
    if opçao==0:
        break
    elif opçao==1:
        cadastro()
    elif opçao==2:
        exibir()
    elif opçao==3 :
        alterar(dados)
    elif opçao==4:
        deletar(dados)
    elif opçao==5:
        busca(dados)
    else:
        print('Você digitou uma opção inválida.')
    
      













    
