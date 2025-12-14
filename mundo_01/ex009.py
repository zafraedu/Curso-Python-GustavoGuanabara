# Faça um programa que leia un número inteiro qualquer e mostre na tela a sua tabuada.

n = int(input('Número: '))

for i in range(1, 11):
    print(f'{n} X {i} = {n * i}')
