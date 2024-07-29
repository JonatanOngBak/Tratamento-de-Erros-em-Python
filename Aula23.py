#print(x)   # NameError: name 'x' is not defined

# erros são EXCEÇÃO / Exception  

#n = int(input('Número: '))
#print(f'Você didigitou o número {n}') # oito = ValueError: invalid literal for int()

#a = int(input('Númerador: '))
#b = int(input('Denominador: '))  # 8 / 0 = ZeroDivisionError: division by zero
#r = a / b                        # foi uma exceçao
#print(f'O resultado é {r}')

#r = 2/'2'  # erro do tipo TypeError

#lst = [3, 6, 4]  # IndexError: list index out of range
#      0, 1, 2   indices      
#print(lst[3])    # o indice 3 não existe nesta lista


#import uteis # ModuleNotFoundError: No module named 'uteis'
             # modulo não encontrado


# O comando 
#   try:
        # operação                        # é otimo 
                                          # tente fazer algo se não mostre a exceção
#   except:                               # um mesmo try pode ter varios except um para cada codigo de erro
        # falhou

#   else:
        # deu certo
#   finally
        # deu certo / não   isso sempre sera executado

try:
    a = int(input('Númerador: '))
    b = int(input('Denominador: '))  
    r = a / b 
except (ValueError, TypeError):
    print(f'\033[31mTivemos um problema com os tipos que você digitou\033[m')
except ZeroDivisionError:
    print(f'\033[31mNão é possivel dividir um número por zero\033[m') 
except KeyboardInterrupt:
    print('O usuario preferiu não informar os dados')   
except Exception as erro:
    print(f'O erro encontrado foi {erro.__cause__}')      

else:
    print(f'O resultado foi {r:.2f}')
finally:
    print('\033[32mVolte sempre muito obrigado\033[m')     


