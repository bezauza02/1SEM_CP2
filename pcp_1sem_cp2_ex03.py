
cp1 = float(input("CP1: "))
cp2 = float(input("CP2: "))
cp3 = float(input("CP3: "))
sp1 = float(input("SP1: "))
sp2 = float(input("SP2: "))
gs = float(input("GS: "))


menor = cp1
if cp2 < menor:
    menor = cp2
if cp3 < menor:
    menor = cp3

soma = cp1 + cp2 + cp3 - menor + sp1 + sp2
media = (soma / 4) * 0.4 + gs * 0.6
media_peso = media * 0.4

print(f"Média: {media:.1f}")
print(f"Média com peso: {media_peso:.1f}")
