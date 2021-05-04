import random


def jogar():

    print("*********************************")
    print("Bem vindo ao jogo de adivinhação")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)  # 42
    numero_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade")
    print("(1) fácil (2) médio (3) difícil")
    nivel = int(input("Digite o nível: "))

    print("*********************************")

    if (nivel == 1):
        numero_de_tentativas = 10
    elif (nivel == 2):
        numero_de_tentativas = 7
    else:
        numero_de_tentativas = 3

    for rodadas in range(1, numero_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodadas, numero_de_tentativas))

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou: ", chute)
        if (chute < 1 or chute > 100):
            continue

        if (chute == numero_secreto):
            print("Você acertou e fez {} pontos.".format(pontos))
            break
        elif (chute > numero_secreto):
            print("Você errou! Seu número é maior.")
        else:
            print("Voce errou! Seu número é menor")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

        print("*********************************")


if(__name__ == "__main__"):
    jogar()
