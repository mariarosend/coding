from decimal import Decimal
precos = {
    "corte": Decimal("35.00"),
    "barba": Decimal("25.00"),
    "sobrancelha": Decimal("15.00"),
    "hidratação": Decimal("40.00"),
}
comanda = ["corte", "barba", "corte", "pintura"]
total = Decimal("0.00")
validos = []

for item in comanda:
    if item not in precos:
        print(f"item fora da tabela: {item}")
        continue
    validos.append(item)
    total += precos[item]

if len(validos) >= 3:
    desconto = total * Decimal("0.10")
else:
    desconto = Decimal("0.00")

print(f"Itens: {len(validos)}")
print(f"Distintos: {sorted(set(validos))}")
print(f"Subtotal: R$ {total:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total: R$ {total - desconto:.2f}")
