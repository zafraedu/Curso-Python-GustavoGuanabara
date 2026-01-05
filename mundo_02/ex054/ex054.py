from datetime import date

maior = 0
menor = 0

for i in range(0, 7):
    ano_nascimento = int(input('Ano de nascimento: '))
    age = date.today().year - ano_nascimento
    if age >= 21:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas já soa maiores de 21 anos')
print(f'{menor} pessoas ainda nao soa maiores de 21 anos')
