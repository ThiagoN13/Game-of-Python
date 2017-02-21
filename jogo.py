import subprocess as sp
import random as rd
import os as comandos

#Função limpa a tela do terminal
def limpaTela():
    #Só funciona se executada pelo terminal linux
    #sp.call("clear", shell = True)

    #Outra alternativa para windows
    #comandos.system("cls")

    #Alternativa(Gambiarra) funciona em qualquer console :D
    print("\n" * 100)

#Função ler aquivo e escolhe uma pelavra aleatoria
def palavraAleatoria():
    print("==========DIGITE UM NÚMERO PARA A SELEÇÃO DO TEMA=========")
    print("=         1. LINGUAGEM DE PROGRAMAÇÃO                    =")
    print("=         2. OBJETOS                                     =")
    print("=         3. COMPONENTES DO COMPUTADOR                   =")
    print("=         4. TODOS OS ASSUNTOS                           =")
    print("==========================================================")
    selecao = int(input("INFORME O TEMA: "))

#Estrutura de seleção do tema
    if selecao == 1:
        print("DICA : LINGUAGEM DE PROGRAMAÇÃO")
        arquivo = open('temas/listaPalavras.txt', 'r', encoding='utf-8')
        lista = (arquivo.readlines())
        indice = rd.randint(0, len(lista)-1)
        arquivo.close()
        return lista[indice]

    elif selecao == 2:
        print("DICA : SUBSTANTIVOS")
        arquivo = open('temas/objetos.txt', 'r', encoding='utf-8')
        lista = (arquivo.readlines())
        indice = rd.randint(0, len(lista)-1)
        arquivo.close()
        return lista[indice]

    elif selecao == 3:
        print("DICA : COMPONENTES DE COMPUTADOR")
        arquivo = open('temas/componentes.txt', 'r', encoding='utf-8')
        lista = (arquivo.readlines())
        indice = rd.randint(0, len(lista)-1)
        arquivo.close()
        return lista[indice]

    elif selecao == 4:
        print("DICA : TODOS OS ASSUNTOS")
        arquivo = open('temas/aleatorio.txt', 'r', encoding='utf-8')
        lista = (arquivo.readlines())
        indice = rd.randint(0, len(lista)-1)
        arquivo.close()
        return lista[indice]
    
#Função que inicia o jogo
def jogo():

    palavra = palavraAleatoria().strip()
    #print(palavra)

    #Armazena as letras digitadas
    digitadas = []

    #Armazena as letras que pertecem a palavra
    acertos = []

    #Armazena letras incorretas digitadas
    erros = 0

    #Quantidade de tentativas que o usuário possui
    tentativas = 7

    while True:
        senha = ''
        for letra in palavra:
            senha += letra if letra in acertos else "__ "
        print(senha)
        if senha == palavra:
            limpaTela()
            print("VOCÊ ACERTOU! A PALAVRA É: %s" % (palavra.upper()))
            input("\n\nTELCE ENTER PARA VOLTAR AO MENU")
            limpaTela()
            break
        tentativa = input("\nDIGITE UMA LETRA: ").lower().strip()
        limpaTela()

        if tentativa in digitadas:
            limpaTela()
            print("VOCÊ JÁ TENTOU ESSA LETRA!")
            continue
        else:
            digitadas += tentativa
            if tentativa in palavra:
                acertos += tentativa
            else:
                erros += 1
                tentativas -= 1
                print("VOCÊ ERROU! RESTAM APENAS %d TENTATIVAS" % (tentativas))
        print("X==:==\nX : ")
        print("X  º " if erros >= 1 else "X")
        linha2 = ""
        if erros == 2:
            linha2 = "  | "
        elif erros == 3:
            linha2 = " \| "
        elif erros >= 4:
            linha2 = " \|/ "
        print("x%s" % linha2)
        linha3 = ""
        if erros == 5:
            linha3 += " / "
        elif erros >= 6:
            linha3 += " /°\ "
        print("x%s" % linha3)
        print("X\n========")
        if erros == 6:
            limpaTela()
            print("VOCÊ FOI ENFORCADO ! A PALAVRA É: %s" % (palavra.upper()))
            input("TECLE ENTER PARA VOLTAR AO MENU")
            limpaTela()
            break

    #Depois de ganhar ou perder a função irá retornar a quantidade de jogadas
    jogadas = erros
    return jogadas
