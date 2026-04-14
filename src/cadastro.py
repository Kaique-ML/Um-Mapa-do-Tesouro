from estrutura_dados import producoes_laranja, tipos_laranja

def cadastrar_producao():
    
    print("\nCadastro de Produção de Laranja\n")

    fazenda = input("Nome da fazenda: ")
    cidade = input("Cidade: ")

    try:
        area = float(input("Área plantada (hectares): "))
        arvores = int(input("Quantidade de árvores: "))
        producao = float(input("Produção estimada (toneladas): "))
        perda = float(input("Perda estimada (%): "))
        safra = int(input("Ano da safra: "))
    except ValueError:
        print("Erro: Digite apenas valores numéricos válidos.")
        return

    print("\nTipos de laranja disponíveis:")
    for i, tipo in enumerate(tipos_laranja):
        print(i + 1, "-", tipo)

    escolha = int(input("Escolha o tipo de laranja: "))

    if escolha < 1 or escolha > len(tipos_laranja):
        print("Tipo inválido.")
        return

    tipo_laranja = tipos_laranja[escolha - 1]

    registro = {
        "fazenda": fazenda,
        "cidade": cidade,
        "area_hectares": area,
        "quantidade_arvores": arvores,
        "tipo_laranja": tipo_laranja,
        "producao_toneladas": producao,
        "perda_percentual": perda,
        "safra": safra
    }

    producoes_laranja.append(registro)

    print("\nProdução cadastrada com sucesso.")