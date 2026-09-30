def criar_arquivo():
    with open("vendas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Ana;Notebook;3500.00\n")
        arquivo.write("Bruno;Mouse;80.00\n")
        arquivo.write("Carlos;Teclado;150.00\n")
        arquivo.write("Ana;Monitor;900.00\n")
        arquivo.write("Daniela;Notebook;3500.00\n")
        arquivo.write("Bruno;Headset;200.00\n")
        arquivo.write("Carlos;Mouse;80.00\n")
        arquivo.write("Ana;Teclado;150.00\n")
        arquivo.write("Daniela;Monitor;900.00\n")


def gerar_relatorio():
    vendas = []

    with open("vendas.txt", "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            vendedor, produto, valor = linha.strip().split(";")

            venda = {
                "vendedor": vendedor,
                "produto": produto,
                "valor": float(valor)
            }

            vendas.append(venda)

    print("VENDAS:")

    for venda in vendas:
        print(
            venda["vendedor"],
            "-",
            venda["produto"],
            "-",
            f"R$ {venda['valor']:.2f}"
        )

    valor_total = 0

    for venda in vendas:
        valor_total += venda["valor"]

    print(f"\nTOTAL DE VENDAS: R$ {valor_total:.2f}")

    quantidade_vendas = {}

    for venda in vendas:
        vendedor = venda["vendedor"]

        if vendedor in quantidade_vendas:
            quantidade_vendas[vendedor] += 1
        else:
            quantidade_vendas[vendedor] = 1

    print("\nQuantidade de vendas:")

    for vendedor, quantidade in quantidade_vendas.items():
        print(f"{vendedor}: {quantidade}")

    total_por_vendedor = {}

    for venda in vendas:
        vendedor = venda["vendedor"]
        valor = venda["valor"]

        if vendedor in total_por_vendedor:
            total_por_vendedor[vendedor] += valor
        else:
            total_por_vendedor[vendedor] = valor

    maior_vendedor = ""
    maior_valor = 0

    for vendedor, valor in total_por_vendedor.items():
        if valor > maior_valor:
            maior_valor = valor
            maior_vendedor = vendedor

    print(
        f"\nMaior valor total em vendas: "
        f"{maior_vendedor} - R$ {maior_valor:.2f}"
    )


criar_arquivo()
gerar_relatorio()