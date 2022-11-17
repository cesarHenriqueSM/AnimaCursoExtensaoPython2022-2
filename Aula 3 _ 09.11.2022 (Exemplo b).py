preco = 1856.78
imposto = preco * 0.05
print(imposto)

def calcular_imposto(preco_produto):
  imposto = preco_produto*0.05
  round (imposto, 2)
  return imposto

valor = 4799
imposto = calcular_imposto(valor)
print(imposto)

valores = [5.64, 87.45, 115, 1420.36]

for valor in valores:
  print(f"O imposto de R${valor} equivale a R${calcular_imposto(valor)}")

