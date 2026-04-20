import json
from estrutura_dados import produtores, lavouras


# ===============================
# CARREGAR PRODUTORES
# ===============================

def carregar_produtores():

    try:

        with open("dados/produtores.json", "r", encoding="utf-8") as arquivo:

            dados = json.load(arquivo)

            produtores.extend(dados)

    except FileNotFoundError:

        print("Arquivo produtores.json não encontrado.")


# ===============================
# SALVAR PRODUTORES
# ===============================

def salvar_produtores():

    with open("dados/produtores.json", "w", encoding="utf-8") as arquivo:

        json.dump(produtores, arquivo, indent=4, ensure_ascii=False)


# ===============================
# CARREGAR LAVOURAS
# ===============================

def carregar_lavouras():

    try:

        with open("dados/lavoura.json", "r", encoding="utf-8") as arquivo:

            dados = json.load(arquivo)

            lavouras.extend(dados)

    except FileNotFoundError:

        print("Arquivo lavoura.json não encontrado.")


# ===============================
# SALVAR LAVOURAS
# ===============================

def salvar_lavouras():

    with open("dados/lavoura.json", "w", encoding="utf-8") as arquivo:

        json.dump(lavouras, arquivo, indent=4, ensure_ascii=False)