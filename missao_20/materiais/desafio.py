import random

def resposta_magica(pergunta):
    respostas = ["Troque esta resposta por uma sua!", "Sim, experimente!", "Talvez. Procure outra pista.", "Pergunte de novo depois de um lanche.", "Com certeza, se você testar!", "O bug ainda está pensando."]
    return random.choice(respostas)

print("=== BOLA 8 MÁGICA GENTIL ===")
pergunta = input("Faça uma pergunta divertida: ")
print("Pergunta recebida:", pergunta)
print("Bola 8 diz:", resposta_magica(pergunta))
