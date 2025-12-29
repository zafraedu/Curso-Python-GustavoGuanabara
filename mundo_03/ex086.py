# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.

matrix = []
for i in range(3):
    fila = []
    for j in range(3):
        n = input(f'Digite um valor para [{i}, {j}]: ')
        while not n.isdigit() or int(n) > 999:
            n = input(f'\033[1;31merror:\033[m digite un valor numerico entre 0 e 999: ')
        fila.append(int(n))
    matrix.append(fila)

print('_'*30)
for fila in matrix:
    for element in fila:
        print(f'[{element:^5}]', end=' ')
    print()
print('_'*30)

# matrix = [[int(input(f'Digite um valor para [{i}, {j}]: ')) for j in range(3)] for i in range(3)]
