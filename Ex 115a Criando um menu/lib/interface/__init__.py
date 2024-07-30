def leiaInt(msg):   
    while True:
        try:
            n = int(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO: por favor, digite um número inteiro.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31m\nERRO: Usuario preferio não digitar o valor\033[m')
            return 0
        else:
            return n 


def linha(tam = 42):
    return '-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1
    print(linha())
    opc = leiaInt('Sua Opção: ')
    return opc    