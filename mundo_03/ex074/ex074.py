from random import randint

numeros = ''
for i in range(5):
    numeros += str(randint(0, 9))

tupla = tuple(numeros)
print(tupla)
print('Maior valor:', max(tupla))
print('Menor valor:', min(tupla))
