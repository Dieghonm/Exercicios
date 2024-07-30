def juros_compostos(valorInicial:float, jurosAnual:float, tempo:int ) -> float :
  acumulado = valorInicial
  for ano in range(1, tempo+1):
    juros = acumulado*jurosAnual
    acumulado += juros
  return(round(acumulado, 2))
print(juros_compostos(1000, 0.05, 10))


