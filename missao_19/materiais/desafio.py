import random

opcoes = ["pedra", "papel", "tesoura"]
pontos = 0
print("=== PEDRA, PAPEL, TESOURA TURBO ===")
while True:
    jogador = input("Escolha pedra, papel, tesoura ou sair: ").lower()
    if jogador == "sair":
        break
    if jogador not in opcoes:
        print("Não entendi essa jogada.")
        continue
    computador = random.choice(opcoes)
    print("Computador escolheu", computador)
    if jogador == computador:
        print("Empate!")
    elif (jogador == "pedra" and computador == "tesoura") or (jogador == "papel" and computador == "pedra") or (jogador == "tesoura" and computador == "papel"):
        pontos = pontos + 1
        print("Você ganhou esta rodada! Pontos:", pontos)
    else:
        print("O computador ganhou esta rodada. Pontos:", pontos)
print("Fim. Sua pontuação foi", pontos)
