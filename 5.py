import numpy as np
from scipy import integrate

cantidad_muestras=500
x= np.linspace (-10,10,cantidad_muestras)
# Matriz para almacenar los resultados de la integración y los errores
resultados_errores = np.zeros((len(x), 2))  # Matriz de ceros con filas igual al número de límites y dos columnas (resultado, error)

def funcion(x):
    return ((np.exp(-x*x/2) * np.sin(x*0.99*2*np.pi)))**2
    
for i in range(cantidad_muestras-1):
    límite_inferior = x[i] 
    límite_superior = x[i+1]
    
    # Calcula la integral definida
    resultado, error = integrate.quad(funcion, límite_inferior, límite_superior)
    resultados_errores[i] = [resultado, error]

# Imprime el resultado
print("Integración h_1:", resultados_errores)
