from functools import reduce

VENDAS = [
    {"produto": "Teclado", "valor": 150.00, "categoria": "Periferico"},
    {"produto": "Mouse", "valor": 80.00, "categoria": "Periferico"},
    {"produto": "Monitor", "valor": 900.00, "categoria": "Tela"},
    {"produto": "Headset", "valor": 120.00, "categoria": "Acessorio"},
    {"produto": "Suporte", "valor": 35.00, "categoria": "Acessorio"},
    {"produto": "Cabo HDMI", "valor": 250.00, "categoria": "Periferico"},
]

IMPOSTO = 0.10
VALOR_MINIMO = 100.00

def acima_do_minimo(venda):
    """Diz se a venda entra no relatorio."""
    return venda["valor"] > VALOR_MINIMO

def aplicar_imposto(venda):
    """Devolve uma NOVA venda com o valor liquido."""
    return {**venda, "valor": venda["valor"] * (1 - IMPOSTO)}

def agrupar_por_categoria(acumulado, venda):
    """Soma a venda no total da sua categoria."""
    cat = venda["categoria"]
    return {**acumulado, cat: acumulado.get(cat, 0) + venda["valor"]}

def relatorio(vendas):
    """Total liquido por categoria, apenas de vendas acima do minimo."""
    relevantes = filter(acima_do_minimo, vendas)
    liquidas = map(aplicar_imposto, relevantes)
    return reduce(agrupar_por_categoria, liquidas, {})

if __name__ == "__main__":
    for categoria, total in relatorio(VENDAS).items():
        print(f"{categoria:12} R$ {total:8.2f}")
def acima_do_minimo(venda):
    """Diz se a venda entra no relatorio."""
    return venda["valor"] > VALOR_MINIMO

def aplicar_imposto(venda):
    """Devolve uma NOVA venda com o valor liquido com imposto variavel."""
    cat = venda["categoria"]
    if cat == "Periferico":
        taxa = 0.10
    elif cat == "Tela":
        taxa = 0.15
    else:
        taxa = 0.05
    return {**venda, "valor": venda["valor"] * (1 - taxa)}

def agrupar_por_categoria(acumulado, venda):
    """Soma a venda no total da sua categoria."""
    cat = venda["categoria"]
    return {**acumulado, cat: acumulado.get(cat, 0) + venda["valor"]}