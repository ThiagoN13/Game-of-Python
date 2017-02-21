from jogo import limpaTela
from ranking import *
from regras import regras


limpaTela()
print("===================================================")
print("\n")
print("======= TECLE ENTER PARA COMEÇAR O JOGO ! =========")
print("\n")
print("===================================================")
input()
limpaTela()


def menu():
    while True:

        print("=============== DIGITE: =======================")
        print("=              1. JOGAR                       =")
        print("=              2. RAKING                      =")
        print("=              3. REGRAS                      =")
        print("=              4. SAIR                        =")
        print("===============================================")
        op = int(input("ESCOLHA UMA OPÇÃO: "))
        limpaTela()

        if op == 1:
            
            ranking()

        if op == 2:

            topFive()
            input("TECLE ENTER PARA VOLTAR AO MENU")
            limpaTela()

        elif (op == 3):

            regras()        
        
        elif (op == 4):
            
            print("BYE, VOLTE SEMPRE !")
            break
            limpaTela()
            
        else:
            
            input('OPÇÃO INVÁLIDA, TECLE ENTAR PARA VOLTAR AO MENU')

menu()
