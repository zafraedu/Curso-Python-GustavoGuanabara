# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência
# de Fibonacci. Exemplo: [7] 0 – 1 – 1 – 2 – 3 – 5 – 8

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
