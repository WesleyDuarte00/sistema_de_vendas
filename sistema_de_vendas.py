estoque = {
    101: {"nome": "Bola de Tenis", "preco": 70.00, "quantidade": 100},
    102: {"nome": "Bola de Basquete", "preco": 85.90, "quantidade": 300},
    103: {"nome": "Bola de Futebol", "preco": 100.00, "quantidade": 700},
    104: {"nome": "Bola de Volei'", "preco": 83.50, "quantidade": 250}
}

carrinho = []

opcao = ""
while opcao != "0":
    print("\n🖥️  SISTEMA DE VENDAS E-COMMERCE")
    print("[1] Visualizar Estoque")
    print("[2] Adicionar Item ao Carrinho")
    print("[3] Visualizar Carrinho")
    print("[4] Finalizar Compra")
    print("[0] Sair do Sistema")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        print("\n" + "="*50)
        print(f"{'ID':<6} | {'NOME DO PRODUTO':<20} | {'PREÇO (R$)':<10} | {'QTD':<5}")
        print("-" * 50)
        for id_prod, info in estoque.items():
            print(f"{id_prod:<6} | {info['nome']:<20} | R$ {info['preco']:<8.2f} | {info['quantidade']:<5}")
        print("="*50)

    elif opcao == "2":

        print("\n" + "="*50)
        print(f"{'ID':<6} | {'NOME DO PRODUTO':<20} | {'PREÇO (R$)':<10} | {'QTD':<5}")
        print("-" * 50)
        for id_prod, info in estoque.items():
            print(f"{id_prod:<6} | {info['nome']:<20} | R$ {info['preco']:<8.2f} | {info['quantidade']:<5}")
        print("="*50)

        id_entrada = input("Digite o ID do produto que deseja comprar: ").strip()
        if not id_entrada.isdigit():
            print("\n❌ Erro: O ID deve ser um número inteiro!")
            continue

        id_escolhido = int(id_entrada)

        if id_escolhido not in estoque:
            print("\n❌ Erro: Produto não encontrado no estoque.")
            continue

        qtd_entrada = input(f"Digite a quantidade de '{estoque[id_escolhido]['nome']}': ").strip()
        if not qtd_entrada.isdigit():
            print("\n❌ Erro: A quantidade deve ser um número inteiro!")
            continue

        qtd_desejada = int(qtd_entrada)

        if qtd_desejada <= 0:
            print("\n❌ Erro: A quantidade deve ser maior do que zero.")
            continue

        if qtd_desejada > estoque[id_escolhido]["quantidade"]:
            print(f"\n❌ Erro: Estoque insuficiente! Temos apenas {estoque[id_escolhido]['quantidade']} unidades.")
            continue

        estoque[id_escolhido]["quantidade"] -= qtd_desejada

        ja_no_carrinho = False
        for item in carrinho:
            if item["id"] == id_escolhido:
                item["quantidade"] += qtd_desejada
                ja_no_carrinho = True
                print(f"\n✅ Mais {qtd_desejada}x '{item['nome']}' adicionados ao seu carrinho!")
                break

        if not ja_no_carrinho:
            novo_item = {
                "id": id_escolhido,
                "nome": estoque[id_escolhido]["nome"],
                "preco_unitario": estoque[id_escolhido]["preco"],
                "quantidade": qtd_desejada
            }
            carrinho.append(novo_item)
            print(f"\n✅ '{novo_item['nome']}' adicionado ao carrinho com sucesso!")

    elif opcao == "3":
        if not carrinho:
            print("\n🛒 Seu carrinho está vazio no momento.")
        else:
            print("\n" + "="*60)
            print(f"{'PRODUTO':<20} | {'QTD':<5} | {'PREÇO UNIT.':<12} | {'TOTAL ITEM':<12}")
            print("-" * 60)

            subtotal = 0
            for item in carrinho:
                total_item = item["preco_unitario"] * item["quantidade"]
                subtotal += total_item
                print(f"{item['nome']:<20} | {item['quantidade']:<5} | R$ {item['preco_unitario']:<9.2f} | R$ {total_item:<9.2f}")

            print("-" * 60)
            print(f"{'SUBTOTAL:':<44} R$ {subtotal:.2f}")
            print("="*60)

    elif opcao == "4":
        if not carrinho:
            print("\n❌ Não é possível finalizar a compra. O carrinho está vazio!")
            continue

        subtotal = 0
        print("\n" + "="*60)
        print(f"{'PRODUTO':<20} | {'QTD':<5} | {'PREÇO UNIT.':<12} | {'TOTAL ITEM':<12}")
        print("-" * 60)
        for item in carrinho:
            total_item = item["preco_unitario"] * item["quantidade"]
            subtotal += total_item
            print(f"{item['nome']:<20} | {item['quantidade']:<5} | R$ {item['preco_unitario']:<9.2f} | R$ {total_item:<9.2f}")
        print("-" * 60)
        print(f"{'SUBTOTAL:':<44} R$ {subtotal:.2f}")
        print("="*60)

        cupom = input("Possui algum cupom de desconto? (Pressione Enter para pular): ").strip().upper()
        desconto = 0.0

        if cupom == "DEV10":
            desconto = subtotal * 0.10
            print("🎉 Cupom DEV10 aplicado: 10% de desconto!")
        elif cupom == "DEV20":
            if subtotal > 500.00:
                desconto = subtotal * 0.20
                print("🎉 Cupom DEV20 aplicado: 20% de desconto!")
            else:
                print("⚠️ Cupom DEV20 só é válido para compras acima de R$ 500.00.")
        elif cupom != "":
            print("❌ Cupom inválido! Prosseguindo sem desconto.")

        total_a_pagar = subtotal - desconto

        print("\n" + "═"*40)
        print(f" RESUMO DO PEDIDO ")
        print("═"*40)
        print(f"Subtotal:       R$ {subtotal:.2f}")
        print(f"Desconto:       R$ {desconto:.2f}")
        print(f"Total a Pagar:  R$ {total_a_pagar:.2f}")
        print("═"*40)

        confirmacao = input("Confirma o pagamento? (S/N): ").strip().upper()

        if confirmacao == "S":
            print("\n💰 Pagamento confirmado com sucesso! Obrigado pela compra!")
            carrinho.clear()
        else:
            print("\n❌ Operação cancelada. Devolvendo itens ao estoque...")
            for item in carrinho:
                id_prod = item["id"]
                estoque[id_prod]["quantidade"] += item["quantidade"]
            carrinho.clear()
            print("Estoque restaurado.")

    elif opcao == "0":
        print("\nSaindo do sistema... Até logo!")

    else:
        print("\n❌ Opção inválida! Por favor, tente novamente.")