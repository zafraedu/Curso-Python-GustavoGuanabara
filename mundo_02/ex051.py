# Desenvolva um programa que leia o primeiro termo e a razao de uma PA.
# No final, mostre os 10 primeiros temos dessa progressao

primeiro_termo = int(input('Primeiro termo da progressao aritimetica: '))
razao = int(input('Razao da progressao aritimetica: '))

# termo = primeiro_termo
# print(termo)
# for i in range(1, 10):
#     termo += razao
#     print(termo)
decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo, razao):
    print(f'{i} ', end=' ')