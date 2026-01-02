#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e
# quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha
# sido informado corretamente.

def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')

nome_jogador = str(input('Nome do Jogador: ')).strip().capitalize()
gols_jogador = str(input('Número de Gols: ')).strip()

if gols_jogador.isdigit():
    gols_jogador = int(gols_jogador)
else:
    gols_jogador = 0
if nome_jogador == '':
    ficha(gols=gols_jogador)
else:
    ficha(nome_jogador, gols_jogador)
