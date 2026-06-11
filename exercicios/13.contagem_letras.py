frase = "Engenharia de Dados"
contagem_letras = {}
for letra in frase:
    if letra.isalpha():  # Verifica se o caractere é uma letra
        letra = letra.lower()  # Converte para minúscula para contar de forma case-insensitive
        if letra in contagem_letras:
            contagem_letras[letra] += 1
        else:
            contagem_letras[letra] = 1
print("Contagem de letras na frase:")
for letra, contagem in contagem_letras.items():
    print(f"{letra}: {contagem}")