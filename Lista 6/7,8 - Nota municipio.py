print('Entrevista nota do municipio.')
total=0
n=0
resp=input('Há alguém disponível p/ responder? (Responda com S ou N)')
if resp.lower()=='s':
    while resp.lower()=='s':
        nota=float(input('Qual a nota? '))
        total+=nota
        n+=1
        resp=input('Há alguém disponível p/ responder? (Responda com S ou N)')
    media=total/n
    print('A média é %5.2f . ' % media)
else:
    print('Ninguém digitou nota.')
