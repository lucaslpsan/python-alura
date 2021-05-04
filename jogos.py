import advinhacao
import forca

print("*********************************")
print("*******Bem vindo aos jogos*******")
print("*********************************")

print("Escolha um dos jogos: Advinhação (1) ou Forca (2)")
escolha_do_jogo = int(input("Digite: "))

if (escolha_do_jogo == 1):
    advinhacao.jogar()
elif (escolha_do_jogo == 2):
    forca.jogar()
