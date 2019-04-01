print("Verificar se o numero é perfeit")
num = int(input("digite o primeiro número: "))
lim= int(input('Digite o segundo numero: '))
tmp = 0 # soma, que vai decidir de se é perfeito ou não

for n in range(num, lim+1): # aumentando os numeros dados
    for i in range(1,n+1): # divisores dos numeros dados
        if n%i==0:         # se n(que é o numero dado) for divisivel pelo nosso divisor 1, ele ganha 1 ponto.
            tmp+=i    
    if 2*n==tmp:        # se o tmp, que são nossos pontos chegarem a metade do nosso numero, ele é perfeito. Pois a formula diz.
        print(n)
        
    tmp=0



         #i=
         #soma=1
