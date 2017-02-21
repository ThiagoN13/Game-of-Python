#!C:\Users\Thiago\Desktop\Thiago\Curso\Lógica de programação\Portable Python 3.2.5.1\Python-Portable.exe

import time
from jogo import *

#Função que verifica se o número que será inserido é valido caso não seja informá o erro
def valida_faixa_inteiro(selecao, início, fim):
    while True:
        try:
            valor = int(input(selecao))
            if início <= valor <= fim:
                return (valor)
        except ValueError:
            print('VALOR INVÁLIDO, POR FAVOR DIGITE UM NÚMERO ENTRE %d e %d' % (início, fim))

def menuGeral():
    print("=========== GAME OF PYTHON ====================")
    print("=            1. JOGO DA FORCA                 =")
    print("=            2. ACERTE O ALVO                 =")
    print("=            3. PEDRA, PAPEL, TESOURA         =")
    print("=            4. JOGO DA VELHA                 =")
    print("=            5. SAIR                          =")
    print("===============================================")

    return valida_faixa_inteiro('ESCOLHA UM JOGO: ', 0, 5)

while True:
    opção = menuGeral()
    
    if opção == 1:
        from playForca import *
        play()
        
    elif opção == 2:
        from alvo import alvo
        alvo()
        
    elif opção == 3:
        from jokempo import *
        jokempo()

    elif opção == 4:
        from menuVelha import *
        menuVelha()    
        
    elif opção == 5:
        print("BYE, VOLTE SEMPRE !")
        time.sleep(3)
        limpaTela()
        break

