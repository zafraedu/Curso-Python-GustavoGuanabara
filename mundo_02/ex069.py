# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.


edades_maior = homens = mulher_menor = 0
while 1:

    edade = int(input('edade: '))
    if edade > 18:
        edades_maior += 1

    sexo = input('sexo [Masculino/Femenino]: ').lstrip()
    if sexo[0].lstrip() in 'Mm':
        homens += 1

    if sexo[0].lstrip() in 'Mm' and edade < 20:
        mulher_menor += 1

    next = input('Quer continuar? [S/N]: ')
    if next.lstrip() in 'Nn':
        break
    print('='*80)
print(f'A) {edades_maior} {'pessoa' if edades_maior == 1 else 'pessoas'} tem mais de 18 anos')
print(f'B) {homens} {'homen' if homens == 1 else 'homens'} foram cadastrados')
print(f'C) {mulher_menor} {'mulher' if mulher_menor == 1 else 'mulheres'} sao menores a 20 anos')
