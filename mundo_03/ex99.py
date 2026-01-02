# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.

from time import sleep

def maior(*num):
    num_maior = num[0] if num else 0
    print('-=' * 30)
    print('Analisando os valores pasados ...')
    for n in num:
        print(n, end=' ')
        sleep(0.3)
        if n > num_maior:
            num_maior = n
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor valor informado foi {num_maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
