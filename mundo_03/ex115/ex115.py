from time import sleep
from cadastro import select_function
from menu import show_menu, menu_option
from utils import d_error, titulo


def main():
    while True:
        show_menu()
        option = menu_option()
        if option == 3:
            break
        if option in (1, 2):
            select_function(option)
        else:
            print(d_error['option'])
        sleep(1)
    titulo('Saindo do sistema... Até logo!')


main()
