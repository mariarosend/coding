import pytest
from dominio import SuaClasse 

# Exercício 5: Teste da invariante[cite: 2]
def test_valor_invalido_levanta_value_error():
    obj = SuaClasse(10)
    # Garante que um valor inválido levanta ValueError[cite: 2]
    with pytest.raises(ValueError):
        obj.atualizar_valor(-10)