import numpy as np
import matplotlib.pyplot as plt

nMax = 10
epsilon = 1E-12

# Auxiliar funciones al cuadrado
def A(t, f):
    return ((np.exp(-t*t/2) * np.sin(t*f*2*np.pi)))**2

# Definir la función y sus parámetros
def g(t, f):
    return np.exp(-t*t/2) * np.sin(t*f*2*np.pi)

# Intervalo de interés para t
# t=np.arange(-5,5,0.01)
t = np.arange(-5, 5, 0.05)

# Diccionario para almacenar e con nombres
rb = []

# Crear una lista vacía
lista_al_cuadrado = []
lista_de_funciones = []
lista_de_parametros = np.arange(-1, 1, 0.2)

# Iterar sobre el parámetro deseado (f)
for f in lista_de_parametros:
    lista_al_cuadrado.append(A(t, f))
    lista_de_funciones.append(g(t, f))

# Semilla (elección de frecuencia)
s = 5

# Numerador = Función con semilla (s)
Numerador = lista_de_funciones[s]

# Denominador es integral de (funcion al cuadrado)
integral = np.trapz(lista_al_cuadrado, t)

R = np.sqrt(integral)

e = Numerador / R[s]

rb.append(e)

i = 1
sigma = 1

# Obtener el valor de coeficientes c
c = e * lista_de_funciones
integral1 = np.trapz(c, t)

# Lista para seleccionar la frecuencia
lista_valores = []

Ph=[]
# Obtener el valor de (P h)
for j in range(10):
    # Obtener el valor de (P h)
    Ph.append( integral1[j] * e)

    # Integrando para dsp calcular el módulo al cuadrado
    Integrando = (lista_de_funciones[j] - Ph[j])**2

    # Módulo al cuadrado para buscar el valor máx
    integral2 = np.trapz(Integrando, t)
    Módulo_al_cuadrado = integral2

    lista_valores.append(Módulo_al_cuadrado)


# Bucle
while i < nMax and epsilon < sigma:
 
    i = i + 1
#linea 8 del algoritmo
    maximo_valor = max(lista_valores)
    ubicacion_maximo = lista_valores.index(maximo_valor)
    s = ubicacion_maximo
        
    # Calcular el nuevo e
    l = lista_de_funciones[s] - Ph[s]  # paso 9 algoritmo

    # Denominador para paso 10 algoritmo
    l2 = l**2
    int_l2 = np.trapz(l2, t)  # modulo al cuadrado para el denominador de ei
    mod_l2 = np.sqrt(int_l2)

    e = l / mod_l2 
    
    rb.append(e)

    # CALCULO PARA SIGMA paso 12 del algoritmo
    # Obtener el valor de coeficientes c
    c = e * lista_de_funciones
    integral12 = np.trapz(c, t)

    # Lista para seleccionar la frecuencia
    lista_valores = []
    
    Ph1=[]
    
    # Obtener el valor de (P h)
    for j in range(10): 
        # Obtener el valor de (P h)
        Ph1.append(integral12[j] * e)
    
    PhT=[None]*10
    for j in range(10):
        PhT[j]=Ph[j]+Ph1[j]
        
    for j in range(10): 
    
        # Integrando para dsp calcular el módulo al cuadrado
        Integrando1 = (lista_de_funciones[j] - PhT[j])**2

        # Módulo al cuadrado para buscar el valor máx
        integral22 = np.trapz(Integrando1, t)
        Módulo_al_cuadrado1 = integral22

        lista_valores.append(Módulo_al_cuadrado1)
       
    error = max(lista_valores)
    print("Ubicación :" + str (s) + "   Error: " + str(error))
    sigma = error
    Ph=PhT

    
# Graficar cada función almacenada en rb
for i, e in enumerate(rb):
    plt.plot(t, e, label=f'Iteración {i+1}')

# Configurar los labels y título
plt.xlabel('t')
plt.ylabel('e(t)')
plt.title('Funciones almacenadas en rb')
plt.legend()

# Mostrar el gráfico
plt.show()