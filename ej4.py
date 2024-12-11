# Variables
numero1 = 2
numero2 = 3
resultado = 0


# Función para simular la acción al presionar un botón
def boton_click():
    global resultado
    resultado = numero1 + numero2
    print("El resultado es")
    print(resultado)


# Simulación de presionar boton (llamamos a la función aquí mismo)
boton_click()