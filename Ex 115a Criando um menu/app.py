"""Vamos criar um menu em Python, usando modularização."""

from lib.interface import *

while True:
    resposta = menu(['Criar Arquivo', 'Cadastrar Pessoa', 'Listar Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção válida!')        


