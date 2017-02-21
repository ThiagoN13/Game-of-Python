from jogo import limpaTela
import time
import random as rd

limpaTela()
print("===================================================")
print("\n")
print("======= TECLE ENTER PARA COMEÇAR O JOGO ! =========")
print("\n")
print("===================================================")
input()
limpaTela()


def jogoVelha2():
    #Função que verifica se alguem ganhou
    def resultado(tabela, jogadas, nome1):
        combinacoes = [[tabela[1], tabela[2], tabela[3]], 
                       [tabela[4], tabela[5], tabela[6]], 
                       [tabela[7], tabela[8], tabela[9]],
                        #Horizontal
                       [tabela[1], tabela[4], tabela[7]],
                       [tabela[2], tabela[5], tabela[8]],
                       [tabela[3], tabela[6], tabela[9]],
                        #Verical
                       [tabela[1], tabela[5], tabela[9]],
                       [tabela[3], tabela[5], tabela[7]]]
        
        #Verificação do jogador vencedor
        for i in range(0, len(combinacoes)):
            
            if combinacoes[i][0] == "X" and combinacoes[i][1] == "X" and combinacoes[i][2] == "X":
                print("O JOGADOR %s GANHOU!" % (nome1))
                break
            elif combinacoes[i][0] == "O" and combinacoes[i][1] == "O" and combinacoes[i][2] == "O":
                print("O COMPUTADOR GANHOU!")
                break

            elif len(jogadas) == 9:
                print("DEU VELHA!")
                break
            if i == (len(combinacoes)-1):
                return True

    nome1 = input("JOGADOR 1 INFORME SEU NOME: ").upper()

    #Variavel que guarda as posições a serem preenchidas
    tabela = [None ," "," "," "," "," "," "," "," "," "]
    jogadas = []
    #Função no qual estará o tabuleiro do jogo
    def tabuleiro():

        mesa = """                     Posições
             %s  | %s | %s     1 | 2 | 3  
             ---+---+---   ---+---+---
             %s  | %s | %s     4 | 5 | 6 
             ---+---+---   ---+---+---
             %s  | %s | %s     7 | 8 | 9  
            """ % (tabela[1],tabela[2],tabela[3],tabela[4],tabela[5],tabela[6],
                      tabela[7],tabela[8],tabela[9])
        print(mesa)
                  
    while True:
        tabuleiro()
        #verifica se a jogada do player 1 é válida
        while bool(resultado(tabela,jogadas,nome1)) == True:
            if bool(resultado(tabela,jogadas,nome1)) == True:
                jogador1 = int(input("%s SUA VEZ: " % (nome1)))
                if tabela[jogador1] == " ":
                    tabela[jogador1] = "X"
                    jogadas.append(jogador1)
                    tabuleiro()
                    break
                else:
                    print("JOGADA INVALIDA")
            else:
                break
        if bool(resultado(tabela,jogadas,nome1)) == False:
            break
            
      
            #verifica se a jogada do player 2 é válida
        while bool(resultado(tabela,jogadas,nome1)) == True:

            if bool(resultado(tabela, jogadas, nome1)) == True:
                jogador2 = rd.randint(0, 9)
                if tabela[jogador2] == " ":
                    tabela[jogador2] = "O"
                    jogadas.append(jogador2)
                    limpaTela()
                    tabuleiro()
                    break
            else:
                break

        if bool(resultado(tabela, jogadas, nome1)) == False:
            break


    #Estrutura para jogar novamente    
    op = input("DESEJA JOGAR NOVAMENTE S/N: ").upper()

    if op == "S":
        
        jogoVelha()
        
    else:
       
        print("BYE, VOLTE SEMPRE !")
        time.sleep(3)
        limpaTela()
    
