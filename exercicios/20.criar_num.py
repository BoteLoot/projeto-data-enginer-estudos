total = 0

try:
    with open("numeros.txt", "r", encoding="utf-8") as file:
        for linha in file:
            try:
                numero = int(linha.strip())
                total += numero
            except ValueError:
                print(f"Linha inválida ignorada: '{linha.strip()}'")
    print(f"Total: {total}")
except FileNotFoundError:
    print("Erro: arquivo 'numeros.txt' não encontrado.")