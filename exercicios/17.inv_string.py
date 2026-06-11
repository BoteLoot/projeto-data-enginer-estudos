
def inverter_string(s): #Função para inverter sem usar [::-1]
    string_invertida = ""
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida
    
palavras = ["python", "dados", "pipeline", "sql", "airflow"]
palavras_invertidas = [inverter_string(palavra) for palavra in palavras]
for palavra, palavra_invertida in zip(palavras, palavras_invertidas):
    print(f"A palavra '{palavra}' invertida é '{palavra_invertida}'.")