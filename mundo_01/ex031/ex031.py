# Desenvolva um programa que pergunte a distancia de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 para viagens mais longas.

km = int(input('Quantos Km de viagem: '))

if km > 200:
    price = km * .45
else:
    price = km * .50

print(f'A viagem vai custar R${price} por {km}Km rodados.')