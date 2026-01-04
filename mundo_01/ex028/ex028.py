from random import randint

n_computador = randint(0, 5)
n_usuario = (int(input('Pense em um número de 0 a 5 ')))

print('VENCEU' if n_usuario == n_computador else 'PERDEU')
print(f'O computador pensou no número {n_computador}')
