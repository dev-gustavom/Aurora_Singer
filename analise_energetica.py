nivel_energia = int(input("Digite o nivel de energia (%): ") )
capacidade_total = float(input("capacidade total (kWh): "))
consumo_decolagem = float(input("Consumo na decolagem (kWh): "))
taxa_perda = float(input("Taxa de perdas (ex: 0.1 para 10%): "))

energia_disponivel = capacidade_total * (nivel_energia / 100)
perdas = energia_disponivel * taxa_perda
energia_util = energia_disponivel - perdas
autonomia = energia_util / consumo_decolagem

print("\n--- ANÁLISE ENERGÉTICA ---")
print(f"Energia disponível: {energia_disponivel:.2f} kWh")
print(f"Perdas: {perdas:.2f} kWh")
print(f"Energia útil: {energia_util:.2f} kWh")
print(f"Autonomia: {autonomia:.2f} ciclos de decolagem")

if autonomia < 1:
    print("⚠ Energia insuficiente para uma decolagem segura")
else:
    print("✔ Energia suficiente para a missão inicial")