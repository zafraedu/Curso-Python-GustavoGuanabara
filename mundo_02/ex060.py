from math import factorial

n = int(input('calcular seu Factorial: '))
i = n
imprime = f'{i}'
while i > 1:
    i -= 1
    imprime += f' x {i}'
print(f'Calculando {n}! = {imprime} = {factorial(n)}')