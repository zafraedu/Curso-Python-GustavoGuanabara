# Refaça o DESAFIO 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# Equilátero: todos os lado iguais
# Isósceles: dois lados iguais
# Escaleno: todos os lados diferentes

r1 = int(input('r1: '))
r2 = int(input('r2: '))
r3 = int(input('r3: '))

if r1 + r2 >= r3 and r1 + r3 >= r2 and r2 + r3 >= r1:
    if r1 == r2 == r3:
        print('Forma um triangulo \033[1;34mEquilátero\033[m')
    elif r1 != r2 != r3:
        print('Forma um triangulo \033[1;34mEscaleno\033[m')
    else:
        print('Forma um triangulo \033[1;34mIsósceles\033[m')
else:
    print('Nao é possivel formar um triangulo')
