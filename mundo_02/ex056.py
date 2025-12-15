# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homen mais velho.
# - Quantas mulheres tem menos de 20 anos.

from statistics import mean

ages = []
maior_age = [0, '']
mulheres_menores = 0

for i in range(0, 4):
    name = str(input('Nome: ')).strip().capitalize()
    age = int(input('Edade: '))
    ages.append(age)
    sexo = int(input('Sexo:\n0 para Mulher\n1 para Homen\n'))

    if sexo and age > maior_age[0]:
        maior_age = [age, name]
    if not sexo and age < 20:
        mulheres_menores += 1

print(f'A média de idade é {mean(ages)}')
print(f'O Homen com mais idade é {maior_age[1]} com {maior_age[0]} anos')
print(f'{mulheres_menores} sao menores a 20 anos')
