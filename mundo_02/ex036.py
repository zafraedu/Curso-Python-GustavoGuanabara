# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quatos anos ele vai pagar.
# Calcule o valor da prestaçao mensal, sabendo que ela nao pode exceder 30% do salário ou entao o empréstimo será negado

valor_casa = float(input('Valor da Casa: '))
salario = float(input('Salário do comprador: '))
anos_pagar = int(input('Em quantos anos pretende pagar: '))

if salario * .3 * 12 * anos_pagar < valor_casa:
    print(f'O empréstimo foi {'\033[1;31m'}NEGADO{'\033[m'}')
else:
    print(f'O empréstimo foi {'\033[1;32m'}APROVADO{'\033[m'}')
