times = ('Palmeiras', 'Corinthians', 'Internacional', 'Cruzeiro', 'Santos', 'Grêmio', 'Atlético Mineiro',
         'Fluminense', 'Botafogo', 'Flamengo', 'São Paulo', 'Vasco da Gama', 'Portuguesa', 'Bahia',
         'Atlético Paranaense', 'Bangu', 'Santa Cruz', 'America', 'Coritiba', 'Ponte Preta')

print(f'Lista de times do Brasileirao: {times}')
print(f'Os 5 primeiros sao {times[:5]}')
print(f'Os 4 ultimos sao {times[-4:]}')
print(f'Times em ordem alfabetica: {sorted(times)}')
print(f'O Corinthians esta na {times.index('Corinthians') + 1}ª posicao')
