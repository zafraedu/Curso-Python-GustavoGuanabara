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
