# Crie um programa que leia o nome e o preço de vários produtos.
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

total_compra = producto_barato_precio = productos_caros = 0
producto_barato_nombre = ''

while 1:
    producto_nombre = input('Producto: ')
    producto_precio = float(input('Precio del producto: '))

    total_compra += producto_precio

    if producto_precio > 1000:
        productos_caros += 1

    if producto_precio < producto_barato_precio:
        producto_barato_precio = producto_precio
        producto_barato_nombre = producto_nombre
    else:
        producto_barato_precio = producto_precio

    validation = ' '
    while validation not in 'SsNn':
        validation = input('¿Quieres añadir otro producto? [S/N] ')
    if validation in 'Nn':
        break
    print('#' * 30)

print(f'La compra cuesta: {total_compra}')
print(f'{productos_caros} {'producto' if producto_precio == 1 else 'productos'} cuestan mas de R$1000')
print(f'{producto_barato_nombre} es el producto mas barato')
