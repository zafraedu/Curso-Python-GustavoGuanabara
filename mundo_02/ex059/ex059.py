option = '4'
n1 = 0
n2 = 0
while option[0] in '1234':
    n1 = int(n1)
    n2 = int(n2)
    if option == '1':
        print('soma:', n1 + n2)
        option = '0'

    elif option == '2':
        print('multiplicar:', n1 * n2)
        option = '0'

    elif option == '3':
        print('maior:', n1 if n1 > n2 else n2)
        option = '0'

    elif option == '4':
        n1 = input('Primeiro valor: ')
        while not n1.isnumeric():
            n1 = input('\033[31merror: first value is not a number\033[m\n'
                       'Digite um numero, por favor: ')

        n2 = input('Segundo valor: ')
        while not n2.isnumeric():
            n2 = input('\033[31merror: second value is not a number\033[m\n'
                       'Digite um numero, por favor: ')
        option = '0'

    print('=' * 60)

    if option == '0':
        option = input('[ 1 ] somar\n'
                       '[ 2 ] multiplicar\n'
                       '[ 3 ] maior\n'
                       '[ 4 ] novos numeros\n'
                       '[ 5 ] sair do programa\n')
        while not option[0] in '12345':
            option = input('\033[1;33mDigite uma das opiçoes abaixo\033[m\n'
                           '[ 1 ] somar\n'
                           '[ 2 ] multiplicar\n'
                           '[ 3 ] maior\n'
                           '[ 4 ] novos numeros\n'
                           '[ 5 ] sair do programa\n')
