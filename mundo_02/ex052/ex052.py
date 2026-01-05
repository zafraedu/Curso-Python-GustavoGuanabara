n = int(input('Digite um numero: '))

lista = []
for i in range(n, 0, -1):
    if n % i == 0:
        lista.append(i)

if sum(lista) == n + 1:
    print('\033[32mEs primo')
else:
    print('\033[31mNo es primo')
