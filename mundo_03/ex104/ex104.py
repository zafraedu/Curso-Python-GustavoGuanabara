def leiaInt(txt: str) -> int:
    n = str(input(txt)).strip()
    while not n.isdigit():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        n = str(input(txt)).strip()
    return int(n)


num = leiaInt('Digite um numero: ')
print(num)
