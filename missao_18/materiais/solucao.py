print("=== CONTAGEM REGRESSIVA PARA A DECOLAGEM ===")
for numero in range(5, 0, -1):
    print(numero)
print("DECOLAR!")

resposta = ""
while resposta != "pronto":
    resposta = input("Digite pronto quando sua nave estiver preparada: ").lower()
print("Missão iniciada!")
