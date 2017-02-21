import random as rd
from jogo import *
import time

limpaTela()
print("===================================================")
print("\n")
print("======= TECLE ENTER PARA COMEÇAR O JOGO ! =========")
print("\n")
print("===================================================")
input()
limpaTela()

def alvo():
    print("ACERTE O ALVO DE 1 Á 100")
    #Gera o alvo
    indice = rd.randint(1, 100)
    nome = input("DIGITE SEU NOME: ")
    limpaTela()
    #Contador de tentativas
    tentativa = 0

    
    while True:

        jogada = int(input("DIGITE UM NÚMERO: "))

        if jogada > indice:
            print("INFORME UM NÚMERO MENOR")
            tentativa +=1

        if jogada < indice:
            print("INFORME UM NÚMERO MAIOR")
            tentativa +=1
            
        elif jogada == indice:
            tentativa +=1
            limpaTela()
            print("PARABÉNS %s VOCÊ ACERTOU O ALVO ERA: %s COM %d TENTATIVAS " %(nome, indice, tentativa))
            break

    #Estrutura para jogar novamente    
    op = input("DESEJA JOGAR NOVAMENTE S/N: ").upper()

    if op == "S":
        
        alvo()
        
    else:

        print("BYE, VOLTE SEMPRE !")
        time.sleep(3)
        limpaTela()
        
