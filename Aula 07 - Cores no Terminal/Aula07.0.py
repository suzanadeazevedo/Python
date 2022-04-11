#\033[ style; tex,;back m
#style 0 -nada, 1- negrito , 4 -underline,- 7 negative
#text cores 30 branco, 31 vermelho, 32 verde, 33 amarelo, 34 azul, 35 lilas, 36 turquesa,  37 cinza
#background cores 40 a 47
#\033[0;33;44m
#\033[4;33;44m
#\033[1;35;43m
#\033[30;42m
#\033[m
#\033[7;30m
print('\033[4;30;45mOlá mundo\033[m')

a = 3
b = 5
print('Os valores são \033[32:40m{}\033[m e \033[31:40m{}\033[m!!!'.format(a,b))
nome = 'Suzana'
print('Olá, muito prazer, {} {} {}'.format('\033[2:31m', nome, '\033[m'))