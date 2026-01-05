from mundo_03.ex115.utils import titulo, Clr, d_error


def menu_option():
    try:
        option = int(input(f'{Clr.YELLOW}Sua Opção: {Clr.RESET}'))
    except ValueError:
        return 0
    except KeyboardInterrupt:
        print(Clr.GREEN + '3', Clr.RESET)
        return 3
    if option not in (1, 2, 3):
        return 0
    return option


def show_menu():
    titulo('MENU PRINCIPAL')
    print(f'{Clr.LIGHTYELLOW_EX}1{Clr.RESET} - {Clr.BLUE}Ver pessoas cadastradas')
    print(f'{Clr.LIGHTYELLOW_EX}2{Clr.RESET} - {Clr.BLUE}Cadastrar nova Pessoa')
    print(f'{Clr.LIGHTYELLOW_EX}3{Clr.RESET} - {Clr.BLUE}Sair do Sistema')
    print(Clr.RESET, end='')
    print('-' * 50)
