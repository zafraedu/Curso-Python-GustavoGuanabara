# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos Dólares ela pode comprar. U$D 1 == R$3.27

brs = float(input('Dinheiro em R$: '))
print(f'Poderás comprar a quantidade de [{brs / 3.27:.2f}] Dólares com {brs} Reais.')