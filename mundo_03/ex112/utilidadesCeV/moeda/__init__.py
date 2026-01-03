def moeda(price): return f'R${price:.2f}'


def dobro(price, rs=False):
    if rs:
        return moeda(price * 2)
    return price * 2


def metade(price, rs=False):
    if rs:
        return moeda(price / 2)
    return price / 2


def aumentar(price, tax, rs=False):
    if rs:
        return moeda(price + price * (tax / 100))
    return price + price * (tax / 100)


def diminuir(price, tax, rs=False):
    if rs:
        return moeda(price - price * (tax / 100))
    return price - price * (tax / 100)


def resumo(price, mais=0, menos=0):
    print('-' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 30)
    print(f'{'Preço analisado:':<20}{moeda(price)}')
    print(f'{'Dobro do preço:':<20}{dobro(price, True)}')
    print(f'{'Metade do preço:':<20}{metade(price, True)}')
    print(f'{mais}{'% de aumento':<{20 - len(str(mais))}}{aumentar(price, mais, True)}')
    print(f'{menos}{'% de redução:':<{20 - len(str(menos))}}{diminuir(price, menos, True)}')
    print('-' * 30)
