import numpy as np

nMax= 10
epsilon= 1E-12

#(t en lugar de x, como variable; f en lugar de mu, como parámetro)

#Auxiliar funciones al cuadrado (para integrar y obtener el denominador en e)
def A(t,f):
    return ((np.exp(-t*t/2) * np.sin(t*f*2*np.pi)))**2

#definir la función y sus parámetros
def g(t,f):
    return np.exp(-t*t/2) * np.sin(t*f*2*np.pi)

#intervalo de interés para t
t=np.arange(-5,5,0.01)

#Crear una lista vacía
lista_al_cuadrado=[]
lista_de_funciones=[]
lista_de_parametros=np.arange(-1,1,0.2)

#la cantidad de valores en lista_de_parametros me da la cantidad de funciones. Una para cada valor de frecuencia

#iterar sobre el parámetro deseado (f)
for f in lista_de_parametros:
    lista_al_cuadrado.append(A(t,f))
    lista_de_funciones.append(g(t, f))
        
#semilla (elección de frecuencia. seleccionando el valor de f según el lugar que ocupe el elemento de la lista)
s=0

#Numerador=Función con semilla (s)
Numerador=lista_de_funciones[s]

#lista_de_funciones es un "array de arrays". al poner [s] selecciono la función (array) correspondiente a la frecuencia de la semilla

#Denomiador es integral de (funcion al cuadrado)
integral= np.trapz(lista_al_cuadrado, t)

#Sacar la raiz de cada valor obtenido por integrar
R= np.sqrt(integral)

e=Numerador/R[s]

#al usar [s] uso el valor que corresponde a la misma función usada en el numerador

rb=[e]
