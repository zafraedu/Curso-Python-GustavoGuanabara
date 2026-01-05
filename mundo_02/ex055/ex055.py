pesos = []
for i in range(0, 5):
    peso = float(input(f'Peso da {i + 1}º pessoa: '))
    pesos.append(peso)
print(f'O maior peso é de {max(pesos)}')
print(f'O menor peso é de {min(pesos)}')
