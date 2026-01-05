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
