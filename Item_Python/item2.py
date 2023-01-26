#Item 2
#programa en python calculo circunferencia 
# Programa para calcular la circunferencia de un círculo 

# Importar la librería math 
import math 

# Declaración del radio 
radio = float(input("Ingrese el valor del radio: ")) 

# Cálculo de la circunferencia 
circunferencia = 2 * math.pi * radio 

# Mostrar el resultado 
print("La circunferencia es", "{:.6f}".format(circunferencia))
