def calcular_salario(horas_trabajadas, tarifa):
  if horas_trabajadas <= 40:
    salario = horas_trabajadas * tarifa
  else:
    horas_extras = horas_trabajadas - 40
    salario_base = 40 * tarifa
    salario_extras = horas_extras * tarifa * 1.5
    salario = salario_base + salario_extras

  return salario

horas_trabajadas = float(input("Ingrese la cantidad de horas trabajadas: "))
tarifa = float(input("Ingrese la tarifa por hora: "))

salario_total = calcular_salario(horas_trabajadas, tarifa)
print("El salario total del trabajador es:", salario_total)
