# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:
# a) de 1 até 10, a cada 1
# b) de 10 até 0, a cada 2
# c) uma contagem personalizada

from time import sleep

def contador(inicio, fim, paso):
    print('-=' * 20)
    print(f'Contagem de {inicio} ate {fim} de {1 if paso == 0 else paso} em {1 if paso == 0 else paso}')
    print('-='*20)
    if inicio > fim:
        for i in range(inicio, fim - 1, -1 if paso == 0 else -paso):
            print(i, end=' ')
            sleep(0.3)
    else:
        for i in range(inicio, fim + 1, 1 if paso == 0 else paso):
            print(i, end=' ')
            sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Inicio: ')), int(input('Fim: ')), abs(int(input('Paso: '))))
