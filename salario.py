# Función que recibe dos parámetros y calcula el salario
def calcular_salario_semanal(horas, pago_hora):
    salario = horas * pago_hora
    return salario

# Bloque principal del programa 
horas_trabajadas = 40
pago_por_hora = 10.50

#Llamada a la función e impresión del resultado
resultado_final = calcular_salario_semanal(horas_trabajadas, pago_por_hora)
print("El salario semanal calculado es: $", resultado_final)