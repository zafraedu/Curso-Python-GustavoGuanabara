from colorama import Fore as Clr, init as colorama_init
colorama_init()

d_error = {
    'option': f'{Clr.RED}ERRO! digite uma opção válida.{Clr.RESET}',
    'archivo': f'{Clr.RED}ERRO! archivo: database.txt não encontrado.{Clr.RESET}',
    'idade': f'{Clr.RED}ERRO! a idade deve ser um valor numérico.{Clr.RESET}'
}

def titulo(txt):
    print('-' * 50)
    print(f'{Clr.RESET}{txt:^50}')
    print('-' * 50)
