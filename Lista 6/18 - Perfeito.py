print("Verificar se o numero é perfeit")
n = int(input("digite o numero: "))
cont = 1 # contador
soma = 0 # soma, que vai decidir de se é perfeito ou não

while cont<n: #vamos contar até chegar no numero, ou seja, dividir por todos os numeros até ele msmo
 if n%cont==0:  #se a divisão for possível continuamos
     soma = soma + cont
     cont = cont + 1
 else:
     cont = cont + 1 #se não, so vamos aumentar o contador
     
if soma==n:
  print ("Número perfeito")
else:
  print("Não é perfeito.")
