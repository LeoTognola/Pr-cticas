def funcion(x, y):
    return x**2 + y**2  # Esta es la función que quieres evaluar

rango_x = range(-5, 6)  # Definir el rango de valores para x
rango_y = range(-5, 6)  # Definir el rango de valores para y

for x in rango_x:
    for y in rango_y:
        resultado = funcion(x, y)
        print(f"Para x={x} y y={y}, el resultado es: {resultado}")
