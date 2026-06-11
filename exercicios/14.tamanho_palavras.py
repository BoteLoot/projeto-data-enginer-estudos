palavras = ["python", "dados", "pipeline", "sql", "airflow"]
tamanho_palavras = [len(palavra) for palavra in palavras]
for palavra, tamanho in zip(palavras, tamanho_palavras):
    print(f"A palavra '{palavra}' tem {tamanho} caracteres.")
