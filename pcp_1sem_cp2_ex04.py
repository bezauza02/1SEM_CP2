
def calcular_horas_extras(salario, horas):
    return salario * 0.015 * horas

def calcular_descontos_faltas(salario, faltas):
    return salario * 0.02 * faltas

def calcular_bonus(cargo, recebeu):
    if recebeu.lower() != 's':
        return 0

    if cargo == 1:
        return 1000
    elif cargo == 2:
        return 500
    elif cargo == 3:
        return 300
    else:
        return 100

nome = input("Nome: ")
cargo = int(input("Cargo (1-Gerente 2-Analista 3-Assistente 4-Estagiário): "))
salario = float(input("Salário base: "))
horas = float(input("Horas extras: "))
faltas = int(input("Faltas: "))
bonus_flag = input("Recebeu bônus (s/n): ")

extra = calcular_horas_extras(salario, horas)
desconto = calcular_descontos_faltas(salario, faltas)
bonus = calcular_bonus(cargo, bonus_flag)

bruto = salario + extra + bonus
final = bruto - desconto

print(f"\nSalário bruto: R$ {bruto:.2f}")
print(f"Acréscimos: R$ {extra + bonus:.2f}")
print(f"Descontos: R$ {desconto:.2f}")
print(f"Salário final: R$ {final:.2f}")
