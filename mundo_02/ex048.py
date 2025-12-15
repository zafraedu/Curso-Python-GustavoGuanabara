# Faça um programa que calcule a soma entre todos os números impares que sao múltiplos de tres
# e que se encontram no intervalo de 1 até 500.

soma = 0
for i in range(1, 500 + 1, 2):
    if i % 3 == 0:
        soma += i
print(soma)
