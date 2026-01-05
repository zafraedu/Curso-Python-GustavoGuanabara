# Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai
# aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.

def clr(cor=''):
    """
    Mostrar cor pela tela
    :param cor: cor en ascii
    :return: A cor
    """
    print('\033[' + cor + 'm', end='')


def titulo(cmd, final=False):
    """
    imprime o titulo ou o fina com cores
    :param cmd: comando para o título.
    :param final: foot del programa
    :return: header ou foot
    """
    if not final:
        clr('1;44')
        txt = f'    Acessando o manual do comando \'{cmd}\''
    else:
        clr('1;42')
        txt = f'    SISTEMA DE AJUDA PyHELP'
    print(f'{'-' * (len(txt) + 4)}\n'
          f'{txt}\n'
          f'{'-' * (len(txt) + 4)}')
    clr()


comando = str(input('Função ou Biblioteca > ')).strip().upper()
while comando != 'FIM':
    titulo(comando)
    clr('7')
    help(comando)
    clr()
    titulo(comando, True)
    comando = str(input('\033[mFunção ou Biblioteca > ')).strip()
