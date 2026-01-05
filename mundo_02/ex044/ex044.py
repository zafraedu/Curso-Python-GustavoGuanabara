price_item = float(input('Preço do produto: '))
payment_method = int(input('''
\033[1;34m1\033[m - dinheiro/cheque
\033[1;34m2\033[m - Cartão
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
