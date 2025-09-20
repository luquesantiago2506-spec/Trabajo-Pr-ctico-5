
# Trabajo Práctico 5: Listas #

# 1. #

import random
notas = [random.randint(1, 10) for i in range(10)]

print(notas)

promedio = sum(notas) / len(notas)

print(f"Promedio de notas: {promedio}")

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))

# 2. #

productos = []

print("Cargá 5 productos:")
for i in range(5):
    p = input(f"Producto {i+1}: ").strip()
    productos.append(p)

ordenada = sorted(productos)
print("\nLista ordenada:", ordenada)

a_eliminar = input("\n¿Qué producto querés eliminar? ").strip()

if a_eliminar in productos:
    productos.remove(a_eliminar)
    print("Producto eliminado.")
else:
    print("Ese producto no está en la lista.")

print("\nLista actualizada:", productos)

# 3. #

import random

numeros = []
for _ in range(15):
    numeros.append(random.randint(1, 100))

pares = []
impares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

print("Lista original:", numeros)
print("Pares:", pares)
print("Impares:", impares)
print("Cantidad de pares:", len(pares))
print("Cantidad de impares:", len(impares))

# 4. #

datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

sin_repeticiones = []
for x in datos:
    if x not in sin_repeticiones:
        sin_repeticiones.append(x)

print(sin_repeticiones)

# 5. #

nums = [1, 2, 3, 4, 5, 6, 7]

ultimo = nums[-1]
for i in range(len(nums)-1, 0, -1):
    nums[i] = nums[i-1]
nums[0] = ultimo

print(nums)

# NOTA: sigo trabajando en los próximos ejerciios. Actualizaré mi trabajo en GitHub cuando los tenga completados. #

