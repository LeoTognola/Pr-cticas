#Parte del Algoritmo
#Cambiar según las correcciones-COMPLETAR
#PREGUNTAR COMO CALCULAR P() DEL ALGORITMO
#PREGUNTAR SI LAS INTEGRALES HECHAS SON LAS QUE SE PIDEN PARA CALCULAR e_i


import numpy as np
from scipy import integrate


#valores iniciales
sigma_1=1
I=1
epsilon=10e-12
n_max=5

# cantidad de valores tiempo
cantidad_muestras=5
rb=[]

x= np.linspace (-10,10,cantidad_muestras)
h= [np.exp(-x*x/2) * np.sin(x*0.99*2*np.pi), np.exp(-x*x/2) * np.sin(x*0.09*2*np.pi), np.exp(-x*x/2) * np.sin(x*0.21*2*np.pi), np.exp(-x*x/2) * np.sin(x*0.35*2*np.pi), np.exp(-x*x/2) * np.sin(x*0.85*2*np.pi)]  

# Matriz para almacenar los resultados de la integración y los errores
resultados_errores = np.zeros(((cantidad_muestras-1)*5, 3))  # Matriz de ceros con filas igual al número de límites y dos columnas (resultado, error)


def funcion_0(y):
    return ((np.exp(-y*y/2) * np.sin(y*0.99*2*np.pi)))**2
def funcion_1(y):
    return ((np.exp(-y*y/2) * np.sin(y*0.09*2*np.pi)))**2
def funcion_2(y):
    return ((np.exp(-y*y/2) * np.sin(y*0.21*2*np.pi)))**2
def funcion_3(y):
    return ((np.exp(-y*y/2) * np.sin(y*0.35*2*np.pi)))**2
def funcion_4(y):
    return ((np.exp(-y*y/2) * np.sin(y*0.85*2*np.pi)))**2


for j in range (5) :   
    for i in range(cantidad_muestras-1):
        límite_inferior = x[i] 
        límite_superior = x[i+1]
              
        # Calcula la integral definida
        if j == 0 :
            resultado, error = integrate.quad(funcion_0, límite_inferior, límite_superior)
        elif j==1:
             resultado, error = integrate.quad(funcion_1, límite_inferior, límite_superior)
        elif j == 2 :
            resultado, error = integrate.quad(funcion_2, límite_inferior, límite_superior)
        elif j==3:
             resultado, error = integrate.quad(funcion_3, límite_inferior, límite_superior)
        elif j==4:
             resultado, error = integrate.quad(funcion_4, límite_inferior, límite_superior)
        resultados_errores[(j*(cantidad_muestras-1))+i] = [resultado, error,j]

#primer elemento lista rb
e_1 = h[0][0]/resultados_errores[0][0]

#completar lista rb
rb=np.append(rb,e_1,axis=None)

while sigma > epsilon and I < n_max:
    I=I+1
