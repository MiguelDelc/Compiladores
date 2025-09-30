# Estructuras de Datos en Python

Este proyecto implementa tres estructuras de datos clásicas como parte de la actividad de práctica:

- **Table (Stack – LIFO)**
- **Queue (FIFO)**
- **Hash (Dictionary – Clave/Valor)**

El objetivo es demostrar cómo funcionan estas estructuras y validar sus operaciones básicas.

---

## Librerías utilizadas

Se usaron librerías estándar de Python:

- **`list`**: usada para **Table**, permite agregar y quitar elementos al final de manera eficiente.
- **`collections.deque`**: usada para **Queue**, ya que permite encolar y desencolar elementos de forma rápida por ambos extremos.
- **`dict`**: usada para **Hash**, implementa una tabla hash que asocia claves con valores.

---

## Archivos del proyecto

- `estructuras.py` → contiene las clases `Table`, `Queue` y `Hash`.
- `main.py` → programa de demostración que ejecuta casos de prueba.
- `README.md` → documentación del proyecto.

---

## Funcionamiento de cada estructura

### Table (Stack – LIFO)
- Regla: último en entrar, primero en salir.  
- Operaciones:  
  - `apilar(x)` → inserta un elemento.  
  - `desapilar()` → elimina el último elemento.  
  - `cima()` → muestra el último sin eliminarlo.  

### Queue (FIFO)
- Regla: primero en entrar, primero en salir.  
- Operaciones:  
  - `meter(x)` → inserta al final.  
  - `quitar()` → elimina el primero.  
  - `frente()` → muestra el primero sin eliminarlo.  

### Hash (Dictionary)
- Regla: acceso mediante clave → valor.  
- Operaciones:  
  - `insertar(clave, valor)` → guarda un par.  
  - `eliminar(clave)` → borra un par.  
  - `buscar(clave)` → devuelve el valor asociado.  
  - `claves()`, `valores()`, `items()` → devuelven listas con las claves, valores o pares.  

---

## Cómo ejecutar

Clona el repositorio y ejecuta el archivo `main.py`:

```bash
python main.py
```
---

##Usé IA

- Utilicé un poco de chat para acordarme de como usar Python y un poco para asegurarme de implementar bien las clases y a su vez para saber    que liberías me convenía usar para implementarlas y que no fuera tan complicado

# Test Cases y Salida Esperada

## Test Cases diseñados

### Table (Stack – LIFO)
1. Insertar elementos: Apilar 10, 20, 30 → la cima debe ser 30.  
2. Desapilar un elemento: Desapilar → devuelve 30 (último insertado).  
3. Consultar cima después de desapilar: Debe devolver 20.  
4. Consultar tamaño: Debe ser 2 después de una extracción.  
5. Error al desapilar vacía: Intentar desapilar con table vacía debe lanzar `IndexError`.  

### Queue (FIFO)
6. Insertar elementos: Encolar A, B, C → el frente debe ser A.  
7. Desencolar un elemento: Desencolar → devuelve A (primero insertado).  
8. Consultar frente después de desencolar: Debe devolver B.  
9. Consultar tamaño: Debe ser 2 después de una extracción.  
10. Error al desencolar vacía: Intentar desencolar con queue vacía debe lanzar `IndexError`.  

### Hash (Dictionary)
11. Insertar elementos: Insertar ("nombre", "Andres"), ("edad", 25), ("rol", "Desarrollador").  
12. Buscar clave existente: Buscar "nombre" → devuelve "Andres".  
13. Listar claves: Debe mostrar ["nombre", "edad", "rol"].  
14. Listar items: Debe mostrar todos los pares clave–valor.  
15. Buscar clave inexistente: Buscar "ciudad" → devuelve `None`.  
16. Eliminar clave existente: Eliminar "rol" → ya no debe aparecer en los items.  
17. Error al eliminar clave inexistente: Intentar eliminar "ciudad" debe lanzar `KeyError`.  

---

## Salida esperada en consola

=== TEST CASES TABLE ===

Cima: 30

Desapilar: 30

Cima después de desapilar: 20

Tamaño actual: 2

Error esperado (table vacía): La table está vacía


=== TEST CASES QUEUE ===

Frente: A

Desencolar: A

Frente después de desencolar: B

Tamaño actual: 2

Error esperado (queue vacía): La queue está vacía


=== TEST CASES HASH ===

Buscar 'nombre': Andres

Claves: ['nombre', 'edad', 'rol']

Items: [('nombre', 'Andres'), ('edad', 25), ('rol', 'Desarrollador')]

Buscar 'ciudad': None

Después de eliminar 'rol': [('nombre', 'Andres'), ('edad', 25)]

Error esperado (clave inexistente): "La clave 'ciudad' no existe"




