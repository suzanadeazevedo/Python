a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #tuplas juntas
d = b + a #tuplas juntas
print(c)
print(d)

print(20*'-')
print(len(c))
print(c.count(5)) #conta quantas vezes aparece elemento escolhido

print(20*'-')
print(d.index(8))#qual posição no index esta o elemento 8
print(d.index(5,1))#deslocamento
