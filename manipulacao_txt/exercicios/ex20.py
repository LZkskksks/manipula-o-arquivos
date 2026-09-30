def criar_arquivo():
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("1;Ana Silva;17;Desenvolvimento de Sistemas\n")
        arquivo.write("2;Bruno Souza;18;Desenvolvimento de Sistemas\n")
        arquivo.write("3;Carlos Oliveira;17;Desenvolvimento de Sistemas\n")
        arquivo.write("4;Daniela Santos;18;Desenvolvimento de Sistemas\n")
        arquivo.write("5;Eduardo Lima;17;Desenvolvimento de Sistemas\n")


def carregar_alunos():
    alunos = []

    with open("alunos.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            id, nome, idade, curso = linha.strip().split(";")

            aluno = {
                "id": int(id),
                "nome": nome,
                "idade": int(idade),
                "curso": curso
            }

            alunos.append(aluno)

    return alunos


def salvar_alunos(alunos):
    with open("alunos.txt", "w", encoding="utf-8") as arquivo:
        for aluno in alunos:
            arquivo.write(
                f"{aluno['id']};"
                f"{aluno['nome']};"
                f"{aluno['idade']};"
                f"{aluno['curso']}\n"
            )


def listar_alunos(alunos):
    print("\n===== LISTA DE ALUNOS =====")

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(
                f"{aluno['id']} - "
                f"{aluno['nome']} - "
                f"{aluno['idade']} anos"
            )


def buscar_aluno(alunos):
    id_busca = int(input("Digite o ID: "))

    for aluno in alunos:
        if aluno["id"] == id_busca:
            print("\nAluno encontrado:")
            print(aluno["nome"])
            print(f"{aluno['idade']} anos")
            print(aluno["curso"])
            return

    print("Aluno não encontrado!")


def cadastrar_aluno(alunos):
    novo_id = 1

    if len(alunos) > 0:
        novo_id = max(aluno["id"] for aluno in alunos) + 1

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    curso = input("Digite o curso: ")

    aluno = {
        "id": novo_id,
        "nome": nome,
        "idade": idade,
        "curso": curso
    }

    alunos.append(aluno)
    salvar_alunos(alunos)

    print("Aluno cadastrado com sucesso!")
    print(f"ID do aluno: {novo_id}")


def remover_aluno(alunos):
    id_remover = int(input("Digite o ID do aluno que deseja remover: "))

    for aluno in alunos:
        if aluno["id"] == id_remover:
            alunos.remove(aluno)
            salvar_alunos(alunos)

            print("Aluno removido com sucesso!")
            return

    print("Aluno não encontrado!")


def alterar_aluno(alunos):
    id_alterar = int(input("Digite o ID do aluno que deseja alterar: "))

    for aluno in alunos:
        if aluno["id"] == id_alterar:
            print("\nAluno encontrado!")

            novo_nome = input("Digite o novo nome: ")
            nova_idade = int(input("Digite a nova idade: "))
            novo_curso = input("Digite o novo curso: ")

            aluno["nome"] = novo_nome
            aluno["idade"] = nova_idade
            aluno["curso"] = novo_curso

            salvar_alunos(alunos)

            print("Aluno alterado com sucesso!")
            return

    print("Aluno não encontrado!")


def sistema_alunos():
    alunos = carregar_alunos()

    while True:
        print("\n===== SISTEMA DE ALUNOS =====")
        print("1 - Listar alunos")
        print("2 - Buscar aluno")
        print("3 - Cadastrar aluno")
        print("4 - Remover aluno")
        print("5 - Alterar aluno")
        print("6 - Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            listar_alunos(alunos)

        elif escolha == "2":
            buscar_aluno(alunos)

        elif escolha == "3":
            cadastrar_aluno(alunos)

        elif escolha == "4":
            remover_aluno(alunos)

        elif escolha == "5":
            alterar_aluno(alunos)

        elif escolha == "6":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


criar_arquivo()
sistema_alunos()