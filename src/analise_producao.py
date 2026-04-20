import sys

# Importando as funções de cadastro e listagem
from cadastro import (
    cadastrar_produtor,
    cadastrar_lavoura,
    registrar_colheita,
    listar_produtores,
    listar_lavouras,
    listar_colheitas
)


from analise_producao import (
    analisar_perdas_colheita, 
    calcular_produtividade_detalhada
)

from arquivos import (
    carregar_produtores, 
    carregar_lavouras, 
    salvar_produtores, 
    salvar_lavouras
)

def menu():
    # --- INICIALIZAÇÃO ---
    # Ao abrir o programa, ele busca o que já foi salvo anteriormente
    print("Iniciando sistema...")
    carregar_produtores()
    carregar_lavouras()
    
    while True:
        print("\n" + "="*40)
        print("   MONITOR DE PERDAS: CANA-DE-AÇÚCAR")
        print("="*40)
        print("1 - Cadastrar Produtor (Oracle + JSON)")
        print("2 - Cadastrar Lavoura")
        print("3 - Registrar Colheita")
        print("4 - Listar Produtores")
        print("5 - Listar Lavouras")
        print("6 - Listar Colheitas")
        print("7 - ANALISAR PERDAS (SOCICANA)")
        print("8 - RELATÓRIO TCH (Produtividade)")
        print("9 - Salvar Dados (JSON)")
        print("0 - Sair")
        print("="*40)

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
            # Função nova que você adicionou
            analisar_perdas_colheita()

        elif opcao == "8":
            # Função de produtividade real (TCH)
            calcular_produtividade_detalhada()

        elif opcao == "9":
            salvar_produtores()
            salvar_lavouras()
            print("\n✅ Dados salvos com sucesso!")

        elif opcao == "0":
            # Salva automaticamente antes de fechar para evitar perda de dados
            print("\nSalvando alterações e encerrando...")
            salvar_produtores()
            salvar_lavouras()
            print("Sistema encerrado. Até logo!")
            break

        else:
            print("⚠️ Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()