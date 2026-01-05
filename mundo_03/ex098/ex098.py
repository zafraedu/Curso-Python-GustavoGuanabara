from time import sleep

def contador(inicio, fim, paso):
    print('-=' * 20)
    print(f'Contagem de {inicio} ate {fim} de {1 if paso == 0 else paso} em {1 if paso == 0 else paso}')
    print('-='*20)
    if inicio > fim:
        for i in range(inicio, fim - 1, -1 if paso == 0 else -paso):
            print(i, end=' ')
            sleep(0.3)
    else:
        for i in range(inicio, fim + 1, 1 if paso == 0 else paso):
            print(i, end=' ')
            sleep(0.3)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Inicio: ')), int(input('Fim: ')), abs(int(input('Paso: '))))
