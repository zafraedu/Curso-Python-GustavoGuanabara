jogadores = []
while True:
    jogador = dict()
    jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()

    n_partidas = str(input(f'Quantas partidas o {jogador['nome']} jogou? ')).strip()
    while not n_partidas.isdigit():
        print('\033[31merror:\033[m Por favor, digite um valor numérico')
        n_partidas = str(input(f'Quantas partidas o {jogador['nome']} jogou? ')).strip()

    jogador['gols'] = []
    for i in range(int(n_partidas)):
        gol = str(input(f'\tQuantos gols na partida {i + 1}? ')).strip()
        while not gol.isdigit():
            gol = str(input(f'\tQuantos gols na partida {i + 1}? ')).strip()
        jogador['gols'].append(int(gol))

    jogador['total'] = sum(jogador['gols'])
    jogadores.append(jogador)

    validation = str(input('Quer continuar? [S/N] ')).strip().upper()
    while len(validation) > 1 or validation not in 'SNsn':
        print('\033[31merror:\033[m Responda somente com S ou N.')
        validation = str(input('Quer continuar? [S/N] ')).strip().upper()
    if validation == 'N':
        break
print('-=' * 20)

print(f'{'cod':<4}{'nome':<15}{'gols':<15}{'total':<15}')
print('-' * 40)
for index, jogador in enumerate(jogadores):
    print(f'{index:<4}', end='')
    for v in jogador.values():
        print(f'{str(v):<15}', end='')
    print()
print('-' * 40)

while True:
    id_jogador = str(input('Mostrar os dados de qual jogador? (999 para terminar) ')).strip()
    while not id_jogador.isdigit() or int(id_jogador) >= len(jogadores) and id_jogador != '999':
        print('\033[31merror:\033[m O valor deve de estar na lista.')
        id_jogador = str(input('Mostrar os dados de qual jogador? (999 para terminar) ')).strip()
    id_jogador = int(id_jogador)
    if id_jogador == 999:
        break

    print(f' -- LEVANTAMENTO DO JOGADOR {jogadores[id_jogador]['nome']}')
    for i, gols in enumerate(jogadores[id_jogador]['gols']):
          print(f'\tNo jogo {i + 1} fez {gols} gols.')
    print('-' * 40)
