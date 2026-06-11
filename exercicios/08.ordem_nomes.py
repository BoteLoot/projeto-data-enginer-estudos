nomes = []

for i in range(6):
    nome = input(f"Digite o nome {i}: ")
    nomes.append(nome)
nomes.sort()
print(f"Nomes em ordem alfabética: {nomes}")