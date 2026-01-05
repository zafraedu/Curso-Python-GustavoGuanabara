km = int(input('Quantos Km de viagem: '))

if km > 200:
    price = km * .45
else:
    price = km * .50

print(f'A viagem vai custar R${price} por {km}Km rodados.')
