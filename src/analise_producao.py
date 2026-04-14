from estrutura_dados import producoes_laranja

def listar_producoes():

    if not producoes_laranja:
        print("\nNenhuma produção cadastrada.")
        return

    print("\nProduções cadastradas:\n")

    for p in producoes_laranja:

        print("Fazenda:", p["fazenda"])
        print("Cidade:", p["cidade"])
        print("Tipo:", p["tipo_laranja"])
        print("Área:", p["area_hectares"], "hectares")
        print("Árvores:", p["quantidade_arvores"])
        print("Produção:", p["producao_toneladas"], "toneladas")
        print("Perda:", p["perda_percentual"], "%")
        print("Safra:", p["safra"])
        print("-" * 40)


def calcular_perda_total():

    perda_total = 0

    for p in producoes_laranja:
        perda = p["producao_toneladas"] * (p["perda_percentual"] / 100)
        perda_total += perda

    print("\nPerda total estimada:", round(perda_total, 2), "toneladas")


def calcular_produtividade():

    for p in producoes_laranja:

        produtividade = p["producao_toneladas"] / p["area_hectares"]

        print("\nFazenda:", p["fazenda"])
        print("Produtividade:", round(produtividade, 2), "toneladas por hectare")