from regras import regrasVelha
from jogo import limpaTela
from velha import jogoVelha
from velha2 import jogoVelha2


def menuVelha():
    while True:

        print("=============== DIGITE: =======================")
        print("=              1. 2 JOGADORES                 =")
        print("=              2. JOGAR SOZINHO               =")
        print("=              3. REGRAS                      =")
        print("=              4. SAIR                        =")
        print("===============================================")
        op = int(input("ESCOLHA UMA OPÇÃO: "))
        limpaTela()

        if op == 1:
            
            jogoVelha()

        if op == 2:

            jogoVelha2()

        elif (op == 3):

            regrasVelha()        
        
        elif (op == 4):
            
            print("BYE, VOLTE SEMPRE !")
            break
            limpaTela()
            
        else:
            
            input('OPÇÃO INVÁLIDA, TECLE ENTAR PARA VOLTAR AO MENU')

menuVelha()
