def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
numero = [2, 3, 4, 5, 10, 11, 13, 15, 17, 20]
for num in numero:
    if eh_primo(num):
        print(f"{num} é um número primo.")
    else:
        print(f"{num} não é um número primo.")