primeiro_termo = int(input('Primeiro termo da progressão aritmética: '))
razao = int(input('Razão da progressão aritmética: '))

decimo = primeiro_termo + (10 - 1) * razao
for i in range(primeiro_termo, decimo, razao):
    print(f'{i} ', end=' ')

# termo = primeiro_termo
# print(termo)
# for i in range(1, 10):
#     termo += razao
#     print(termo)
