produtos = {"Notebook": 2500, "Smartphone": 1500, "Tablet": 1200, "Monitor": 800, "Teclado": 80, "Mouse": 50}
for produto, preco in produtos.items():
    if preco > 100:
        preco_com_desconto = preco * 0.9  # Aplica um desconto de 10%
        print(f"{produto}: R${preco_com_desconto:.2f} (desconto aplicado)")
    else:
        print(f"{produto}: R${preco:.2f} (sem desconto)")