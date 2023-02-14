#Tuplas: Variaveis Compostas
#Elemento identificado por indice
#for c in tupla
#tuplas são IMUTAVEIS, não tem como tirar o item e nem mudar.
#tuplas em python aceita varios tipos de dados juntos
#del(tupla) deleta tupla
#from typing import Tuple

#lanche: tuple[str, str, str, str] = ('hamburguer', 'suco', 'pizza', 'pudim')
lanche= ('hamburguer', 'suco', 'pizza', 'pudim')
print(lanche[1:3])
print(lanche[:3])
print(lanche[1])
print(lanche[-2:])
print(lanche[-1])
print(lanche)
print(3*'*')
print(len(lanche))
print(3*'*')
print(sorted(lanche)) #ordenado
print(20*'-')

for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print(20*'-')

for cont in range (0, len(lanche)):
    print(cont)
print(20 * '-')

for cont in range (0, len(lanche)):
    print(lanche[cont])
print(20 * '-')

for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} -> número {pos}')
print(20 * '-')






