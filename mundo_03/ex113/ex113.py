def leia_int(txt: str):
    while True:
        try:
            n = int(input(txt))
        except ValueError:
            print('\033[31mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu nao digitar nenhum numero.\033[m')
            exit(1)
        else:
            break
    return n


def leia_float(txt: str):
    while True:
        try:
            n = float(input(txt))
        except ValueError:
            print('\033[31mERRO: por favor, digite um número Real válido.\033[m')
        except KeyboardInterrupt:
            print('\n\033[31mUsuário preferiu nao digitar o numero Real.\033[m')
            return 0
        else:
            break
    return n


i = leia_int('Digite um Inteiro: ')
f = leia_float('Digite um Real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {f}')
