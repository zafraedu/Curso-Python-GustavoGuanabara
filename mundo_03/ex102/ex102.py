def factorial(n: int, show: bool=False) -> int:
    """
    Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opicional) Mostrar ou nao a conta.
    :return: O valor do Fatorial de um número.
    """
    fac = 1
    for i in range(n, 0, -1):
        if show:
            print(f'{fac} x {i} = {fac * i}')
        fac *= i
    return fac


factorial(5, True)
print('-' * 30)
print('5! =', factorial(5, False))
