numero1 = int(input("Informe o primeiro número (menor): "))
numero2 = int(input("Informe o segundo número (maior): "))

soma = 0
contador = 0

for i in range(numero1, numero2 + 1):
    soma += i
    contador += 1

media = soma / contador

print(f"A média aritmética entre {numero1} e {numero2} é {media}")