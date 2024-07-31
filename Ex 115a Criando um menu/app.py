"""Vamos criar um menu em Python, usando modularização."""

from lib.interface import *
from lib.Arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)   

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema'])
    if resposta == 1:
        # opcão de listar o conteudo de um arquivo!
        lerAquivo(arq)
    elif resposta == 2:
        cabeçalho('Opção 2')
    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m') 
    sleep(2)
