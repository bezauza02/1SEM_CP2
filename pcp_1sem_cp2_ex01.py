
estado = int(input("Código do estado (1 a 5): "))
peso_ton = float(input("Peso da carga (toneladas): "))
codigo_carga = int(input("Código da carga (10 a 40): "))


peso_kg = peso_ton * 1000


if 10 <= codigo_carga <= 20:
    preco_kg = 100
elif 21 <= codigo_carga <= 30:
    preco_kg = 250
else:
    preco_kg = 340

preco_total = peso_kg * preco_kg


if estado == 1:
    imposto = preco_total * 0.35
elif estado == 2:
    imposto = preco_total * 0.25
elif estado == 3:
    imposto = preco_total * 0.15
elif estado == 4:
    imposto = preco_total * 0.05
else:
    imposto = 0

total = preco_total + imposto

print(f"Peso em kg: {peso_kg}")
print(f"Preço da carga: R$ {preco_total:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Valor total: R$ {total:.2f}")