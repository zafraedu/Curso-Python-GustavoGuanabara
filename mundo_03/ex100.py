# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função
# vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores
# pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia():
    print('Sorteando 5 valores da lista: ', end=' ')
    lst = []
    for i in range(5):
        r_num = randint(0, 9)
        print(r_num, end=' ')
        sleep(0.5)
        lst.append(r_num)
    print('PRONTO!')
    return lst


def somaPar(lst):
    print(f'Somando os valores pares de {lst}, temos', sum(n for n in lst if n % 2 == 0))


lista = sorteia()
somaPar(lista)
