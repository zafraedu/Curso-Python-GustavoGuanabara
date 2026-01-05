from time import sleep
from random import randint

print('-'*30)
print(' ' * 6 + 'JOGA NA MEGA SENA')
print('-'*30)

number_games = input('Quantos jogos você quer que eu sorteie? ')
while not number_games.strip().isdigit():
    number_games = input('\033[1;31merror:\033[m o valor deve ser numerico: ')

print(f'\n\033[1m{'-='*3}  SORTEANDO {number_games} JOGOS  {'-='*3}\033[m')
for game in range(int(number_games)):
    numeros = []
    for i in range(6):
        n = randint(1, 60)
        while n in numeros:
            n = randint(1, 60)
        numeros.append(n)
    print(f'Jogo {game + 1}: {numeros}')
    sleep(1)
print(f'\033[1m{'-='*4} < BOA SORTE! > {'-='*5}\033[m')
