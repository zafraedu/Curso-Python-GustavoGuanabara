velocidade = int(input('Velocidade em Km/h: '))

if velocidade > 80:
    print('Foi multado')
    print(f'A multa é de R${(velocidade - 80) * 7.00}')
