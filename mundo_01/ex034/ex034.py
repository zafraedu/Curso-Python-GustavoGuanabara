salario = float(input('Qual é o seu salário? '))

if salario > 1250:
    new_salario = salario + salario * .10
else:
    new_salario = salario + salario * .15

print('\nTeve um aumento de', end=' ')
print('15%' if salario <= 1250 else '10%')
print(f'O valor do seu novo salário  é de R${new_salario:.2f}')
