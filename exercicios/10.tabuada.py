numeros = list(range(1, 6))
for n in range(1, 21):
    print(f"Tabuada do {n}:")
    for m in numeros:
        resultado = n * m
        print(f"{m} x {n} = {resultado}")