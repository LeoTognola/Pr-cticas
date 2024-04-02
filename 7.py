from scipy.integrate import quad

# Define la función a integrar
def f(x):
    return x**2

# Define los límites para la integración
limites = [(0, 1), (0, 2), (0, 3)]  # Puedes agregar más límites según sea necesario

# Lista para almacenar los resultados de la integración
resultados = []
errores =[]

# Itera sobre los límites y realiza la integración
for limite in limites:
    resultado, error = quad(f, limite[0], limite[1])
    resultados.append(resultado)
    errores.append(error)
    
print(resultados)  # Muestra los resultados de la integración
print(errores)



import numpy as np
from scipy.integrate import quad

# Define la función a integrar
def f(x):
    return x**2

# Define los límites para la integración
limites = [(0, 1), (0, 2), (0, 3)]  # Puedes agregar más límites según sea necesario

# Matriz para almacenar los resultados de la integración y los errores
resultados_errores = np.zeros((len(limites), 2))  # Matriz de ceros con filas igual al número de límites y dos columnas (resultado, error)

# Itera sobre los límites y realiza la integración
for i, limite in enumerate(limites):
    resultado, error = quad(f, limite[0], limite[1])
    resultados_errores[i] = [resultado, error]

# Muestra los resultados de la integración y los errores
for i, (resultado, error) in enumerate(resultados_errores):
    print("Resultado de la integración {}: {}".format(i+1, resultado))
    print("Error de la integración {}: {}".format(i+1, error))
