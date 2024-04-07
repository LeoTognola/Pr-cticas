#Definir los Límites para Integrar UNA Función

from scipy import integrate
import numpy as np

x= np.linspace (0,100,10000)


# Define la función que deseas integrar
def funcion(x):
    return np.exp(-x*x/2) * np.sin(x*0.99*2*np.pi)

# Límites de integración

limite_inferior = x_0
limite_superior = 1

# Calcula la integral definida
resultado, error = integrate.quad(funcion, limite_inferior, limite_superior)

# Imprime el resultado
print("El resultado de la integral definida es:", resultado)



#Límites Superpuestos
import numpy as np
cantidad_muestras=6
x= np.linspace (0,100,cantidad_muestras)

for i in range(cantidad_muestras-1):
    límite_inferior = x[i] 
    límite_superior = x[i+1]
    print (límite_inferior , límite_superior)



#Límites SIN Superponerse
import numpy as np
cantidad_muestras=6
x= np.linspace (0,100,cantidad_muestras)

for i in range(cantidad_muestras-1):
    límite_inferior = x[i*2] 
    límite_superior = x[i*2+1]
    print (límite_inferior , límite_superior)
