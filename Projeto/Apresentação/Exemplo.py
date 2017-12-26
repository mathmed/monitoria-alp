#INICIAMOS IMPORTANDO TODOS OS MÉTODOS DO TKINTER (*), E OUTROS QUE IREMOS USAR
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.messagebox import askquestion
import random
dados={}
class principal (object): #Classe utilizada para interligar todas as janelas durante o programa.
    def __init__(self,event):
        self.font1 = ('Times New Roman', '20', 'bold')# Fontes utilizadas no programa
        self.font2 = ('Times New Roman', '12', 'bold')
        #
        frame=Frame(inicial,bg='dark violet')   #Frame ou container, ''sub-janela'' invisivel onde será inserido os dados na tela.
        frame.grid()           #Método de empacotamento
        #
        titulo=Label(frame,text='Programa Alma Gêmea ♥', bg = 'dark violet',fg='black', font = self.font1) #Label, pode ser comparado à um print!!
        titulo.grid(row=0, column =1)
        #
        subtitulo=Label(frame,text='Tela de Login', bg = 'dark violet',fg='white', font = self.font1)
        subtitulo.grid(row =1 , column = 1)
        #
        login=Label(frame,text='Login:', bg = 'dark violet',fg='white', font = self.font2)
        login.grid(row=2,column =0)
        self.loginEntrada=Entry(frame)           #Método de entrada! Tudo e recebido no formato string, como um input!
        self.loginEntrada.grid(row=2,column =1)
        #
        senha=Label(frame,text='Senha:', bg = 'dark violet',fg='white', font = self.font2)
        senha.grid(row=3,column =0)
        self.senhaEntrada=Entry(frame,show='*')
        self.senhaEntrada.grid(row=3,column =1)
        #
        botaoEntrar=Button(frame,text = 'Entrar', bg = 'green', fg = 'white', font = self.font2, width= 8) #Criando um botão
        botaoEntrar.bind('<Button-1>', self.validar_acesso)
        botaoEntrar.grid(row=4, column = 1)    
        botaoCriarConta=Button(frame,text = 'Criar conta', bg = 'green', fg = 'white', font = self.font2, width = 8)
        botaoCriarConta.bind('<Button-1>', self.cadastro)
        botaoCriarConta.grid(row=5, column = 1,pady=5)
        
    def cadastro(self,event): # TELA DE CADASTRO
        cadastro=Tk()
        frame=Frame(cadastro,bg='tan1')
        frame.grid()
        login=Label(frame,text='Login:', bg = 'tan1',fg='black', font = self.font2)
        login.grid(row=0,column =0)
        self.loginEntrada1=Entry(frame)
        self.loginEntrada1.grid(row=0,column =1)
        #
        senha=Label(frame,text='Senha:', bg = 'tan1',fg='black', font = self.font2)
        senha.grid(row=1,column =0)
        self.senhaEntrada1=Entry(frame,show='*')
        self.senhaEntrada1.grid(row=1,column =1)
        #
        nome=Label(frame,text='Nome:', bg = 'tan1',fg='black', font = self.font2)
        nome.grid(row=2,column =0)
        self.nomeEntrada=Entry(frame)
        self.nomeEntrada.grid(row=2,column =1)
        #
        genero=Label(frame,text='Gênero:', bg = 'tan1',fg='black', font = self.font2)
        genero.grid(row=3,column=0)
        self.generoEntrada=Spinbox(frame,value=('Masculino','Feminino'), state='readonly') #MÉTODO SPINBOX, UTILIZADO PARA LIMITAR AS ESCOLHAS
        self.generoEntrada.grid(row=3,column=1)
        #
        botaoGravar=Button(frame,text = 'Gravar', bg = 'green', fg = 'white', font = self.font2)
        botaoGravar.bind('<Button-1>', self.validar_cadastro)
        botaoGravar.grid(row=4,column =1, pady=8)
        #
        cadastro.configure(background='tan1')
        cadastro.title('Cadastramento')
        cadastro.geometry('400x150')
        cadastro.mainloop()

    def ultima(self,event): # TELA DO RESULTADO
        ultima=Tk()
        login=self.loginEntrada.get().upper()
        genero=dados[login][1]
        if genero=='Feminino':
            sorteio=random.randint(0,31)
            tupla=['Miguel','Arthur','Davi','Bernardo','Gabriel','Pedro','Lucas','Matheus','Guilherme','Gustavo','Henrique','Felipe','Eduardo','Vitor','Deilson','Vitor','Caio','Thiago','Otavio','Bruno','Rodrigo','inexistente','Luan','Igor','Vinicius','cuzcuz com ovo','açai','uma lata de pitú','Flavius','Netflix','coxinha','esse que você ta pensando']
        else:
            sorteio=random.randint(0,31)
            tupla=['Alice','Sophia','Laura','Helena','Deilson','Júlia','Luiza','Lívia','Maria Eduarda','Ana','Melissa','Beatriz','Maíra','Elisa','Nicole','Gabriela','Marina','Alícia','Larissa','Daniele','Bianca','Laís','Carolina','Eduarda','inexistente','cuzcuz com ovo','açai','uma lata de pitú','Flavius','Netflix','coxinha','essa que você ta pensando']
        #
        frame=Frame(ultima,bg='snow')
        frame.grid()
        #
        label=Label(frame, bg = 'snow',fg='red', font = self.font1)
        label['text']='Olá %s, a sua alma gêmea é  %s ♥ ♥ ♥ ' %(dados[login][2],tupla[sorteio])
        label.grid(row=0, column = 0)
        #
        botao=Button(frame,bg = 'green', fg = 'white', text = 'Não gostou do resultado? Clique aqui!', font = self.font2)
        botao.bind('<Button-1>', self.haha)
        botao.grid(row = 1, column = 0,pady=10)
        
        #  
        ultima.configure(background='gold2')
        ultima.title('Resultado')
        ultima.geometry()
        ultima.mainloop()
 
    def validar_acesso(self,event):                           #CÓDIGO  LÓGICA
        login=self.loginEntrada.get().upper() 
        senha=self.senhaEntrada.get()
        if login in dados:
            if dados[login][0]==senha: 
                resultado=askquestion(title='Êxito', message='Acesso permitido, prosseguir?')    #ASK QUESTION
                if resultado == 'yes':
                    self.ultima(event)
            else:
                showinfo(title='Falha', message='Usuario e/ou senha incorretos')
        else:
            showinfo(title='Falha', message='Usuario e/ou senha incorretos')        

    def validar_cadastro(self,event):
        login=self.loginEntrada1.get().upper()
        senha=self.senhaEntrada1.get()
        genero=self.generoEntrada.get()
        nome=self.nomeEntrada.get()
        if len(login) !=0 and len(senha) !=0 and len(nome)!= 0:                                      #CÓDIGO DE LÓGICA
            aux=[senha,genero,nome]
            dados[login]=aux
            showinfo(title='Êxito!', message= 'Conta criada com sucesso!')
        else:
            showinfo(title='Falha!', message= 'Você deixou campos em branco!')
    def haha(self,event):
        showinfo(title='Vish..', message ='Você não tem escolha, comece a gostar ☺')
inicial=Tk ()
principal(inicial)
inicial.configure(background='dark violet')
inicial.title('Alma Gêmea')             # PROPRIEDADES DA PRIMEIRA JANELA
inicial.geometry('430x250')
inicial.mainloop()
