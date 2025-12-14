# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condiçao de pagamento:
# - A vista dinheiro/cheque: 10% de desconto
# - A vista no cartao: 5% de desconto
# - em ate 2x no cartao: precio normal
# - 3x ou mais no cartao: 20% de juros

price_item = float(input('Preço do produto: '))
payment_method = int(input('''
\033[1;34m1\033[m - dinheiro/cheque
\033[1;34m2\033[m - Cartao
'''))

if payment_method == 1:
    print(f'Tu tens 10% de desconto, sua compra iŕa custar apenas {price_item - price_item * .10}')
elif payment_method == 2:
    payment_method += int(input('''
    \rVai querer parcelar sua compra ?
    
    \r\033[1;34m0\033[m - Nao
    \r\033[1;34m1\033[m - 2x
    \r\033[1;34m(numero de quantas vezes quer parcelar)\033[m - 3x ou mais 
    \r'''))
else:
    print('error: invalid number;\nTry again ;)')

if payment_method == 2:
    print(f'Tu tens um 5% de desconto, sua compra irá custar apenas R${price_item - price_item * .05:.2f} [SEM JURO')
elif payment_method == 3:
    print(f'Preço normal, terás que pagar {price_item / 2} por mes')
elif payment_method > 3:
    print(f'Com juros de 20%, sua compra iŕa custar no final R${(price_item + price_item * .20) / (payment_method - 2):.2f} por mes')
print(payment_method - 2)

