from estructuras import Pila, Cola, TablaDiccionario

def demo():
    print("=== DEMO PILA ===")
    pila = Pila()
    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)
    print("Cima:", pila.cima())
    print("Desapilar:", pila.desapilar())
    print("Tamaño:", pila.tamano())

    print("\n=== DEMO COLA ===")
    cola = Cola()
    cola.meter("A")
    cola.meter("B")
    cola.meter("C")
    print("Frente:", cola.frente())
    print("Desencolar:", cola.quitar())
    print("Tamaño:", cola.tamano())

    print("\n=== DEMO TABLA DICCIONARIO ===")
    tabla = TablaDiccionario()
    tabla.insertar("nombre", "Andres")
    tabla.insertar("edad", 25)
    tabla.insertar("rol", "Desarrollador")
    print("Buscar 'nombre':", tabla.buscar("nombre"))
    print("Claves:", tabla.claves())
    print("Items:", tabla.items())
    tabla.eliminar("rol")
    print("Después de eliminar:", tabla.items())


if __name__ == "__main__":
    demo()
