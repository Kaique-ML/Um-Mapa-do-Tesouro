# Importe a função do arquivo banco_oracle.py
from banco_oracle import inserir_produtor 

from estrutura_dados import (
    adicionar_produtor,
    adicionar_lavoura,
    adicionar_colheita,
    listar_produtores,
    listar_lavouras,
    listar_colheitas
)

# =====================================================
# CADASTRAR PRODUTOR
# =====================================================

def cadastrar_produtor():
    print("\n===== Cadastro de Produtor (Cana-de-açúcar) =====\n")

    try:
        id_produtor = int(input("ID do produtor: "))
        nome = input("Nome do produtor: ")
        fazenda = input("Nome da fazenda: ")
        latitude = float(input("Latitude: "))
        longitude = float(input("Longitude: "))
    except ValueError:
        print("Erro: valores inválidos.")
        return

    # 1. Salva na estrutura de dados local (Lista)
    adicionar_produtor(id_produtor, nome, fazenda, latitude, longitude)

    # 2. SALVA NO BANCO ORACLE 
    # Isso garante que os dados persistam mesmo se o programa fechar
    print("Enviando dados para o banco de dados Oracle...")
    inserir_produtor(id_produtor, nome, fazenda, latitude, longitude)

    print("\nProdutor cadastrado com sucesso em todos os sistemas.")


# =====================================================
# CADASTRAR LAVOURA
# =====================================================

def cadastrar_lavoura():

    print("\n===== Cadastro de Lavoura =====\n")

    try:
        id_lavoura = int(input("ID da lavoura: "))
        produtor_id = int(input("ID do produtor: "))
        cultura = input("Cultura plantada: ")
        area = float(input("Área plantada (hectares): "))
    except ValueError:
        print("\nErro: Digite valores numéricos válidos.")
        return

    adicionar_lavoura(id_lavoura, produtor_id, cultura, area)

    print("\nLavoura cadastrada com sucesso.")


# =====================================================
# REGISTRAR COLHEITA
# =====================================================

def registrar_colheita():

    print("\n===== Registro de Colheita =====\n")

    try:
        id_colheita = int(input("ID da colheita: "))
        lavoura_id = int(input("ID da lavoura: "))
        producao = float(input("Produção (toneladas): "))
        tipo_colheita = input("Tipo de colheita: ")
    except ValueError:
        print("Erro: valores inválidos.")
        return

    adicionar_colheita(id_colheita, lavoura_id, producao, tipo_colheita)

    print("\nColheita registrada com sucesso.")


# =====================================================
# MENU DO SISTEMA
# =====================================================

def menu():

    while True:

        print("\n===== SISTEMA AGROTECH =====")
        print("1 - Cadastrar produtor")
        print("2 - Cadastrar lavoura")
        print("3 - Registrar colheita")
        print("4 - Listar produtores")
        print("5 - Listar lavouras")
        print("6 - Listar colheitas")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_produtor()

        elif opcao == "2":
            cadastrar_lavoura()

        elif opcao == "3":
            registrar_colheita()

        elif opcao == "4":
            listar_produtores()

        elif opcao == "5":
            listar_lavouras()

        elif opcao == "6":
            listar_colheitas()

        elif opcao == "0":
            print("\nEncerrando sistema...")
            break

        else:
            print("Opção inválida.")