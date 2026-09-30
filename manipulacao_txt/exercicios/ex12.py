def criar_arquivo():
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;8.5\n")
        arquivo.write("Bruno;5.0\n")
        arquivo.write("Carlos;7.2\n")
        arquivo.write("Daniela;9.0\n")
        arquivo.write("Eduardo;3.5\n")
        arquivo.write("Fernanda;6.8\n")
        arquivo.write("Gabriel;2.0\n")


def classificar_alunos():
    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            nome, nota = linha.strip().split(";")
            nota = float(nota)

            if nota >= 6:
                situacao = "Aprovado"
            elif nota >= 4:
                situacao = "Recuperação"
            else:
                situacao = "Reprovado"

            print(nome, "-", nota, "-", situacao)


criar_arquivo()
classificar_alunos()