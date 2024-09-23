aprovados = 0  #

while True:
    
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 9.5:
        print(f"Aprovado com média {media}")
        aprovados += 1
    else:
        print(f"Reprovado com média {media}")

    continuar = input("Calcular a média de outro aluno? Sim (Digite 'S') / Não (Digite 'N'): ").strip().upper()
    if continuar != "S":
        break
        print(f"Quantidade de alunos aprovados: {aprovados}")

print(f"Quantidade de alunos aprovados: {aprovados}")
