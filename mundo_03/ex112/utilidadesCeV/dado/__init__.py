def leiaDinheiro(price):
    while True:
        price = price.strip()
        if price.count('.') <= 1 and price.replace('.', '').isnumeric(): break # if is a float or int
        if ',' in price and price.count(',') == 1 and '.' not in price: # convert ',' in '.' (float)
            price = price.replace(',', '.')
            break

        print(f'\033[31merror: \'{price}\' é um preço inválido!\033[m')
        price = input('Digite o preço: R$')
    return float(price)


def leiaInt(txt: str) -> int:
    n = str(input(txt)).strip()
    while not n.isdigit():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        n = str(input(txt)).strip()
    return int(n)