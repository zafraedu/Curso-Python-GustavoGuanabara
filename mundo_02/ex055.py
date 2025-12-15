# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maio e o menor peso lidos.

pesos = []
for i in range(0, 5):
    peso = float(input(f'Peso da {i + 1}º pessoa: '))
    pesos.append(peso)
print(f'O maior peso é de {max(pesos)}')
print(f'O menor peso é de {min(pesos)}')
