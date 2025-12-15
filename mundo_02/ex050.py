# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.

soma = 0
for i in range(0, 6):
    n = int(input(f'Digite o {i + 1}º numero: '))
    if not n % 2:
        soma += n
print(soma)
