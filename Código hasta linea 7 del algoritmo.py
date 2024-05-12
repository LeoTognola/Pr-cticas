import numpy as np

nMax= 10
epsilon= e-12

#Auxiliar fucniones al cuadrado
def A(t,f):
    return ((np.exp(-t*t/2) * np.sin(t*f*2*np.pi)))**2

#definir la función y sus parámetros

def g(t,f):
    return np.exp(-t*t/2) * np.sin(t*f*2*np.pi)

#intervalo de interés para t
#t=np.arange(-5,5,0.01)
t=np.arange(-5,5,0.5)

#Crear una lista vacía
lista_al_cuadrado=[]
lista_de_funciones=[]
lista_de_parametros=np.arange(-1,1,0.02)

#iterar sobre el parámetro deseado (f)
for f in lista_de_parametros:
    lista_al_cuadrado.append(A(t,f))
    lista_de_funciones.append(g(t, f))
        
#semilla (elección de frecuencia)
s=0

#Numerador=Función con semilla (s)
Numerador=lista_de_funciones[s]

#Denomiador es integral de (funcion al cuadrado)

integral= np.trapz(lista_al_cuadrado, t)

e=Numerador/integral[s]

rb=[e]

i=1
sigma=1

#Bucle
while (i<nMax) and (epsilon<sigma):
    i=i+1
    

#rb.append(e)