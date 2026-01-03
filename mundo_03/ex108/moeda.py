def dobro(price): return price * 2
def metade(price): return price / 2
def aumento(price, tax): return price + price * (tax / 100)
def diminuir(price, tax): return price - price * (tax / 100)
def moeda(price): return f'R${price:.2f}'