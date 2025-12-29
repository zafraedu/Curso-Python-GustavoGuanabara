# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista_unica: list = [[], []]
for i in range(7):
    n = input(f'Digite o {i + 1}o. valor: ')
    while not n.isdigit():
        n = input('\033[31merror:\033[m digite um numero: ')
    n = int(n)

    if n % 2 == 0:
        lista_unica[0].append(n)
    else:
        lista_unica[1].append(n)
print('_'*30)
print('Lista original:', lista_unica)
print('Valores PARES:', sorted(lista_unica[0]))
print('Valores IMPARES:', sorted(lista_unica[1]))
