# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

numeros = ''
for i in range(4):
    numeros += input('Digite um numero: ')

tupla_str = tuple(numeros)
print(tupla_str)
print(f'O valor 9 apareceu {'vez' if tupla_str.count('9') == 1 else 'vezes'}')
print(f'{tupla_str.index('3') if '3' in tupla_str else 'O valor 3 nao se encontra na lista'}')
print('Os valores pares digitados foram', len(tuple(x for x in tupla_str if int(x) % 2 == 0)))
