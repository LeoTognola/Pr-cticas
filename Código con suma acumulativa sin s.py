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
t = np.arange(-5, 5, 0.1)

# Crear una lista vacía
lista_al_cuadrado = []
lista_de_funciones = []
lista_de_parametros = np.arange(-1, 1, 0.2)

# Iterar sobre el parámetro deseado (f)
for f in lista_de_parametros:
    lista_al_cuadrado.append(A(t, f))
    lista_de_funciones.append(g(t, f))

# Semilla (elección de frecuencia)
s = 3

# Numerador = Función con semilla (s)
Numerador = lista_de_funciones[s]

# Denominador es integral de (funcion al cuadrado)
integral = np.trapz(lista_al_cuadrado, t)

R = np.sqrt(integral)

e = Numerador / R[s]

# Diccionario para almacenar e con nombres
rb = {'e1': e}
unique_rb = {tuple(e)}  # Conjunto para verificar duplicados

# Lista para almacenar la suma acumulativa de Ph
suma_acumulativa_Ph = np.zeros_like(e)

i = 1
sigma = 1

# Bucle
while i < nMax and epsilon < sigma:
    i += 1
    
    # Obtener el valor de coeficientes c
    c = np.array([np.trapz(e * f, t) for f in lista_de_funciones])

    # Lista para seleccionar la frecuencia
    lista_valores = []

    # Obtener el valor de (P h)
    for j in range(10):
        # Obtener el valor de (P h)
        Ph = c[j] * e
        
        # Actualizar la suma acumulativa de Ph
        suma_acumulativa_Ph += Ph
        
        # Integrando para dsp calcular el módulo al cuadrado
        Integrando = (lista_de_funciones[j] - suma_acumulativa_Ph)**2

        # Módulo al cuadrado para buscar el valor máx
        integral2 = np.trapz(Integrando, t)
        Módulo_al_cuadrado = integral2

        lista_valores.append(Módulo_al_cuadrado)

    maximo_valor = max(lista_valores)
    ubicacion_maximo = lista_valores.index(maximo_valor)
    s = ubicacion_maximo

    #print (s) 
    print(f"Iteración {i}: s = {s}, Error = {maximo_valor}")
    
    # Calcular ei
    l = lista_de_funciones[s] - c[s] * e  # paso 9 algoritmo

    # Denominador para paso 10 algoritmo
    l2 = l**2
    int_l2 = np.trapz(l2, t)  # modulo al cuadrado para el denominador de ei
    mod_l2 = np.sqrt(int_l2)

    e = l / mod_l2 
    
    if tuple(e) not in unique_rb:
        rb[f'e{i}'] = e  # paso 11 del algoritmo
        unique_rb.add(tuple(e))

    # CALCULO PARA SIGMA paso 12 del algoritmo
    # Obtener el valor de coeficientes c
    c = np.array([np.trapz(e * f, t) for f in lista_de_funciones])

    # Lista para seleccionar la frecuencia
    lista_valores1 = []

    # Obtener el valor de (P h)
    for j in range(10):
        # Obtener el valor de (P h)
        Ph1 = c[j] * e
    
        # Integrando para dsp calcular el módulo al cuadrado
        Integrando1 = (lista_de_funciones[j] - Ph1)**2

        # Módulo al cuadrado para buscar el valor máx
        integral22 = np.trapz(Integrando1, t)
        Módulo_al_cuadrado1 = integral22

        lista_valores1.append(Módulo_al_cuadrado1)
        
    error = max(lista_valores1)
    sigma = error

# Imprimir la suma acumulativa de Ph
#print('Suma acumulativa de Ph:')
#print(suma_acumulativa_Ph)

# Graficar la suma acumulativa de Ph
#plt.plot(t, suma_acumulativa_Ph, label='Suma acumulativa de Ph')

#plt.xlabel('t')
#plt.ylabel('Suma acumulativa de Ph(t)')
#plt.title('Suma acumulativa de Ph en cada iteración')

# Imprimir resultados
for key, value in rb.items():
    print(f'{key}: {value}')

# Graficar resultados
for key, value in rb.items():
    plt.plot(t, value, label=key)

plt.xlabel('t')
plt.ylabel('e(t)')
plt.title('Evolución de e en cada iteración')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))  # Mover la leyenda a la derecha
plt.tight_layout()  # Ajustar el diseño para que todo se vea bien
plt.show()
