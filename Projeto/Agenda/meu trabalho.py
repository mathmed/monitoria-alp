from tkinter import *
dados={}
aux=[]
class agenda(object):
    def __init__(self , meu):
        #FONTE
        self.font=('Verdana', '20', 'bold')
        self.font1=('Verdana', '12', 'bold')
        #FRAME LOGO
        self.framelogo=Frame(meu, bg = 'light green')
        self.framelogo.pack()
        #FRAME BOTÕES
        self.frame1=Frame(meu, pady= 25, bg='light green')
        self.frame1.pack()
        #FRAME SAIR
        self.framesair=Frame(meu, pady= 15, bg = 'light green')
        self.framesair.pack()
        #FRAME MATEUS
        self.framemath=Frame(meu)
        self.framemath.pack()
        #BOTÕES
        botões=('Novo contato' , 'Dados contato', 'Alterar dados', 'Deletar contato', 'Busca avançada')
        subframe=Frame(self.frame1)
        subframe.pack()
        #ABRE CONTATO
        self.b1=Button(subframe,text = botões[0], bg = 'green', fg= 'white', width= 25, padx =5, font = self.font)
        self.b1.bind("<Button-1>", self.abre_novocontato)
        #ABRE PESQUISA
        self.b2=Button(subframe,text = botões[1], bg = 'green', fg= 'white', width= 25, padx =5, font = self.font)
        self.b2.bind("<Button-1>", self.abre_pesquisa)
        self.b3=Button(subframe,text = botões[2], bg = 'green', fg= 'white', width= 25, padx =5, font = self.font)
        self.b3.bind("<Button-1>", self.alterar_dados)
         #FALTA COLOCAR
        self.b4=Button(subframe,text = botões[3], bg = 'green', fg= 'white', width= 25, padx =5, font = self.font)
        self.b5=Button(subframe,text = botões[4], bg = 'green', fg= 'white', width= 25, padx =5, font = self.font)
        self.b1.pack(side = TOP)
        self.b2.pack(side = TOP)
        self.b3.pack(side = TOP)
        self.b4.pack(side = TOP)
        self.b5.pack(side = TOP)
        
        #IMAGEM
        logo = PhotoImage(file = 'agenda1.gif')
        self.logo = Label(self.framelogo,bg='light green')
        self.logo['image'] = logo
        self.logo.image = logo
        self.logo.pack()
            
        #BOTÃO SAIR
        self.botao=Button(self.framesair, text = 'Sair', bg = 'red' , fg = 'white', width =25, padx=5, font= self.font)
        self.botao.pack(side = LEFT)
        #FEITO POR MATH
        self.math=Label(self.framemath, text= 'Feito por @MathMed', bg = 'black', fg= 'white', font = self.font)
        self.math.pack(side = BOTTOM)
        ####
    def abre_novocontato (self, event):
        raiz=Tk()
        #FRAMES
        self.framecampos=Frame(raiz, bg = 'light blue')
        self.framecampos.grid()
        #
        self.framegravar=Frame(raiz,bg = 'light blue')
        self.framegravar.grid(row =3, column = 0, pady=35)
        #NOME
        self.nome=Label(self.framecampos, text = 'Nome contato: ' ,bg = 'light blue', font= self.font1)
        self.nome.grid(row = 0, column=0)
        self.nome1=Entry(self.framecampos)
        self.nome1.grid(row =0, column = 1)
        #NUMERO
        self.numero=Label(self.framecampos, text = 'Número contato: ' ,bg = 'light blue', font= self.font1)
        self.numero.grid(row = 1, column=0)
        self.numero1=Entry(self.framecampos)
        self.numero1.grid(row =1, column = 1)
        #CIDADE
        self.cidade=Label(self.framecampos, text = 'Cidade: ' ,bg = 'light blue', font= self.font1)
        self.cidade.grid(row = 2, column=0)
        self.cidade1=Entry(self.framecampos)
        self.cidade1.grid(row =2, column = 1)
        #ESTADO
        self.estado=Label(self.framecampos, text = 'Estado: ' ,bg = 'light blue', font= self.font1)
        self.estado.grid(row = 3, column=0)
        self.estado1=Entry(self.framecampos)
        self.estado1.grid(row =3, column = 1)
        #EMAIL
        self.email=Label(self.framecampos, text = 'Email: ' ,bg = 'light blue', font= self.font1)
        self.email.grid(row = 4, column=0)
        self.email1=Entry(self.framecampos)
        self.email1.grid(row =4, column = 1)
        #GRAVAR
        self.botaogravar=Button(self.framegravar, text= 'Gravar', bg= 'green', fg='white', font = self.font1)
        self.botaogravar.bind("<Button-1>", self.gravar)
        self.botaogravar.grid()
        #RESULTADO
        self.resultado=Label(self.framegravar, bg = 'light blue', fg = 'white', font = self.font1)
        self.resultado.grid()
        #
        raiz['bg']='light blue'
        raiz.title('Novo Contato')
        raiz.geometry('400x300')
        raiz.mainloop()
    def gravar(self,event):
        #GRAVAR
        self.resultado['text']='Gravado com sucesso.'
        self.resultado['bg']='green'
        a=self.nome1.get().upper()
        nome=a
        numero=self.numero1.get()
        cidade=self.cidade1.get()
        estado=self.estado1.get()
        email=self.email1.get()
        aux=[nome,numero,cidade,estado,email]
        dados[nome]=aux




        
        ####
    def abre_pesquisa(self,event):
        raiz1= Tk()
        #FRAMES  
        self.frameentrada=Frame(raiz1 , bg= 'grey')
        self.frameentrada.grid()
        #
        self.frameresult=Frame(raiz1, bg = 'grey')
        self.frameresult.grid(sticky=W)
        #
        self.framepesquisar=Frame(raiz1,bg= 'grey')
        self.framepesquisar.grid(sticky=S)
        #ENTRADA
        self.entrada=Label(self.frameentrada, text =' Nome do contato:' , bg = 'black', fg = 'white', font = self.font1)
        self.entrada1=Entry(self.frameentrada)
        self.entrada.grid(row=1, column= 2)
        self.entrada1.grid(row = 1, column = 5)
        #SAIDA NOME
        self.nomepesquisado=Label(self.frameresult, text = 'Nome:' , bg = 'black', fg = 'white', font= self.font1)
        self.nomepesquisado.grid(row = 6, column = 0,sticky=W,pady=10)
        self.nomepesquisado1=Label(self.frameresult, bg = 'grey', font= self.font1)
        self.nomepesquisado1.grid(row = 6, column = 1, sticky=W,pady=10)
        #SAÍDA NUMERO
        self.numeropesquisado=Label(self.frameresult, text = 'Número:' , bg = 'black', fg = 'white', font= self.font1)
        self.numeropesquisado.grid(row=7,column= 0,sticky=W,pady=10)
        self.numeropesquisado1=Label(self.frameresult, bg = 'grey', font= self.font1)
        self.numeropesquisado1.grid(row = 7, column = 1, sticky=W,pady=10)
        #SAÍDA CIDADE
        self.cidadepesquisado=Label(self.frameresult, text = 'Cidade:' , bg = 'black', fg = 'white', font= self.font1)
        self.cidadepesquisado.grid(row = 8, column= 0,sticky=W,pady=10)
        self.cidadepesquisado1=Label(self.frameresult, bg = 'grey', font= self.font1)
        self.cidadepesquisado1.grid(row = 8, column = 1, sticky=W,pady=10)
        #SAÍDA ESTADO
        self.estadopesquisado=Label(self.frameresult, text = 'Estado:' , bg = 'black', fg = 'white', font= self.font1)
        self.estadopesquisado.grid(row = 9, column= 0,sticky=W,pady=10)
        self.estadopesquisado1=Label(self.frameresult, bg = 'grey', font= self.font1)
        self.estadopesquisado1.grid(row = 9, column = 1, sticky=W,pady=10)
        #SAÍDA EMAIL
        self.emailpesquisado=Label(self.frameresult, text = 'Email:' , bg = 'black', fg = 'white', font= self.font1)
        self.emailpesquisado.grid(row = 10, column = 0,sticky=W,pady=10)
        self.emailpesquisado1=Label(self.frameresult, bg = 'grey', font= self.font1)
        self.emailpesquisado1.grid(row = 10, column = 1, sticky=W,pady=10)

        #BOTAO PESQUISAR
        self.pesquisa=Button(self.framepesquisar, text = 'Pesquisar' , bg = 'green', fg= 'white', font = self.font1)
        self.pesquisa.bind("<Button-1>", self.pesquisar)
        self.pesquisa.grid(row = 4, column = 7)
        #SAIDA SE NÃO TIVER DADOS
        self.saida=Label(self.framepesquisar, bg= 'grey', font= self.font1)
        self.saida.grid(row =6, column=7)
        #
        raiz1['bg']='grey'
        raiz1.title('Pesquisa')
        raiz1.geometry('600x400')
        raiz1.mainloop()

        
    def pesquisar(self,event):
        pesq=self.entrada1.get().upper()
        if pesq in dados:
            self.saida['text']='Contato encontrado.'
            self.saida['fg']='white'
            self.nomepesquisado1['text']=dados[pesq][0]
            self.nomepesquisado1['bg']='white'
            self.numeropesquisado1['text']=dados[pesq][1]
            self.numeropesquisado1['bg']='white'
            self.cidadepesquisado1['text']=dados[pesq][2]
            self.cidadepesquisado1['bg']='white'
            self.estadopesquisado1['text']=dados[pesq][3]
            self.estadopesquisado1['bg']='white'
            self.emailpesquisado1['text']=dados[pesq][4]
            self.emailpesquisado1['bg']='white'
        else:
            self.saida['text']='Nenhum contato com esses dados.'
            self.saida['fg']='red'
            self.nomepesquisado1['text']='xxxx'
            self.nomepesquisado1['bg']='red'
            self.numeropesquisado1['text']='xxxx'
            self.numeropesquisado1['bg']='red'
            self.cidadepesquisado1['text']='xxxx'
            self.cidadepesquisado1['bg']='red'
            self.estadopesquisado1['text']='xxxx'
            self.estadopesquisado1['bg']='red'
            self.emailpesquisado1['text']='xxxx'
            self.emailpesquisado1['bg']='red'


    def alterar_dados(self,event):
        raiz2= Tk()
        #FRAMES ENTRADAS
        self.framepesquisa=Frame(raiz2, bg = 'lightskyblue', pady=15)
        self.framepesquisa.pack()
        #FRAME BOTÕES
        self.framebotao=Frame(raiz2, bg = 'lightskyblue', pady=25)
        self.framebotao.pack()
        #FRAMEAUX
        self.subframe=Frame(self.framebotao)
        self.subframe.pack()
        #PESQUISA
        self.pesquisa=Label(self.framepesquisa, text = 'Nome do contato à alterar: ', bg='blue2', fg = 'white', font= self.font1)
        self.pesquisa.pack(side= LEFT)
        self.pesquisa1=Entry(self.framepesquisa)
        self.pesquisa1.pack(side = LEFT)
        #BOTÃO
        self.botao=Button(self.framepesquisa, text = 'Pesquisar', bg = 'blue2', fg = 'white' , font = self.font1)
        self.botao.bind("<Button-1>", self.se_pesquisa)
        self.botao.pack(side = BOTTOM)
        #SE NÃO TIVER OU TIVER (MENSAGEM)
        self.fail=Label(self.framepesquisa, bg='lightskyblue' ,fg = 'red' ,font = self.font1)
        self.fail.pack(side = BOTTOM)
        #SE TIVER
        self.botaonome=Button(self.subframe, text = 'Alterar nome' ,bg = 'blue2', fg='white', font = self.font1,width=25, padx=5)
        self.botaonome.bind("<Button-1>", self.change_name)
        self.botaonome.pack(side = TOP)
        #
        self.botaonumero=Button(self.subframe, text = 'Alterar número' ,bg = 'blue2', fg='white', font = self.font1, width=25, padx=5)
        self.botaonumero.pack(side = TOP)
        #
        self.botaocidade=Button(self.subframe, text = 'Alterar Cidade' ,bg = 'blue2', fg='white', font = self.font1, width=25, padx=5)
        self.botaocidade.pack(side = TOP)
        #
        self.botaoestado=Button(self.subframe, text = 'Alterar Estado' ,bg = 'blue2', fg='white', font = self.font1, width=25, padx=5)
        self.botaoestado.pack(side = TOP)
        #
        self.botaoemail=Button(self.subframe, text = 'Alterar E-Mail' ,bg = 'blue2', fg='white', font = self.font1, width=25, padx=5)
        self.botaoemail.pack(side = TOP)
        #
        

        
        raiz2['bg']='lightskyblue'
        raiz2.title('Alterar Dados')
        raiz2.geometry('600x400')
        raiz2.mainloop()

    def se_pesquisa(self,event):
        pesq1=self.pesquisa1.get().upper()
        if pesq1 in dados:
            self.fail['text']='Contato encontrado'
            self.fail['fg']='black'
        else:
            self.fail['text']='Contato não encontrado'
            self.fail['fg']='red'
            
    def change_name (self,event):
        if self.fail['text']=='Contato encontrado':
            alterarnome= Tk()
            #FRAMES
            self.framegeral=Frame(alterarnome, bg = 'lightskyblue', pady=25)
            self.framegeral.pack()
            #LABEL, ENTRY E BUTTON
            self.alterarnomelabel=Label(self.framegeral, bg = 'lightskyblue', fg= 'white', text = 'Novo nome:' , font= self.font1)
            self.alterarnomelabel.pack(side= LEFT)
            #
            self.alterarnomeentry=Entry(self.framegeral)
            self.alterarnomeentry.pack(side= LEFT)
            #
            self.alterarnomebotao=Button(self.framegeral, bg = 'green' , fg = 'white', text = 'Gravar', font= self.font1)
            self.alterarnomebotao.bind("<Button-1>", self.change_name1)
            self.alterarnomebotao.pack(side=BOTTOM)


            alterarnome['bg'] = 'lightskyblue'
            alterarnome.title('Alterar Nome')
            alterarnome.geometry('400x200')
            alterarnome.mainloop()

    def change_name1(self, event):
        aux1=self.pesquisa1.get().upper()
        aux2 = self.alterarnomeentry.get().upper()
        dados[aux1][0]=aux2
        dados[aux]=aux2


        

meu = Tk()
meu['bg']='light green'
agenda(meu)
meu.title('Agenda')
meu.geometry('1200x800')
meu.wm_iconbitmap('favicon.ico')
meu.mainloop()
