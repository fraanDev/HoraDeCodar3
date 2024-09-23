N = int(input("Informe o valor de N para gerar as tabuadas: "))

for i in range(1, N + 1):
    print(f"Tabuada do {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print("-" * 20)  