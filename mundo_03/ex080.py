# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

numeros: list = []
for i in range(5):
    n = int(input('Digite um valor: '))
    if not numeros or n >= numeros[-1]:
        numeros.append(n)
        print(f'Adicionado ao final da lista ...')
    else:
        pos = 0
        while pos < len(numeros):
            if n <= numeros[pos]:
                numeros.insert(pos, n)
                print(f'Adicionado na posiçao {pos} da lista ...')
                break
            pos += 1

print('Os valores digitados em ordem foram', numeros)

# numeros: list = []
# for i in range(5):
#     n = int(input('Digite um valor: '))
#     numeros.append(n)
#     numeros = sorted(numeros) # una trampa
#     if n == max(numeros):
#         print(f'Adicionado ao final da lista ...')
#     else:
#         print(f'Adicionado na posiçao {numeros.index(n)} da lista ...')