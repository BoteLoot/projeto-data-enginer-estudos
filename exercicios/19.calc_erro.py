def calculadora(a, b, operacao):
    if operacao == 'soma':
        return a + b
    elif operacao == 'subtracao':
        return a - b
    elif operacao == 'multiplicacao':
        return a * b
    elif operacao == 'divisao':
        if b == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        return a / b
    else:
        raise ValueError("Operação inválida. Use 'soma', 'subtracao', 'multiplicacao' ou 'divisao'.")
try:
    resultado = calculadora(10, 0, 'divisao')
    print(f"Resultado: {resultado}")
except ZeroDivisionError as e:
    print(f"Erro: {e}")
except ValueError as e:
    print(f"Erro: {e}")

print(calculadora(10, 5, 'soma'))  # Saída: 15
print(calculadora(10, 5, 'subtracao'))  # Saída: 5
print(calculadora(10, 5, 'multiplicacao'))  # Saída: 50
print(calculadora(10, 5, 'divisao'))  # Saída: 2.0
print(calculadora(10, 0, 'divisao'))  # ERRO: Divisão por zero não é permitida.
print(calculadora(10, 5, 'modulo'))  # ERRO: Operação inválida. Use 'soma', 'subtracao', 'multiplicacao' ou 'divisao'.
