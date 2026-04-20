from cadastro import (
    cadastrar_produtor,
    cadastrar_lavoura,
    registrar_colheita,
    listar_produtores,
    listar_lavouras,
    listar_colheitas
)
# Importar as funções de manipulação de arquivos
from arquivos import (
    carregar_produtores, 
    carregar_lavouras, 
    salvar_produtores, 
    salvar_lavouras
)

def menu():
    # --- INICIALIZAÇÃO ---
    # Carrega os dados existentes nos arquivos JSON para as listas do sistema
    print("Carregando dados do sistema...")
    carregar_produtores()
    carregar_lavouras()
    
    while True:
        print("\n===== MONITOR DE PERDAS: CANA-DE-AÇÚCAR =====")
        print("1 - Cadastrar produtor")
        print("2 - Cadastrar lavoura")
        print("3 - Registrar colheita")
        print("4 - Listar produtores")
        print("5 - Listar lavouras")
        print("6 - Listar colheitas")
        print("7 - Salvar alterações (JSON)") # Opção explícita de salvamento
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

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
            
        elif opcao == "7":
            # --- SALVAMENTO MANUAL ---
            salvar_produtores()
            salvar_lavouras()
            print("\nDados salvos com sucesso nos arquivos JSON.")

        elif opcao == "0":
            # --- SALVAMENTO AUTOMÁTICO AO SAIR ---
            print("\nSalvando dados e encerrando sistema...")
            salvar_produtores()
            salvar_lavouras()
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()