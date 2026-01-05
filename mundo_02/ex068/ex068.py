from random import randint

racha = 0
while 1:
    n_pc = randint(0, 10)
    user = input('Par o Impar [P/I]: ')
    if n_pc % 2 and user[0] in 'Pp':
        racha += 1
        print('\033[1;32mVENCEU\033[m')
    elif not n_pc % 2 and user[0] in 'Ii':
        racha += 1
        print('\033[1;32mVENCEU\033[m')
    else:
        print('\033[1;31mPERDEU\033[m')
        break
print(f'Ganhou {racha} {'vez' if racha == 1 else 'vezes'}')
