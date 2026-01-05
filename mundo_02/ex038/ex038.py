n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

if n1 > n2:
    print(f'O {'\033[33m'}primeiro valor{'\033[m'} é {'\033[34m'}maior{'\033[m'}')
elif n2 > n1:
    print(f'O {'\033[33m'}segundo valor{'\033[m'} é {'\033[34m'}maior{'\033[m'}')
else:
    print(f'{'\033[33m'}Nao existe{'\033[m'} valor maior, os dois sao {'\033[34m'}iguais{'\033[m'}')
