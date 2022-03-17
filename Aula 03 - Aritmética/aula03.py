nome = input('\n Qual é seu nome?')
print('\n Prazer em te conhecer , {}'.format(nome))

print('\n Vamos fazer calculos?\n')

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
soma = n1 + n2
mult = n1 * n2
div = n1 / n2
divInt = n1 // n2
exp = n1 ** n2
print('A soma é {}, a multiplicação é {} e a divisão é {:.1f}.'.format(soma, mult, div), end = ' ')
print('A divisão inteira é {} e a potência é {}'.format(divInt, exp))