import numpy as np

nMax= 10
epsilon= 1E-12

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
lista_de_parametros=np.arange(-1,1,0.2)

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

R= np.sqrt(integral)

e=Numerador/R[s]

rb=[e]

i=1
sigma=1

#Bucle
while i<nMax and epsilon<sigma:
   i=i+1

#P*h

#obtener el valor de coeficientes c
c=e*lista_de_funciones
integral1= np.trapz(c, t)

#lista para seleccionar la frecuencia
lista_valores=[]

#obtener el valor de (P h)
for j in range (10):
    
    #obtener el valor de (P h)
    Ph=integral1[j]*e
    
    #Integrando para dsp calcular el módulo al cuadrado
    Integrando=(lista_de_funciones[j]-Ph)**2

    #módulo al cuadrado para buscar el valor máx
    integral2= np.trapz(Integrando, t)
    Módulo_al_cuadrado=integral2

    lista_valores.append(Módulo_al_cuadrado)

maximo_valor = max(lista_valores)
ubicacion_maximo = lista_valores.index(maximo_valor)
w=ubicacion_maximo
print("El valor máximo es:", maximo_valor)
print("Su ubicación en la lista es:", ubicacion_maximo)
    
#rb.append(e)