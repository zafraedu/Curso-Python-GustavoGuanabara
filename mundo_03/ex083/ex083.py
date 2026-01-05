expressao = str(input('Digite uma expressão: ')).replace(' ', '')
lista = list()
for i in expressao:
    if i == '(':
        lista.append(i)
    elif i == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(i)
            break

if not lista:
    print('A expressão é valida')
else:
    print('A expressão nao é valida')
