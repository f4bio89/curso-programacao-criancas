print("=== AVENTURA DAS ESCOLHAS ===")
print("Você chegou a uma floresta. Há uma ponte e uma caverna.")
escolha = input("Você escolhe ponte ou caverna? ").lower()
if escolha == "ponte":
    print("Você atravessou com cuidado e encontrou um mapa brilhante!")
elif escolha == "caverna":
    print("Você encontrou um dragão amigável que adora charadas!")
else:
    print("Você inventou um terceiro caminho e descobriu um jardim secreto!")
