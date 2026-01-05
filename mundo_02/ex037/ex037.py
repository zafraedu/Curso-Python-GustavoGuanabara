n = int(input('Number: '))

op = input('''
    \033[1mEscolha um método para conversao:\033[m 
    
    \033[34m1\033[m - \033[33mBinário\033[m
    \033[34m2\033[m - \033[33mOctal\033[m
    \033[34m3\033[m - \033[33mHexadecimal\033[m

    ''')

if op == '1':
    print(f'{n} in binary is {'\033[1m'}{str(bin(n)[2:])}{'\033[m'}')
elif op == '2':
    print(f'{n} in octal is {'\033[1m'}{str(oct(n)[2:])}{'\033[m'}')
elif op == '3':
    print(f'{n} in hexadecimal is {'\033[1m'}{str(hex(n)[2:])}{'\033[m'}')
else:
    print('Esta nao é uma opção valida, adeus ;)')
