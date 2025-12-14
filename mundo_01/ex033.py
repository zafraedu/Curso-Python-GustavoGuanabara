# Faça um programa que leia tres números e mostre qual é o maior e qual é o menor.

from mycolours import color

n1 = int(input('Number 1: '))
n2 = int(input('Number 2: '))
n3 = int(input('Number 3:  '))

# nma = n1
# if nma < n2:
#     nma = n2
# if nma < n3:
#     nma = n3
#
# nmi = n1
# if nmi > n2:
#     nmi = n2
# if nmi > n3:
#     nmi = n3
#
# print(f'Maior: {nma}')
# print(f'Menor: {nmi}')

numeros = [n1, n2, n3]
print(f'Maior: {color['y']}{max(numeros)}{color['none']}')
print(f'Menor: {color['y']}{min(numeros)}{color['none']}')