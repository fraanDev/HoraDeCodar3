notas = []

for i in range(6):
    while True:
        nota = float(input(f"Informe a nota {i+1}: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")

media = sum(notas) / 6

print(f"A média do aluno é {media}")
