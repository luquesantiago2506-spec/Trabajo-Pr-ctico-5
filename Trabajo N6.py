
# 1.

def imprimir_hola_mundo():
    print("Hola Mundo!")

if __name__ == "__main__":
    imprimir_hola_mundo()

# 2. 

def saludar_usuario(nombre):
    return f"Hola {nombre}!"

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    print(saludar_usuario(nombre))

# 3.

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

if __name__ == "__main__":
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)


# 4.

import math

def calcular_area_circulo(radio):
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

if __name__ == "__main__":
    radio = float(input("Ingrese el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")


# 5.

def segundos_a_horas(segundos):
    return segundos / 3600

if __name__ == "__main__":
    segundos = int(input("Ingrese la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# 6.

def tabla_multiplicar(numero):
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

if __name__ == "__main__":
    numero = int(input("Ingrese un número: "))
    tabla_multiplicar(numero)

# 7.

def operaciones_basicas(a, b):
    """
    Devuelve (suma, resta, multiplicacion, division).
    Si b es 0, la división será None.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else None
    return (suma, resta, multiplicacion, division)

if __name__ == "__main__":
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
    except ValueError:
        print("Entrada inválida. Debe ingresar números.")
    else:
        suma, resta, multiplicacion, division = operaciones_basicas(a, b)
        print(f"Suma: {suma}")
        print(f"Resta: {resta}")
        print(f"Multiplicación: {multiplicacion}")
        if division is None:
            print("División: indefinida (no se puede dividir por cero).")
        else:
            print(f"División: {division}")

# 8.

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

if __name__ == "__main__":
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros (ej. 1.70): "))
        if altura <= 0:
            print("La altura debe ser mayor a 0.")
        else:
            imc = calcular_imc(peso, altura)
            print(f"Su IMC es: {imc:.2f}")
    except ValueError:
        print("Entrada inválida. Use números (ej. 70.5, 1.75).")


# 9.

def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

if __name__ == "__main__":
    try:
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius:.2f} °C equivalen a {fahrenheit:.2f} °F")
    except ValueError:
        print("Entrada inválida. Ingrese un número (ej. 23.5).")

# 10.

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

if __name__ == "__main__":
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        c = float(input("Ingrese el tercer número: "))
        promedio = calcular_promedio(a, b, c)
        print(f"El promedio es: {promedio:.2f}")
    except ValueError:
        print("Entrada inválida. Ingrese solo números.")
