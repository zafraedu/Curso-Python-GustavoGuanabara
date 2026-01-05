termos_total = int(input('Quantos termos vc quer mostrar? '))

i = 0
a, b = (0, 1)
fib = 0
while i < termos_total:
    print(fib, end=' ')
    a = b
    b = fib
    fib = a + b
    i += 1
