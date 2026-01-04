num = str(input('Número de 0 a 9999: ')).lstrip()

# num = int(num) # best code
# u = num // 1 % 10
# d = num // 10 % 10
# c = num // 100 % 10
# m = num // 1000 % 10

u = str(int(num) / 10)
d = str(int(num) / 100)
c = str(int(num) / 1000)
m = str(int(num) / 10000)


print(f'unidade: {u[u.find('.') + 1]}')
print(f'dezena: {d[d.find('.') + 1]}')
print(f'centena: {c[c.find('.') + 1]}')
print(f'milhar: {m[m.find('.') + 1]}')
