from cadastro import cadastrar_producao
from analise_producao import listar_producoes, calcular_perda_total, calcular_produtividade

def menu():

    while True:

        print("\n===== Sistema Agrotech Laranja =====\n")

        print("1 - Cadastrar produção")
        print("2 - Listar produções")
        print("3 - Calcular perda total")
        print("4 - Calcular produtividade")
        print("5 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            cadastrar_producao()

        elif opcao == "2":
            listar_producoes()

        elif opcao == "3":
            calcular_perda_total()

        elif opcao == "4":
            calcular_produtividade()

        elif opcao == "5":
            print("\nEncerrando sistema.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()