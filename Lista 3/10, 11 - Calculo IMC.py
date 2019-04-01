print('Programa desenvolvido por Mateus Medeiros')
print()
print('Para calcular o seu IMC :D')
print()
altura=float(input('Digite sua altura, por exemplo 1.78: '))
peso=float(input('Digite seu peso, por exemplo 75.4: ' ))
print('Vamos calcular seu IMC')
print()
b=altura**2
imc=peso/b
if imc <= 18.5:
    print('Você está abaixo do peso.')
elif imc >=18.6 and imc<= 24.9:
    print('Você está saudável.')
elif imc>=25.0 and imc<= 29.9:
    print('Você está acima do peso ideal.')
elif imc >=30.0 and imc<= 34.9:
    print('Você está com obesidade grau I (leve)' )
elif imc >=35.0 and imc<= 39.9:
    print('Você está com obesidade grau II (severa)' )
elif imc >= 40.0:
    print('Você está com obesidade grau III (mórbida)' )
print('O Seu IMC é de: %5.2f ' % imc)
input()
