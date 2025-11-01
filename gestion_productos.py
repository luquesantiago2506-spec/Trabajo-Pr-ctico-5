
# Gestión de Productos

from pathlib import Path

ARCHIVO = Path("productos.txt")

# 

def crear_archivo_inicial():
    """(1) Crear archivo inicial con 3 productos si no existe."""
    if not ARCHIVO.exists():
        inicial = [
            {"nombre": "Lapicera", "precio": 120.5, "cantidad": 30},
            {"nombre": "Cuaderno", "precio": 850.0, "cantidad": 10},
            {"nombre": "Goma", "precio": 95.0, "cantidad": 50},
        ]
        with ARCHIVO.open("w", encoding="utf-8") as f:
            for p in inicial:
                f.write(f'{p["nombre"]},{p["precio"]},{p["cantidad"]}\n')

def leer_productos():
    """(2) Leer archivo y (4) cargar en lista de diccionarios."""
    productos = []
    if not ARCHIVO.exists():
        return productos
    with ARCHIVO.open("r", encoding="utf-8") as f:
        for linea in f:
            linea = linea.strip()
            if not linea:
                continue
            partes = linea.split(",")
            if len(partes) != 3:
                continue
            nombre = partes[0].strip()
            try:
                precio = float(partes[1].replace(",", "."))
                cantidad = int(partes[2])
            except ValueError:
                continue
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    return productos

def mostrar(productos):
    """(2) Mostrar en formato pedido."""
    if not productos:
        print("No hay productos para mostrar.")
        return
    for p in productos:
        print(f'Producto: {p["nombre"]} | Precio: ${p["precio"]} | Cantidad: {p["cantidad"]}')

def pedir_nuevo_producto():
    """(3) Pedir y validar nuevo producto desde teclado."""
    print("\nIngresá un nuevo producto (nombre, precio, cantidad).")
    nombre = input("Nombre: ").strip()
    precio_txt = input("Precio: ").strip().replace(",", ".")
    cantidad_txt = input("Cantidad: ").strip()
    try:
        precio = float(precio_txt)
        cantidad = int(cantidad_txt)
    except ValueError:
        print("Datos inválidos. No se agregó el producto.")
        return None
    return {"nombre": nombre, "precio": precio, "cantidad": cantidad}

def append_a_archivo(producto):
    """(3) Agregar al archivo sin borrar el contenido existente (modo 'a')."""
    with ARCHIVO.open("a", encoding="utf-8") as f:
        f.write(f'{producto["nombre"]},{producto["precio"]},{producto["cantidad"]}\n')

def buscar_por_nombre(productos, nombre):
    """(5) Búsqueda exacta por nombre (case-insensitive)."""
    nombre = nombre.strip().lower()
    for p in productos:
        if p["nombre"].lower() == nombre:
            return p
    return None

def guardar_todos(productos):
    """(6) Sobrescribir el archivo con todos los productos actualizados (modo 'w')."""
    with ARCHIVO.open("w", encoding="utf-8") as f:
        for p in productos:
            f.write(f'{p["nombre"]},{p["precio"]},{p["cantidad"]}\n')

# 

def main():
    crear_archivo_inicial()
    productos = leer_productos()
    print("\n=== Listado de productos ===")
    mostrar(productos)

    nuevo = pedir_nuevo_producto()
    if nuevo:
        append_a_archivo(nuevo)
        productos.append(nuevo)

    nombre_buscar = input("\nIngresá un nombre para buscar: ").strip()
    encontrado = buscar_por_nombre(productos, nombre_buscar)  # (5)
    if encontrado:
        print(f'Encontrado → Producto: {encontrado["nombre"]} | Precio: ${encontrado["precio"]} | Cantidad: {encontrado["cantidad"]}')
    else:
        print("No existe un producto con ese nombre.")

    guardar_todos(productos)
    print("\nCambios guardados en productos.txt")

if __name__ == "__main__":
    main()
