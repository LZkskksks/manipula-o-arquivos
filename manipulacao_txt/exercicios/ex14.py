def gerenciar_tarefas():
    tarefas = []

    # Carregar tarefas existentes
    try:
        with open("tarefas.txt", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                tarefas.append(linha.strip())
    except FileNotFoundError:
        # Cria o arquivo caso ele ainda não exista
        with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
            pass

    while True:
        print("\n1 - Adicionar tarefa")
        print("2 - Listar tarefas")
        print("3 - Remover tarefa")
        print("4 - Sair")

        escolha = input("Escolha: ")

        if escolha == "1":
            tarefa = input("Digite a tarefa: ")
            tarefas.append(tarefa)

            with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
                for tarefa in tarefas:
                    arquivo.write(tarefa + "\n")

            print("Tarefa adicionada!")

        elif escolha == "2":
            print("\nTarefas:")

            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa)

        elif escolha == "3":
            print("\nTarefas:")

            for i, tarefa in enumerate(tarefas, start=1):
                print(i, "-", tarefa)

            numero = int(input("Digite o número da tarefa que deseja remover: "))

            if numero >= 1 and numero <= len(tarefas):
                tarefas.pop(numero - 1)

                with open("tarefas.txt", "w", encoding="utf-8") as arquivo:
                    for tarefa in tarefas:
                        arquivo.write(tarefa + "\n")

                print("Tarefa removida!")
            else:
                print("Número de tarefa inválido!")

        elif escolha == "4":
            print("Programa encerrado.")
            break

        else:
            print("Opção inválida!")


gerenciar_tarefas()
