frase =  'Curso em Video Python'

# Analise

#Verificar comprimento
print (len(frase))

#contar detreminada letra
print (frase.count('o'))

#contar detreminada letra com fatiamento incluido
print (frase.count('o', 0, 13))

#encontrar (resultado afirma  inicio da posição) (valor inexistente resulta em -1)
print (frase.find('deo'))

#se existe string
print ('Curso' in frase)
