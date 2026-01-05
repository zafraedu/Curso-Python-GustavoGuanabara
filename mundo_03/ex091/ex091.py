from operator import itemgetter
from random import randint
from time import sleep

jogadores = {f'jogador{i}': randint(1, 6) for i in range(1, 5)}
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ordered_dict = dict(sorted(jogadores.items(), key=itemgetter(1), reverse=True)) # key=lambda x: x[1]
print('Ranking dos jogadores:')
for i, (k, v) in enumerate(ordered_dict.items()):
    print(f'{i + 1}º lugar: {k} com {v}')
