# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

from statistics import mean

validation = 'S'
n_maior = 0
n_menor = 0
lista= []
while validation[0].upper() == 'S':
    n = int(input('Digite um numero: '))
    lista.append(n)
    validation = input('Quer continuar? [S/N] ')

print(f'A média entre todos os numeros é de {mean(lista)}')
print(f'O maior numero digitado foi {max(lista)}')
print(f'O menor numero digitado for {min(lista)}')
