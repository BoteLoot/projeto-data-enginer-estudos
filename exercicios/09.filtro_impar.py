numeros = [5, 3, 8, 1, 4, 7, 2, 6, 9, 0, 12, 15, 10, 11, 14, 13, 17, 16, 19, 18]
impares = []
for numero in numeros:
    if numero % 2 != 0:
        impares.append(numero)
print(f"Números ímpares: {impares}")