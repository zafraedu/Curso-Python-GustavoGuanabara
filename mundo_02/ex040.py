# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇAO
# - Média 7.0 ou superior: APROVADO

n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2

print(f'A sua média foi de {media:.1f}')

if media < 5.0:
    print('\033[1;31mREPROVADO\033[m')
elif media >= 7.0:
    print('\033[1;32mAPROVADO\033[m')
else:
    print('\033[1;33mRECUPERAÇAO\033[m')
