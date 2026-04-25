#Variáveis
cod_estado = int(input("Digite o código do estado de origem da carga do caminhão (1 a 5): "))
peso = float(input("Digite o peso da carga do caminhão (Em Toneladas): "))
cod_carga = int(input("Digite o código da carga (10 a 40): "))

#Peso da carga do caminhão convertida em Kg e preço da carga do caminhão

peso_kg = peso * 1000

if cod_carga >= 10 and cod_carga <= 20:
    preco_carga = peso_kg  * 100
elif cod_carga >= 21 and cod_carga <= 30:
    preco_carga = peso_kg * 250
elif cod_carga >= 31 and cod_carga <= 40:
    preco_carga = peso_kg * 340

#Valor do imposto
if cod_estado == 1:
    valor_impst = preco_carga * 0.35
elif cod_estado == 2:
    valor_impst = preco_carga * 0.25
elif cod_estado == 3:
    valor_impst = preco_carga * 0.15
elif cod_estado == 4:
    valor_impst = preco_carga * 0.05
elif cod_estado == 5:
    valor_impst = 0

#Valor total
vlr_total = valor_impst + preco_carga
print(peso_kg)
print(preco_carga)
print(valor_impst)
print(vlr_total)
