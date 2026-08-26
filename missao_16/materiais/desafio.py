import random

missoes = ["desenhar um robô", "inventar um planeta", "contar uma piada", "fazer pose de heroína", "procurar algo azul"]
print("=== DADO DAS AVENTURAS ===")
input("Aperte Enter para lançar o dado...")
numero = random.randint(1, 6)
print("Você tirou:", numero)
print("Missão sorteada:", random.choice(missoes))
