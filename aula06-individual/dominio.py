# --- EXERCÍCIOS DE FIXAÇÃO (INDIVIDUAL) ---

class SuaClasse:
    # Exercício 4: Atributo de classe
    nome_do_sistema = "Meu Sistema POO" 

    def __init__(self, valor):
        # A proteção de verdade mora no método
        self._valor = valor # Atributo 'protegido' por convenção (underscore)

    # Exercício 6: Property em ação
    @property
    def calculo_property(self):
        # Calcula um valor sob demanda, sem parênteses
        return self._valor * 2

    # Exercício 2: Função vira método
    def atualizar_valor(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("O valor não pode ser negativo") # Invariante[cite: 2]
        self._valor = novo_valor


# Exercício 1: Dois objetos, dois estados[cite: 2]
obj1 = SuaClasse(valor=10)
obj2 = SuaClasse(valor=20)
print(f"Estado Obj1: {obj1._valor}")
print(f"Estado Obj2: {obj2._valor}")

# Provando o Exercício 4 (Atributo de classe compartilhado)[cite: 2]
print(f"Nome do sistema Obj1: {obj1.nome_do_sistema}")
print(f"Nome do sistema Obj2: {obj2.nome_do_sistema}")

# Diferença de chamar property (Exercício 6)[cite: 2]
print(f"Property em ação (sem parênteses): {obj1.calculo_property}")

# Exercício 3: Quebrar de propósito[cite: 2]
try:
    obj1.atualizar_valor(-5) # Tentando colocar valor inválido[cite: 2]
except ValueError as e:
    print(f"Erro capturado com sucesso: {e}")