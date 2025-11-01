

# 1.

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Añadir nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

precios_frutas

# 2.

precios_frutas.update({
    'Banana': 1330,
    'Manzana': 1700,
    'Melón': 2800
})

precios_frutas


# 3. Lista con únicamente los nombres de las frutas

frutas = list(precios_frutas.keys())
frutas


# 4. Agenda de 5 contactos y consulta por nombre

contactos = {}

for i in range(1, 6):
    nombre = input(f"Ingresá el nombre del contacto #{i}: ").strip()
    telefono = input(f"Ingresá el teléfono de {nombre}: ").strip()
    contactos[nombre] = telefono

buscado = input("Ingresá el nombre a consultar: ").strip()
numero = contactos.get(buscado)

if numero is not None:
    print(f"El número de {buscado} es: {numero}")
else:
    print(f"No se encontró el contacto '{buscado}'.")


# 5) Pedir una frase, mostrar palabras únicas

import re

frase = input("Ingresá una frase: ")

# Separar palabras ignorando mayúsculas y signos
palabras = re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]+", frase.lower())

palabras_unicas = set(palabras)

recuento = {}
for p in palabras:
    recuento[p] = recuento.get(p, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Recuento:", recuento)


# 6) Nombres de 3 alumnos

alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ").strip()
    notas = []
    for j in range(3):
        nota = float(input(f"Nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

print("\nPromedios:")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / 3
    print(f"{nombre}: notas={notas} -> promedio={promedio:.2f}")


# 7.

parcial1 = {"Ana", "Luis", "Sofía", "Marcos"}
parcial2 = {"Sofía", "Marcos", "Carla", "Iván"}

ambos = parcial1 & parcial2

solo_uno = parcial1 ^ parcial2

al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)


# 8. Diccionario: producto - stock

stock = {}

def leer_entero_no_negativo(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 0:
                print("Ingresá un entero no negativo.")
                continue
            return n
        except ValueError:
            print("Número inválido. Probá de nuevo.")

def buscar_clave(dic, nombre):
    for k in dic:
        if k.casefold() == nombre.casefold():
            return k
    return None

while True:
    print("\nMenú:")
    print("1) Consultar stock")
    print("2) Agregar unidades a un producto existente")
    print("3) Agregar un producto nuevo")
    print("4) Salir")
    op = input("Elegí una opción: ").strip()

    if op == "1":
        nombre = input("Producto a consultar: ").strip()
        k = buscar_clave(stock, nombre)
        if k is not None:
            print(f"Stock de {k}: {stock[k]}")
        else:
            print(f"'{nombre}' no existe en el inventario.")

    elif op == "2":
        nombre = input("Producto a actualizar: ").strip()
        k = buscar_clave(stock, nombre)
        if k is None:
            print(f"'{nombre}' no existe. Usá la opción 3 para crearlo.")
            continue
        cant = leer_entero_no_negativo(f"Unidades a agregar a {k}: ")
        stock[k] += cant
        print(f"Nuevo stock de {k}: {stock[k]}")

    elif op == "3":
        nombre = input("Nombre del nuevo producto: ").strip()
        k = buscar_clave(stock, nombre)
        if k is not None:
            print(f"{k} ya existe con stock {stock[k]}.")
            cant = leer_entero_no_negativo(f"Unidades a agregar a {k}: ")
            stock[k] += cant
            print(f"Nuevo stock de {k}: {stock[k]}")
        else:
            cant = leer_entero_no_negativo(f"Stock inicial de {nombre}: ")
            stock[nombre] = cant
            print(f"Se agregó '{nombre}' con stock {cant}.")

    elif op == "4":
        print("Fin del programa.")
        break

    else:
        print("Opción inválida.")


# 9.

agenda = {
    ("lunes",  "10:00"): "Reunión",
    ("martes", "15:00"): "Clase de inglés",
    ("viernes","18:30"): "Gimnasio",
}

def norm_dia(d):
    return d.strip().casefold()

dia  = input("Día a consultar (ej. lunes): ")
hora = input("Hora a consultar (HH:MM): ")

evento = agenda.get((norm_dia(dia), hora.strip()))
if evento:
    print(f"En {dia} a las {hora} hay: {evento}")
else:
    print(f"No hay actividad para {dia} a las {hora}.")

# 10.

def invertir_paises_capitales(original):
    return {capital: pais for pais, capital in original.items()}

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = invertir_paises_capitales(original)

print(invertido)

