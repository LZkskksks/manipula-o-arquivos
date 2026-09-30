def adicionar_frase():
    frase = input("Digite uma frase: ")

    with open("frases.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(frase + "\n")

    print("Frase adicionada com sucesso!")


adicionar_frase()
