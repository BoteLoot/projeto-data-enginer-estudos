numeros = [5, 3, 8, 1, 4, 7, 2, 6, 9, 0, 12, 15, 10, 11, 14, 13, 17, 16, 19, 18]
maior = numeros[0]
menor = numeros[0]
total = 0

for numero in numeros:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    total += numero

media = total / len(numeros)
print(f"Maior número: {maior}")
print(f"Menor número: {menor}")
print(f"Média: {media:.2f}")