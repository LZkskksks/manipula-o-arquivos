def criar_arquivo():
    frase = input("Digite uma frase: ")

    with open("frase.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write(frase)

    print("Arquivo criado com sucesso!")


criar_arquivo()
