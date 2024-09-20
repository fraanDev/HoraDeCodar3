valor1 = float(input("Informe o primeiro valor: "))

while True:
    valor2 = float(input("Informe o segundo valor (não pode ser zero ou negativo): "))
    if valor2 > 0:
        break
    else:
        print("Valor inválido. O segundo valor deve ser maior que zero.")

resultado = valor1 / valor2

print(f"O resultado da divisão de {valor1} por {valor2} é: {resultado}")
