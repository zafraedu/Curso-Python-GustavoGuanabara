idades_maior = homens = mulher_menor = 0
while 1:

    idade = int(input('idade: '))
    if idade > 18:
        idades_maior += 1

    sexo = input('sexo [Masculino/Femenino]: ').lstrip()
    if sexo[0].lstrip() in 'Mm':
        homens += 1

    if sexo[0].lstrip() in 'Mm' and idade < 20:
        mulher_menor += 1

    next = input('Quer continuar? [S/N]: ')
    if next.lstrip() in 'Nn':
        break
    print('='*80)
print(f'A) {idades_maior} {'pessoa' if idades_maior == 1 else 'pessoas'} tem mais de 18 anos')
print(f'B) {homens} {'homem' if homens == 1 else 'homens'} foram cadastrados')
print(f'C) {mulher_menor} {'mulher' if mulher_menor == 1 else 'mulheres'} sao menores a 20 anos')
