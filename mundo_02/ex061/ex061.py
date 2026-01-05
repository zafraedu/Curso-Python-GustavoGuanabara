primeiro_termo = int(input('Primeiro termo da progressão aritmética: '))
razao = int(input('Razão da progressão aritmética: '))
decimo = primeiro_termo + (10 - 1) * razao

while primeiro_termo <= decimo:
    print(primeiro_termo, end = ' ')
    primeiro_termo += razao
