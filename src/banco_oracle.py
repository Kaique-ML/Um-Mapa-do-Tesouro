import oracledb

#Não esqueça de instalar o import:  
    # pip install oracledb

def conectar_banco():

    conn = oracledb.connect(
        user="rm572500",
        password="fiap26",
        dsn="oracle.fiap.com.br:1521/ORCL"
    )

    return conn


def inserir_produtor(id, nome, fazenda, latitude, longitude):

    try:

        conn = conectar_banco()

        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO produtores
            (id, nome, fazenda, latitude, longitude)
            VALUES (:1, :2, :3, :4, :5)
            """,
            (id, nome, fazenda, latitude, longitude)
        )

        conn.commit()

        cursor.close()
        conn.close()

        print("Produtor inserido com sucesso!")

    except Exception as erro:
        print("Erro ao inserir produtor:", erro)


def testar_conexao():

    try:

        conn = conectar_banco()
        print("Conexão com Oracle realizada com sucesso!")

        conn.close()

    except Exception as erro:
        print("Erro ao conectar:", erro)