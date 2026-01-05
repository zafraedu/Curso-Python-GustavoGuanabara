tupla = ('Lapis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99)

for pos, i in enumerate(tupla):
    if not pos % 2:
        print(f'{i:.<30}', end='')
    else:
        print(f'R$ {i:>6.2f}')
