jogador = {'nome': str(input('Nome do Jogador: ')).strip().capitalize()}
partidas_jogadas =  int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
jogador['gols'] = [int(input(f'Quantos gols na partida {i}? ')) for i in range(partidas_jogadas)]
jogador['total'] = sum(jogador['gols'])
print('-=' * 20)
print(jogador)
print('-=' * 20)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {partidas_jogadas} partidas.')
for i, gols in enumerate(jogador['gols']):
    print(f'\t=> Na partida {i}, fez {gols} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
