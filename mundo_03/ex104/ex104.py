# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(txt: str) -> int:
    n = str(input(txt)).strip()
    while not n.isdigit():
        print('\033[31mERRO! Digite um número inteiro válido.\033[m')
        n = str(input(txt)).strip()
    return int(n)


num = leiaInt('Digite um numero: ')
print(num)