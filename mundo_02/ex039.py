# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
anoa = date.today().year
anon = int(input('Ano de nascimento: '))
age = anoa - anon

if age > 18:
    print(f'O senhor já passou do prazo por {age - 18} {'anos' if age - 18 > 1 else 'ano'}')
elif age < 18:
    print(f'Rapaz, falta {18 - age} {'anos' if 18 - age > 1 else 'ano'} ainda para se alistar')
else:
    print('Voce deve se alistar')
