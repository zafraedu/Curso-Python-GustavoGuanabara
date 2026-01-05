from colorama import Fore

n1 = int(input('Number 1: '))
n2 = int(input('Number 2: '))
n3 = int(input('Number 3: '))

numeros = [n1, n2, n3]
print(f'Maior: {Fore.YELLOW}{max(numeros)}{Fore.RESET}')
print(f'Menor: {Fore.YELLOW}{min(numeros)}{Fore.RESET}')

# nma = n1
# if nma < n2:
#     nma = n2
# if nma < n3:
#     nma = n3
#
# nmi = n1
# if nmi > n2:
#     nmi = n2
# if nmi > n3:
#     nmi = n3
#
# print(f'Maior: {nma}')
# print(f'Menor: {nmi}')
