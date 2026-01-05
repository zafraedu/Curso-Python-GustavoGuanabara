pessoas = list()
pesos = list()
while 1:
    pessoa = list()
    pessoa.append(str(input('Nome: ')).strip().capitalize())
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa)
    pesos.append(pessoa[1])

    validation = str(input('Quer continual ? [S/N]')).strip().lower()
    if validation[0] == 'n':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'As pessoas mais pesadas foram', end=' ')
for pessoa in pessoas:
    if pessoa[1] == max(pesos):
        print(f'[{pessoa[0]}]', end=' ')
print(f'\nAs pessoas menos pesadas foram', end=' ')
for pessoa in pessoas:
    if pessoa[1] == min(pesos):
        print(f'[{pessoa[0]}]', end=' ')
