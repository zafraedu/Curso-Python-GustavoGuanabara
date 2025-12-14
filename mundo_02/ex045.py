# Crie um programa que faça o computador jogar Jokenpo com voce.

from random import randint
from time import sleep

items = ('Pedra', 'Papel', 'Tesoura')

user = int(input('''
\033[1mVamos jogar JOKENPO escolha um número de 0 a 2\033[m

\033[1;34m0\033[m para PEDRA
\033[1;33m1\033[m para PAPEL
\033[1;31m2\033[m para TESOURA
'''))
computer = randint(0, 2)

if user > 2:
    print('\033[31mERROR: Digite um número de \033[1m0\033[0;31m ao \033[1m2\033[0;31m, seu burro\033[m')
else:
    print('JO')
    sleep(.5)
    print('KEN')
    sleep(.5)
    print('PO !!!!!\n')


if user == 0 and computer == 1:
    print(f'O computador escolheu {items[computer]}\n\033[1;31mPERDEU\033[m')
elif user == 1 and computer == 2:
    print(f'O computador escolheu {items[computer]}\n\033[1;31mPERDEU\033[m')
elif user == 2 and computer == 0:
    print(f'O computador escolheu {items[computer]}\n\033[1;31mPERDEU\033[m')
elif user == 0 and computer == 2:
    print(f'O computador escolheu {items[computer]}\n\033[1;32mVENCEU\033[m')
elif user == 1 and computer == 0:
    print(f'O computador escolheu {items[computer]}\n\033[1;32mVENCEU\033[m')
elif user == 2 and computer == 1:
    print(f'O computador escolheu {items[computer]}\n\033[1;32mVENCEU\033[m')
elif user == computer:
    print(f'O computador escolheu {items[computer]}\n\033[1;33mEMPATE\033[m')
