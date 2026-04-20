# =====================================================
# ESTRUTURAS DE DADOS DO SISTEMA AGROTECH
# =====================================================

# Listas principais do sistema
produtores = []
lavouras = []
colheitas = []


# =====================================================
# ADICIONAR PRODUTOR
# =====================================================

def adicionar_produtor(id, nome, fazenda, latitude, longitude):

    produtor = {
        "id": id,
        "nome": nome,
        "fazenda": fazenda,
        "latitude": latitude,
        "longitude": longitude
    }

    produtores.append(produtor)


# =====================================================
# ADICIONAR LAVOURA
# =====================================================

def adicionar_lavoura(id, produtor_id, cultura, area):

    lavoura = {
        "id": id,
        "produtor_id": produtor_id,
        "cultura": cultura,
        "area": area
    }

    lavouras.append(lavoura)


# =====================================================
# ADICIONAR COLHEITA
# =====================================================

def adicionar_colheita(id, lavoura_id, producao, tipo_colheita):

    colheita = {
        "id": id,
        "lavoura_id": lavoura_id,
        "producao": producao,
        "tipo_colheita": tipo_colheita
    }

    colheitas.append(colheita)


# =====================================================
# LISTAR PRODUTORES
# =====================================================

def listar_produtores():

    if not produtores:
        print("Nenhum produtor cadastrado.")
        return

    for p in produtores:

        print("\n----------------------")
        print("ID:", p["id"])
        print("Nome:", p["nome"])
        print("Fazenda:", p["fazenda"])
        print("Latitude:", p["latitude"])
        print("Longitude:", p["longitude"])


# =====================================================
# LISTAR LAVOURAS
# =====================================================

def listar_lavouras():

    if not lavouras:
        print("Nenhuma lavoura cadastrada.")
        return

    for l in lavouras:

        print("\n----------------------")
        print("ID:", l["id"])
        print("Produtor ID:", l["produtor_id"])
        print("Cultura:", l["cultura"])
        print("Área:", l["area"], "hectares")


# =====================================================
# LISTAR COLHEITAS
# =====================================================

def listar_colheitas():

    if not colheitas:
        print("Nenhuma colheita registrada.")
        return

    for c in colheitas:

        print("\n----------------------")
        print("ID:", c["id"])
        print("Lavoura ID:", c["lavoura_id"])
        print("Produção:", c["producao"], "toneladas")
        print("Tipo de colheita:", c["tipo_colheita"])


# =====================================================
# RESUMO DO SISTEMA (USO DE TUPLA)
# =====================================================

def resumo_producao():

    total_produtores = len(produtores)
    total_lavouras = len(lavouras)
    total_colheitas = len(colheitas)

    return (total_produtores, total_lavouras, total_colheitas)