# Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
# individualmente.

from statistics import mean

lista_completa = []
while 1:
    aluno = [str(input('Nome: ')).strip().capitalize(), [float(input(f'Nota {i + 1}: ')) for i in range(2)]]
    lista_completa.append(aluno)

    validation = str(input('Quer continuar? [S/N]: ')).strip()
    if validation in 'nN':
        break

print('-=-'*10)
print(f'{'No.':<4}{'NOME':<10}{'MÉDIA':>8}')
print('-'*30)
for i, (nome, notas) in enumerate(lista_completa):
    print(f'{i:<4}{nome:<10}{mean(notas):>8}')
print('-'*30)

while 1:
    opt = int(input('Mostrar notas de qual alununo ? (999 interrompe): '))
    if opt == 999:
        break
    if 0 <= opt < len(lista_completa):
        print(f'As notas de {lista_completa[opt][0]} foram {lista_completa[opt][1]}')
        print('-'*30)
