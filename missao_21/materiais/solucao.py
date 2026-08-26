import random

def escolher(lista):
    return random.choice(lista)

personagens = ["uma capivara astronauta", "um gato detetive", "uma robô cozinheira"]
lugares = ["na Lua de Gelatina", "em uma biblioteca subterrânea", "numa cidade de nuvens"]
objetos = ["uma chave musical", "um mapa invisível", "uma mochila falante"]

print("=== LABORATÓRIO DE HISTÓRIAS ===")
nome = input("Diga o nome da personagem principal: ")
print("\nEra uma vez " + nome + ", " + escolher(personagens) + ".")
print("Ela viajou " + escolher(lugares) + " procurando " + escolher(objetos) + ".")
print("Depois de testar três ideias, resolveu o mistério com criatividade!")
