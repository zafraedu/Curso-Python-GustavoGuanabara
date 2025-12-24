# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final,
# mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = list()
for i in range(5):
    numeros.append(int(input(f'{i}º Numero: ')))
numeros_max = numeros.count(max(numeros))
numeros_min = numeros.count(min(numeros))

print(f'\nEl maior numero es el {max(numeros)} y esta en {'las posiciones' if numeros_max > 1 else 'la posicion}'}', end=' ')
for pos, n in enumerate(numeros):
    if n == max(numeros):
        print(pos, end=' ')
print(f'\nEl menor numero es el {min(numeros)} y esta en {'las posiciones' if numeros_min >  1 else 'las posicion'}', end=' ')
for pos, n in enumerate(numeros):
    if n == min(numeros):
        print(pos, end=' ')

