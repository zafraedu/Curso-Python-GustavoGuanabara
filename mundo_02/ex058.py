# Melhore o jogo do desafio 028 onde o computador vai "opensar" em um numero entre 0 e 10.
# So que agora o jogador vai tentar adivinhar ate acertar,
# mostrando no final quantos palpites foram necessarios para vencer.

from random import randint

n_pensado = randint(0, 10)
n_usuario = int(input('Digite em um numero de 0 a 10: '))

palpites = 0
while n_usuario != n_pensado:
    if not n_usuario in range(0, 10 + 1):
        if n_usuario > 10:
            n_usuario = int(input('\033[31merror: palpite nao valido\033[m\nDigite um numero menor (de 0 a 10): '))
        elif n_usuario < 0:
            n_usuario = int(input('\033[31merror: palpite nao valido\033[m\nDigite um numero maior a 0: '))
    else:
        n_usuario = int(input('Tente outro palpite: '))
        palpites += 1

print(f'{'='*40}\n'
      f'\033[1;32mAcertou\033[m, eu estava pensando no numero {n_pensado}\n'
      f'Voce levou somente {palpites} palpites.')
