valor_total = int(input('Qual será o valor sacado? '))
valor_sacado = 0

while valor_sacado != valor_total:
    resto = valor_total - valor_sacado
    if resto // 50 >= 1:
        valor_sacado += (resto // 50) * 50
        print(f'{resto // 50} cedulas de R$50')
    elif resto // 20 >= 1:
        valor_sacado += (resto // 20) * 20
        print(f'{resto // 20} cedulas de R$20')
    elif resto // 10 >= 1:
        valor_sacado += (resto // 10) * 10
        print(f'{resto // 10} cedulas de R$10')
    elif resto // 1 >= 1:
        valor_sacado += (resto // 1) * 1
        print(f'{resto // 1} cedulas de R$1')
