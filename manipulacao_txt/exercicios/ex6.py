def criar_arquivo():
    with open("nomes.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana\n")
        arquivo.write("Bruno\n")
        arquivo.write("Carlos\n")
        arquivo.write("Daniela\n")
        arquivo.write("Eduardo\n")
        arquivo.write("Fernanda\n")
        arquivo.write("Gabriel\n")

def carregar_nomes():
    nomes = []

    with open("nomes.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nomes.append(linha.strip())

    print(nomes)
criar_arquivo()
carregar_nomes()
