def criar_arquivo():
    with open("numeros.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("10\n")
        arquivo.write("15\n")
        arquivo.write("22\n")
        arquivo.write("31\n")
        arquivo.write("40\n")
        arquivo.write("55\n")
        arquivo.write("68\n")
        arquivo.write("73\n")
        arquivo.write("80\n")
        arquivo.write("91\n")


def mostrar_numeros():
    numeros = []

    with open("numeros.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            numeros.append(int(linha.strip()))

    for numero in numeros:
        if numero % 2 == 0:
            print(numero)


criar_arquivo()
mostrar_numeros()