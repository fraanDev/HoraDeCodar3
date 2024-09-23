dentro_intervalo = 0
fora_intervalo = 0

for i in range(10):
    valor = int(input(f"Informe o valor {i+1}: "))
    if 24 <= valor <= 42:
        dentro_intervalo += 1
    else:
        fora_intervalo += 1

print(f"Valores dentro do intervalo [24, 42]: {dentro_intervalo}")
print(f"Valores fora do intervalo: {fora_intervalo}")