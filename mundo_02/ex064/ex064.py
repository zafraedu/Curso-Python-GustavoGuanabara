count = 0
n = int(input('Digite um numero [999 para parar]: '))
result = 0
while n != 999:
    if n != 999:
        result += n
        count += 1
    n = int(input('Digite um numero [999 para parar]: '))
print(f'{count} numeros foram digitados e a soma entre todos da {result}')
