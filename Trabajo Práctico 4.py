
import random
notas = [random.randint(1, 10) for i in range(10)]

print(notas)

promedio = sum(notas) / len(notas)

print(f"Promedio de notas: {promedio}")

print("Nota más alta:", max(notas))
print("Nota más baja:", min(notas))