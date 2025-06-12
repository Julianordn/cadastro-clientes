# cliente.py
from utils import carregar_clientes, salvar_clientes, validar_nome, validar_email, validar_telefone

def cadastrar_cliente():
    print("\n📋 Cadastro de Novo Cliente")

    while True:
        nome = input("Nome: ")
        if not validar_nome(nome):
            print("❌ Nome inválido. Tente novamente.")
            continue
        break

    while True:
        email = input("Email: ")
        if not validar_email(email):
            print("❌ Email inválido. Tente novamente.")
            continue
        break

    while True:
        telefone = input("Telefone (somente números): ")
        if not validar_telefone(telefone):
            print("❌ Telefone inválido. Tente novamente.")
            continue
        break

    clientes = carregar_clientes()
    cliente = {"nome": nome, "email": email, "telefone": telefone}
    clientes.append(cliente)
    salvar_clientes(clientes)
    print("✅ Cliente cadastrado com sucesso!")

def listar_clientes():
    print("\n📄 Lista de Clientes")
    clientes = carregar_clientes()
    if not clientes:
        print("Nenhum cliente cadastrado.")
        return
    for i, cliente in enumerate(clientes, 1):
        print(f"{i}. {cliente['nome']} - {cliente['email']} - {cliente['telefone']}")

def atualizar_cliente():
    listar_clientes()
    clientes = carregar_clientes()
    if not clientes:
        return
    try:
        indice = int(input("Digite o número do cliente que deseja atualizar: ")) - 1
        if indice < 0 or indice >= len(clientes):
            print("❌ Cliente inválido.")
            return

        print("Deixe o campo vazio para manter o valor atual.")
        nome = input(f"Novo nome ({clientes[indice]['nome']}): ")
        email = input(f"Novo email ({clientes[indice]['email']}): ")
        telefone = input(f"Novo telefone ({clientes[indice]['telefone']}): ")

        if nome.strip() and validar_nome(nome):
            clientes[indice]['nome'] = nome
        if email.strip() and validar_email(email):
            clientes[indice]['email'] = email
        if telefone.strip() and validar_telefone(telefone):
            clientes[indice]['telefone'] = telefone

        salvar_clientes(clientes)
        print("✅ Cliente atualizado com sucesso!")

    except ValueError:
        print("❌ Entrada inválida.")

def deletar_cliente():
    listar_clientes()
    clientes = carregar_clientes()
    if not clientes:
        return
    try:
        indice = int(input("Digite o número do cliente que deseja deletar: ")) - 1
        if indice < 0 or indice >= len(clientes):
            print("❌ Cliente inválido.")
            return
        confirmacao = input(f"Tem certeza que deseja deletar {clientes[indice]['nome']}? (s/n): ").lower()
        if confirmacao == 's':
            clientes.pop(indice)
            salvar_clientes(clientes)
            print("✅ Cliente deletado com sucesso.")
        else:
            print("❌ Operação cancelada.")
    except ValueError:
        print("❌ Entrada inválida.")
