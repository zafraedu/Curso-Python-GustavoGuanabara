# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matrix = [[int(input(f'Digite um valor para [{i}, {j}]: ')) for j in range(3)] for i in range(3)]
soma_pares = sum(elemento for fila in matrix for elemento in fila if elemento % 2 == 0)
soma_tercera_coluna = sum(matrix[i][-1] for i in range(3))
maior_valor_segunda_fila = max(matrix[1])

for fila in matrix:
    for elemento in fila:
        print(f'[{elemento:^5}]', end=' ')
    print()

print('A soma de todos os valores pares:', soma_pares)
print('A soma dos valores da tercera coluna:', soma_tercera_coluna)
print('O maior valor da segunda linha:', maior_valor_segunda_fila)
