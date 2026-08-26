def responder(mensagem):
    mensagem = mensagem.lower()
    if "oi" in mensagem:
        return "Oi! Eu sou o chatbot da Base Secreta."
    if "bug" in mensagem:
        return "Bugs são pistas. Vamos testar uma parte por vez?"
    if "jogo" in mensagem:
        return "Meu jogo favorito é inventar aventuras com código!"
    return "Ainda estou aprendendo. Tente falar de bug, jogo ou oi."

print("=== CHATBOT DA BASE SECRETA ===")
print("Digite sair para encerrar.")
while True:
    mensagem = input("Você: ")
    if mensagem.lower() == "sair":
        print("Chatbot: Até a próxima missão!")
        break
    print("Chatbot:", responder(mensagem))
