from statistics import mean

ages = []
maior_age = [0, '']
mulheres_menores = 0

for i in range(0, 4):
    name = str(input('Nome: ')).strip().capitalize()
    age = int(input('Edade: '))
    ages.append(age)
    sexo = int(input('Sexo:\n0 para Mulher\n1 para Homem\n'))

    if sexo and age > maior_age[0]:
        maior_age = [age, name]
    if not sexo and age < 20:
        mulheres_menores += 1

print(f'A média de idade é {mean(ages)}')
print(f'O Homen com mais idade é {maior_age[1]} com {maior_age[0]} anos')
print(f'{mulheres_menores} sao menores a 20 anos')
