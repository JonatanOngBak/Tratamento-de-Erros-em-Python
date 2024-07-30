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


def leiaReal(msg):   
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('\033[31mERRO: por favor, digite um número inteiro.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31m\nERRO: Usuario preferio não digitar o valor\033[m')
            return 0
        else:
            return n    

num = leiaInt('Digite um valor inteiro: ')
num2 = leiaReal('Digite um valor Real')
print(f'O valor inteiro foi {num} e o Real foi {num2}')