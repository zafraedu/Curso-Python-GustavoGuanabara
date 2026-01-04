km = int(input('Quantos Km rodados? '))
days = int(input('Quantos dias alugados? '))
price = (60 * days) + (.15 * km)

print(f'O total a pagar é de R${price:.2f}')
