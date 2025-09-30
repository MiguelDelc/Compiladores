from collections import deque

class Pila:
    def __init__(self):
        self.elementos = []

    def apilar(self, elemento):
        self.elementos.append(elemento)

    def desapilar(self):
        return self.elementos.pop()

    def cima(self):
        return self.elementos[-1]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)


class Cola:
    def __init__(self):
        self.elementos = deque()

    def meter(self, elemento):
        self.elementos.append(elemento)

    def quitar(self):
        return self.elementos.popleft()

    def frente(self):
        return self.elementos[0]

    def esta_vacia(self):
        return len(self.elementos) == 0

    def tamano(self):
        return len(self.elementos)


class TablaDiccionario:
    def __init__(self):
        self.tabla = dict()

    def insertar(self, clave, valor):
        self.tabla[clave] = valor

    def eliminar(self, clave):
        del self.tabla[clave]

    def buscar(self, clave):
        return self.tabla.get(clave)

    def claves(self):
        return list(self.tabla.keys())

    def valores(self):
        return list(self.tabla.values())

    def items(self):
        return list(self.tabla.items())

    def tamano(self):
        return len(self.tabla)
