#Função no qual irá ler todas as linhas e imprimir na tela 
def regras():
    regras = open("regras/regras.txt", "r")
    for linha in regras.readlines():
        print(linha)

def regrasVelha():
    regras = open("regras/regrasVelha.txt", "r")
    for linha in regras.readlines():
        print(linha)

def regrasJokempo():
    regras = open("regras/regrasJokempo.txt", "r")
    for linha in regras.readlines():
        print(linha)
