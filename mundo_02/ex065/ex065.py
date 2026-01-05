from statistics import mean

validation = 'S'
n_maior = 0
n_menor = 0
lista= []
while validation[0].upper() == 'S':
    n = int(input('Digite um numero: '))
    lista.append(n)
    validation = input('Quer continuar? [S/N] ')

print(f'A média entre todos os numeros é de {mean(lista)}')
print(f'O maior numero digitado foi {max(lista)}')
print(f'O menor numero digitado for {min(lista)}')
