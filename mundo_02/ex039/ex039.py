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
