from regras import regrasJokempo
from jokempo import jokempo
from jogo import limpaTela


def menuVelha():
    while True:

        print("=============== DIGITE: =======================")
        print("=              1. JOGAR                       =")
        print("=              2. REGRAS                      =")
        print("=              3. SAIR                        =")
        print("===============================================")
        op = int(input("ESCOLHA UMA OPÇÃO: "))
        limpaTela()

        if op == 1:
            
            jokempo()

        if op == 2:

            regrasJokempo()

        elif (op == 3):

            print("BYE, VOLTE SEMPRE !")
            break
            limpaTela()       
            
        else:
            
            input('OPÇÃO INVÁLIDA, TECLE ENTAR PARA VOLTAR AO MENU')

menuVelha()
