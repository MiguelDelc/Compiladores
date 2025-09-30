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
#Usé IA
Utilicé un poco de chat para acordarme de como usar Python y un poco para asegurarme de implementar bien las clases y a su vez para saber que liberías me convenía usar para implementarlas y que no fuera tan complicado

#Casos de uso
