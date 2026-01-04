# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7.00 por cada Km acima do limite

velocidade = int(input('Velocidade em Km/h: '))

if velocidade > 80:
    print('Foi multado')
    print(f'A multa é de R${(velocidade - 80) * 7.00}')
