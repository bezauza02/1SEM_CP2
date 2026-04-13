
def pode_aprovar(idade, renda, valor):
    return idade > 18 and valor <= renda * 20

def definir_taxa(parcelas):
    if parcelas <= 6:
        return 0.05
    elif parcelas <= 12:
        return 0.08
    else:
        return 0.10

def calcular_parcela(valor, taxa, parcelas):
    return valor * (taxa * (1 + taxa)**parcelas) / ((1 + taxa)**parcelas - 1)

def calcular_total(parcela, parcelas):
    return parcela * parcelas

def calcular_juros(total, valor):
    return total - valor

nome = input("Nome: ")
idade = int(input("Idade: "))
renda = float(input("Renda: "))
valor = float(input("Valor do empréstimo: "))
parcelas = int(input("Parcelas (3-24): "))

if not pode_aprovar(idade, renda, valor):
    print("Empréstimo NEGADO")
else:
    taxa = definir_taxa(parcelas)
    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)

    print("\n--- APROVADO ---")
    print(f"Cliente: {nome}")
    print(f"Valor financiado: R$ {valor:.2f}")
    print(f"Taxa: {taxa*100:.1f}% ao mês")
    print(f"Parcela: R$ {parcela:.2f}")
    print(f"Total pago: R$ {total:.2f}")
    print(f"Juros pagos: R$ {juros:.2f}")