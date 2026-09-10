from decimal import Decimal

PRECOS = {
    "corte": Decimal("35.00"),
    "barba": Decimal("25.00"),
    "sobrancelha": Decimal("15.00"),
    "hidratacao": Decimal("40.00"),
}

def itens_validos(comanda, precos=PRECOS):
    """Devolve apenas os itens que existem no catalogo."""
    validos = []
    for item in comanda:
        if item in precos:
            validos.append(item)
    return validos

def subtotal(comanda, precos=PRECOS):
    """Soma o preco dos itens validos."""
    total = Decimal("0.00")
    for item in itens_validos(comanda, precos):
        total += precos[item]
    return total

def desconto(comanda, valor, minimo=3):
    """10 por cento a partir de minimo itens VALIDOS."""
    if len(itens_validos(comanda)) >= minimo:
        return valor * Decimal("0.10")
    return Decimal("0.00")

def fechar(comanda):
    """Devolve subtotal, desconto e total."""
    sub = subtotal(comanda)
    desc = desconto(comanda, sub)
    return {"subtotal": sub, "desconto": desc, "total": sub - desc}

if __name__ == "__main__":
    conta = fechar(["corte", "barba", "corte", "pintura"])
    for chave, valor in conta.items():
        print(f"{chave: <9} R$ {valor:.2f}")

