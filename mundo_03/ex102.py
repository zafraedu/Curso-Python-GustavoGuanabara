# Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a
# calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o
# processo de cálculo do fatorial.

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
