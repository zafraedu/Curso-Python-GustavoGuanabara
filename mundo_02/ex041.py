# A Confederaçao Nacional de Nataçao precisa de um programa que leia o ano de nascimento de um atleta e
# mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SENIOR
# - Acima: MASTER

from datetime import date
born = int(input('Ano de nascimento: '))
age = date.today().year - born

if age <= 9:
    print('MIRIM')
elif age <= 14:
    print('INFANTIL')
elif age <= 19:
    print('JUNIOR')
elif age <= 20:
    print('SENIOR')
else:
    print('MASTER')
