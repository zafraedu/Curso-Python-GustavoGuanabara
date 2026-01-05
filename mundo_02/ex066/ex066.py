count = soma = 0
while 1:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    soma += n
    count += 1
print(f'{count} numeros foram digitados, e a soma total é {soma}')
