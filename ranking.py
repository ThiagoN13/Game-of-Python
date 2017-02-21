from jogo import *
#from play import *

def ranking():
    
    nome = str(input("INFORME SEU NOME PARA COMEÇARMOS: "))
        
    limpaTela()
    print("DICA: O NOME DE UMA LINGUAGEM DE PROGRAMAÇÃO")

    #Inicia o jogo e guarda o retorno de jogadas em play
    play = jogo()


    #Cria o arquivo para ser armazenado o nome de todos os jogadores
    arquivoPlay = open("ranking/listaJogadores.txt", "a", encoding="utf-8")
    arquivoPlay.write(str(play) + ":" + nome + "\n")
    arquivoPlay.close()

    #Ler arquivo com nomes dos jogadores
    arquivoPlay = open("ranking/listaJogadores.txt", "r", encoding="utf-8")
    listaPlay = list(arquivoPlay.readlines())
    listaPlay.sort()
    arquivoPlay.close()

    #Separando score e nome e armazenando em rankGlobal
    rankGlobal = []
    rankGlobal.sort()
    for e in listaPlay:
        rankGlobal.append(e.split(":"))

    #Criando e gravando o ranking em um arquivo
    topFive = open("ranking/topFive.txt", "w", encoding="utf-8")
    for c in range(0, len(rankGlobal)):

        if len(rankGlobal) < 6:
            topFive.writelines("POSIÇÃO: %dº \t\t  JOGADOR: %s \t\t ERROS: %s" % ((c + 1), rankGlobal[c][1].replace("\n", ""), rankGlobal[c][0]) + "\n")

    topFive.close()

#Função que exibe o ranking
def topFive():

    #Cria o arquivo onde será armazenado os nomes dos jogadores
    arquivoTopFive =  open("ranking/topFive.txt", "r", encoding="utf-8")
    #ler o arquivo
    listaTopFive = arquivoTopFive.read()
    print("RANKING DOS TOP 5\n")
    print(listaTopFive)

    
    




