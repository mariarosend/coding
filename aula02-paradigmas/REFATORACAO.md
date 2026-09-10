# Refatoracao do relatorio de vendas

## As duas versoes

### Versao Procedural (Original)
python
def relatorio(vendas):
total_por_categoria = {}
for v in vendas:
if v["valor"] <= VALOR_MINIMO:
continue
liquido = v["valor"] * (1 - IMPOSTO)
cat = v["categoria"]
if cat not in total_por_categoria:
total_por_categoria[cat] = 0
total_por_categoria[cat] += liquido
return total_por_categoria
### Versao Funcional (Pipeline)
python
def relatorio(vendas):
relevantes = filter(acima_do_minimo, vendas)
liquidas = map(aplicar_imposto, relevantes)
return reduce(agrupar_por_categoria, liquidas, {})
## Tempo gasto
* Escrever os testes: 25 minutos
* Separar as tres funcoes: 35 minutos
* Aplicar a mudanca de imposto por categoria: 20 minutos

## Qual versao a equipe leva para o projeto do semestre
A equipe adota a versão funcional baseada em pipeline. O código ficou significativamente mais legível, as responsabilidades estão bem isoladas em funções puras, e a facilidade para implementar mudanças em regras de negócio (como a variação de impostos) provou ser muito superior sem o risco de efeitos colaterais.

## O que ficou em duvida
Como lidar com a performance do `reduce` em bases de dados extremamente grandes no backend do projeto?