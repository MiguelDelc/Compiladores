from estructuras import Table, Queue, Hash

def demo():
    print("=== DEMO PILA ===")
    table = Table()
    table.apilar(10)
    table.apilar(20)
    table.apilar(30)
    print("Cima:", table.cima())
    print("Desapilar:", table.desapilar())
    print("Tamaño:", table.tamano())

    print("\n=== DEMO COLA ===")
    cola = Queue()
    cola.meter("A")
    cola.meter("B")
    cola.meter("C")
    print("Frente:", cola.frente())
    print("Desencolar:", cola.quitar())
    print("Tamaño:", cola.tamano())

    print("\n=== DEMO TABLA DICCIONARIO ===")
    hash = Hash()
    hash.insertar("nombre", "Andres")
    hash.insertar("edad", 25)
    hash.insertar("rol", "Desarrollador")
    print("Buscar 'nombre':", hash.buscar("nombre"))
    print("Claves:", hash.claves())
    print("Items:", hash.items())
    hash.eliminar("rol")
    print("Después de eliminar:", hash.items())


if __name__ == "__main__":
    demo()
