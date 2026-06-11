alunos = {"Alice": 8.5, "Bob": 7.0, "Charlie": 9.5, "David": 6.5, "Eve": 8.0}
print("Aprovados:")
for nome, nota in alunos.items():
    if nota >= 7.0:
        print(f"{nome}: {nota}")
print("Reprovados:")
for nome, nota in alunos.items():
    if nota < 7.0:
        print(f"{nome}: {nota}")