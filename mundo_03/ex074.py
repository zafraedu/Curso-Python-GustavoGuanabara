# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import randint

numeros = ''
for i in range(5):
    numeros += str(randint(0, 9))

tupla = tuple(numeros)
print(tupla)
print('Maior valor:', max(tupla))
print('Menor valor:', min(tupla))