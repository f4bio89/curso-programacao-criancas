print("=== COFRE DOS NÚMEROS ===")
chave = int(input("Digite um número de 1 a 10: "))
if chave == 0:  # TROQUE 0 PELA CHAVE SECRETA
    print("Cofre aberto! Você encontrou um adesivo de Caçadora de Bugs!")
else:
    print("Ainda não. Encontramos uma pista: tente outro número.")
