# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porçao Inteira.
#
# Ex:
# Digite um núumero: 6.127
# O número 6.127 tem a parte inteira 6.

from math import trunc

n = float(input('Number: '))

# print(f'O número {n} tem a parte inteira {n:.0f}.') # without module
print(f'O número {n} tem a parte inteira {trunc(n)}.')
