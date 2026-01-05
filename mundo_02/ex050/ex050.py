soma = 0
for i in range(0, 6):
    n = int(input(f'Digite o {i + 1}º numero: '))
    if not n % 2:
        soma += n
print(soma)
