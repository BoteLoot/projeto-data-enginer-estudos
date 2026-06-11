a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
print(f"A soma de {a} e {b} é: {a + b}")
print(f"A subtração de {a} e {b} é: {a - b}")
print(f"A multiplicação de {a} e {b} é: {a * b}")
if b != 0:
    print(f"A divisão de {a} por {b} é: {a / b}")
else:    print("Erro: Divisão por zero não é permitida.")