#Aqui vou desenvolver meu código de teste para revisão.

# Lista (array) principal para armazenar os motores cadastrados em memória
motores = []

def gerar_novo_id():
    """Gera um ID sequencial automático."""
    if not motores:
        return 1
    return motores[-1]["id"] + 1

def cadastrar_motor():
    """Coleta os dados do usuário e adiciona um novo motor à lista."""
    print("\n--- CADASTRAR NOVO MOTOR ---")
    modelo = input("Modelo/Série do motor: ").strip()
    fabricante = input("Fabricante (ex: WEG, Siemens): ").strip()
    
    # Validação simples para valores numéricos
    while True:
        try:
            potencia_cv = float(input("Potência (CV): "))
            rotacao_rpm = int(input("Rotação (RPM): "))
            tensao_v = input("Tensão (ex: 220/380V): ").strip()
            break
        except ValueError:
            print("❌ Erro: Potência e Rotação devem ser valores numéricos. Tente novamente.")

    novo_motor = {
        "id": gerar_novo_id(),
        "modelo": modelo,
        "fabricante": fabricante,
        "potencia_cv": potencia_cv,
        "rotacao_rpm": rotacao_rpm,
        "tensao_v": tensao_v
    }
    
    motores.append(novo_motor)
    print(f"✅ Motor '{modelo}' cadastrado com sucesso! (ID: {novo_motor['id']})")

def listar_motores():
    """Exibe todos os motores armazenados na lista."""
    print("\n--- LISTA DE MOTORES CADASTRADOS ---")
    if not motores:
        print("Nenhum motor cadastrado no momento.")
        return

    for m in motores:
        print(f"ID: {m['id']} | Modelo: {m['modelo']} | Fab: {m['fabricante']} | "
              f"Potência: {m['potencia_cv']} CV | {m['rotacao_rpm']} RPM | Tensão: {m['tensao_v']}")

def buscar_motor():
    """Busca motores pelo ID ou parte do nome do modelo."""
    print("\n--- BUSCAR MOTOR ---")
    if not motores:
        print("Nenhum motor cadastrado para buscar.")
        return

    termo = input("Digite o ID ou nome do modelo: ").strip().lower()
    encontrados = [
        m for m in motores 
        if termo == str(m["id"]) or termo in m["modelo"].lower()
    ]

    if not encontrados:
        print("🔍 Nenhum motor encontrado com esse critério.")
    else:
        for m in encontrados:
            print(f"ID: {m['id']} | Modelo: {m['modelo']} | Fab: {m['fabricante']} | "
                  f"Potência: {m['potencia_cv']} CV | {m['rotacao_rpm']} RPM | Tensão: {m['tensao_v']}")

def atualizar_motor():
    """Permite editar os dados de um motor existente pelo ID."""
    print("\n--- ATUALIZAR MOTOR ---")
    listar_motores()
    if not motores:
        return

    try:
        id_busca = int(input("\nDigite o ID do motor que deseja alterar: "))
    except ValueError:
        print("❌ ID inválido.")
        return

    for m in motores:
        if m["id"] == id_busca:
            print("Deixe em branco e pressione Enter para manter o valor atual.")
            
            novo_modelo = input(f"Modelo [{m['modelo']}]: ").strip()
            novo_fab = input(f"Fabricante [{m['fabricante']}]: ").strip()
            nova_pot = input(f"Potência CV [{m['potencia_cv']}]: ").strip()
            nova_rot = input(f"Rotação RPM [{m['rotacao_rpm']}]: ").strip()
            nova_ten = input(f"Tensão [{m['tensao_v']}]: ").strip()

            if novo_modelo: m["modelo"] = novo_modelo
            if novo_fab: m["fabricante"] = novo_fab
            if nova_pot: m["potencia_cv"] = float(nova_pot)
            if nova_rot: m["rotacao_rpm"] = int(nova_rot)
            if nova_ten: m["tensao_v"] = nova_ten

            print("✅ Motor atualizado com sucesso!")
            return

    print("❌ Motor com este ID não foi encontrado.")

def remover_motor():
    """Remove um motor da lista pelo ID."""
    print("\n--- REMOVER MOTOR ---")
    listar_motores()
    if not motores:
        return

    try:
        id_busca = int(input("\nDigite o ID do motor que deseja remover: "))
    except ValueError:
        print("❌ ID inválido.")
        return

    for i, m in enumerate(motores):
        if m["id"] == id_busca:
            removido = motores.pop(i)
            print(f"🗑️ Motor '{removido['modelo']}' (ID: {id_busca}) removido com sucesso!")
            return

    print("❌ Motor com este ID não foi encontrado.")

def popular_dados_teste():
    """Insere alguns registros iniciais para facilitar os testes."""
    motores.extend([
        {"id": 1, "modelo": "W22 IR3 Premium", "fabricante": "WEG", "potencia_cv": 10.0, "rotacao_rpm": 1750, "tensao_v": "220/380V"},
        {"id": 2, "modelo": "1LE0", "fabricante": "Siemens", "potencia_cv": 5.0, "rotacao_rpm": 3500, "tensao_v": "380/660V"}
    ])

def menu_principal():
    """Loop principal de navegação do sistema."""
    popular_dados_teste() # Comente esta linha se quiser iniciar com a lista vazia
    
    while True:
        print("\n" + "="*35)
        print("   SISTEMA DE CADASTRO DE MOTORES")
        print("="*35)
        print("1. Cadastrar Motor")
        print("2. Listar Todos os Motores")
        print("3. Buscar Motor")
        print("4. Atualizar Motor")
        print("5. Remover Motor")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_motor()
        elif opcao == "2":
            listar_motores()
        elif opcao == "3":
            buscar_motor()
        elif opcao == "4":
            atualizar_motor()
        elif opcao == "5":
            remover_motor()
        elif opcao == "0":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("⚠️ Opção inválida! Tente novamente.")

# Ponto de entrada do script
if __name__ == "__main__":
    menu_principal()