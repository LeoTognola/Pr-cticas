import numpy as np
from scipy import integrate

cantidad_muestras=6
x= np.linspace (-10,10,cantidad_muestras)

# Matriz para almacenar los resultados de la integración y los errores
resultados_errores = np.zeros(((cantidad_muestras-1)*5, 3))  # Matriz de ceros con filas igual al número de límites y dos columnas (resultado, error)


#funciones a integrar

def funcion_1(y):
    return ((np.exp(-y*y/2) * np.sin(y*0.99*2*np.pi)))**2
def funcion_2(y):
    return ((np.exp(-y*y/2) * np.sin(y*0.09*2*np.pi)))**2
def funcion_3(y):
    return ((np.exp(-y*y/2) * np.sin(y*0.21*2*np.pi)))**2
def funcion_4(y):
    return ((np.exp(-y*y/2) * np.sin(y*0.35*2*np.pi)))**2
def funcion_5(y):
    return ((np.exp(-y*y/2) * np.sin(y*0.85*2*np.pi)))**2


#ciclos para integrar cada funcion con cada par de limites

for j in range (5) :   
    for i in range(cantidad_muestras-1):
        límite_inferior = x[i] 
        límite_superior = x[i+1]
              
        # Calcula la integral definida
        if j == 0 :
            resultado, error = integrate.quad(funcion_1, límite_inferior, límite_superior)
        elif j==1:
             resultado, error = integrate.quad(funcion_2, límite_inferior, límite_superior)
        elif j == 2 :
            resultado, error = integrate.quad(funcion_3, límite_inferior, límite_superior)
        elif j==3:
             resultado, error = integrate.quad(funcion_4, límite_inferior, límite_superior)
        elif j==4:
             resultado, error = integrate.quad(funcion_5, límite_inferior, límite_superior)
        resultados_errores[(j*(cantidad_muestras-1))+i] = [resultado, error,j]

# Imprime el resultado
print( resultados_errores)
