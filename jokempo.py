import random as rd
from jogo import limpaTela
import time

limpaTela()
print("===================================================")
print("\n")
print("======= TECLE ENTER PARA COMEÇAR O JOGO ! =========")
print("\n")
print("===================================================")
input()
limpaTela()

def jokempo():
    nome = input("INFORME SEU NOME: ").upper()
    limpaTela()
    while True:
        #Lista da jogada a ser escolhida
        lista = [None, "PEDRA", "PAPEL", "TESOURA"]

        #Gerar indice aleatorio 
        indice = rd.randint(1, 3)
        
        #Define jogada do computador
        maquina = lista[indice]

        #Jogada definida pelo usuario
        print("=============== ESCOLHA: ======================")
        print("=              1. PEDRA                       =")
        print("=              2. PAPEL                       =")
        print("=              3. TESOURA                     =")
        print("===============================================")
        
        jogada = int(input("ESCOLHA UMA OPÇÃO: "))
         
        #Define jogada do usuario
        jogador = lista[jogada]

        print(nome,": ", jogador)
        print("COMPUTER: ", maquina)
        
        #Se a jogada for igual ao indice dará empate
        if jogada == indice:
            print("EMPATE!!!")

        # Verificando qual jogada vencedora (eu tava tentando resumir o maximo de codigo kk)    
        if jogador == "PAPEL" and maquina == "TESOURA" or maquina == "PEDRA" and jogador == "TESOURA" or maquina == "PAPEL" and jogador == "PEDRA":
            print("VOCÊ PERDEU")
            break
        
        if jogador == "TESOURA" and maquina == "PAPEL" or maquina == "TESOURA" and jogador == "PEDRA" or maquina == "PEDRA" and jogador == "PAPEL":
            print(nome,"WINS")
            break

    #Estrutura para jogar novamente    
    op = input("DESEJA JOGAR NOVAMENTE S/N: ").upper()

    if op == "S":
        
        joguinho()
        
    else:
       
        print("BYE, VOLTE SEMPRE !")
        time.sleep(3)
        limpaTela()







            
