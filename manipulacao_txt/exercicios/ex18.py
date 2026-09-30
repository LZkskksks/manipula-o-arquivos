def criar_arquivo():
    with open("notas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;8.5;7.0;9.0\n")
        arquivo.write("Bruno;5.0;6.0;4.5\n")
        arquivo.write("Carlos;7.5;8.0;9.0\n")
        arquivo.write("Daniela;9.0;9.5;10.0\n")
        arquivo.write("Eduardo;4.0;5.0;3.5\n")
        arquivo.write("Fernanda;6.5;7.0;8.0\n")


def gerenciar_notas():
    alunos = []

    with open("notas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            nome = dados[0]
            nota1 = float(dados[1])
            nota2 = float(dados[2])
            nota3 = float(dados[3])

            aluno = {
                "nome": nome,
                "nota1": nota1,
                "nota2": nota2,
                "nota3": nota3
            }

            alunos.append(aluno)

    for aluno in alunos:
        media = (
            aluno["nota1"] +
            aluno["nota2"] +
            aluno["nota3"]
        ) / 3

        if media >= 6:
            situacao = "Aprovado"
        else:
            situacao = "Reprovado"

        print(f"{aluno['nome']} - Média: {media:.2f} - {situacao}")


criar_arquivo()
gerenciar_notas()