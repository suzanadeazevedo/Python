# else if = elif
#if -> elif -> else (else apenas uma vez)

nome = str(input('Qual é o seu nome?: '))
if nome == 'Loki':
    print('Que nome bonito ^.^')
elif nome == 'João' or nome =='Maria':
    print('Seu nome é bem popular no Brasil :)')
elif nome in 'Ana Claudia Paula Natalia':
    print('É um nome feminino comum :S')
else:
    print('Que nome comum ¬¬ ')
print('Tenha um bom dia {}!'.format(nome))