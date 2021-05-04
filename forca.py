import random


def jogar():
    print_boas_vindas()
    palavra_secreta = obtem_palavra_secreta()
    letras_acertadas = gera_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0
    tentativas = 7

    print(letras_acertadas)

    while(not enforcou and not acertou):
        chute = input("Digite um letra: ").strip().upper()

        if(chute != "" and chute in palavra_secreta):
            letras_acertadas = preenche_letras_acertadas(
                chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1
            print("Você ainda tem {} tentativas".format(tentativas - erros))
            desenha_forca(erros)

        enforcou = erros == tentativas
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print("**************Fim****************")


def print_boas_vindas():
    print("*********************************")
    print("***Bem vindo ao jogo de forca****")
    print("*********************************")


def obtem_palavra_secreta():
    palavras = []

    with open("palavras.txt", "r", encoding="UTF-8") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    palavra_secreta = palavras[random.randrange(0, len(palavras))].upper()

    return palavra_secreta


def gera_letras_acertadas(palavra_secreta):
    # ["_"] * len(palavra_secreta)
    return ["_" for letra in palavra_secreta]


def preenche_letras_acertadas(chute, palavra_secreta, letras_acertadas):
    for index, letra in enumerate(palavra_secreta):
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra

    return letras_acertadas


def imprime_mensagem_vencedor():
    print("\n   Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("\n   Puxa, você foi enforcado!")
    print("   A palavra era {}".format(palavra_secreta))
    print("            _____")
    print("           /     \\")
    print("          | () () |")
    print("           \  ^  /")
    print("            |||||")
    print("            |||||")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


if(__name__ == "__main__"):
    jogar()
