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
