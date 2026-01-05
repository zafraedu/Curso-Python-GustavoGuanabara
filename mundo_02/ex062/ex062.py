termo = int(input('Primeiro termo da progressao aritimetica: '))
razao = int(input('Razao da progressao aritimetica: '))
final_termo = 10
count = 0

while final_termo != 0:
    final_razao = termo + (final_termo - 1) * razao
    while termo <= final_razao:
        print(termo, end=' ')
        termo += razao
        count += 1
    final_termo = int(input('\nQuantos termos vc quer mostrar a mais?: '))

print(count)
