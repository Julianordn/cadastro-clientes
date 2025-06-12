# cadastro_clientes.py
from cliente import cadastrar_cliente, listar_clientes, atualizar_cliente, deletar_cliente

def menu():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Cadastrar cliente")
        print("2. Listar clientes")
        print("3. Atualizar cliente")
        print("4. Deletar cliente")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            atualizar_cliente()
        elif opcao == "4":
            deletar_cliente()
        elif opcao == "5":
            print("👋 Saindo do programa. Até mais!")
            break
        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
