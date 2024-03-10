### LABORATORIO 12 Y 13

### Ejercicio 01
###Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para
###comparar los caracteres de la palabra en orden original y reverso.

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def encolar(self, item):
        self.items.append(item)

    def desencolar(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None


def es_palindroma(palabra):
    cola = Cola()

    # Encolar los caracteres de la palabra en orden original
    for caracter in palabra:
        cola.encolar(caracter)

    # Construir la palabra en orden reverso desencolando los caracteres
    palabra_reverso = ""
    while not cola.esta_vacia():
        palabra_reverso += cola.desencolar()

    # Comparar la palabra original con la palabra en orden reverso
    return palabra == palabra_reverso


# Ejemplo de uso
palabra = "radar"
if es_palindroma(palabra):
    print(f"{palabra} es palíndroma.")
else:
    print(f"{palabra} no es palíndroma.")

### Ejercicio 02
###Crea un sistema de gestión de pedidos que utilice una cola para procesar los pedidos en el orden en que
###fueron recibidos. Implementa funciones para agregar pedidos, procesar pedidos y mostrar el estado
###actual de la cola.

class ColaPedidos:
    def __init__(self):
        self.pedidos = []

    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)
        print(f"Pedido agregado: {pedido}")

    def procesar_pedido(self):
        if self.pedidos:
            pedido = self.pedidos.pop(0)
            print(f"Procesando pedido: {pedido}")
        else:
            print("No hay pedidos para procesar")

    def mostrar_estado(self):
        if self.pedidos:
            print("Pedidos pendientes:")
            for pedido in self.pedidos:
                print(pedido)
        else:
            print("No hay pedidos pendientes")


# Ejemplo de uso
cola = ColaPedidos()
cola.agregar_pedido("Pedido 1")
cola.agregar_pedido("Pedido 2")
cola.agregar_pedido("Pedido 3")

cola.mostrar_estado()
cola.procesar_pedido()
cola.mostrar_estado()
cola.procesar_pedido()
cola.mostrar_estado()
cola.procesar_pedido()

### Ejercicio 03
###Desarrolla un programa que encuentre el camino más corto a través de un laberinto. Utiliza una cola
###para realizar un recorrido en anchura (BFS) desde el punto de inicio hasta el punto de destino.

from collections import deque

def encontrar_camino_mas_corto(laberinto, inicio, destino):
    # Dimensiones del laberinto
    filas = len(laberinto)
    columnas = len(laberinto[0])

    # Movimientos posibles: arriba, abajo, izquierda, derecha
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Cola para el recorrido BFS
    cola = deque([(inicio, 0)])  # Cada elemento de la cola es una tupla (coordenada, distancia)

    # Conjunto para marcar las celdas visitadas
    visitado = set()
    visitado.add(inicio)

    # Bucle principal del BFS
    while cola:
        (x, y), distancia = cola.popleft()

        # Verificar si alcanzamos el destino
        if (x, y) == destino:
            return distancia

        # Explorar los movimientos posibles
        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy
            if 0 <= nx < filas and 0 <= ny < columnas and laberinto[nx][ny] == 0 and (nx, ny) not in visitado:
                cola.append(((nx, ny), distancia + 1))
                visitado.add((nx, ny))

    # Si no se encuentra un camino al destino
    return -1

# Ejemplo de uso
laberinto = [
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1]
]
inicio = (0, 0)
destino = (4, 4)

distancia_mas_corta = encontrar_camino_mas_corto(laberinto, inicio, destino)
if distancia_mas_corta != -1:
    print(f"El camino más corto desde {inicio} hasta {destino} es de {distancia_mas_corta} pasos.")
else:
    print(f"No hay un camino desde {inicio} hasta {destino}.")


### Ejercicio 04 
###Implementa un sistema de gestión de tareas que permita agregar tareas, marcar tareas como
###completadas y mostrar la próxima tarea pendiente.

class SistemaGestionTareas:
    def __init__(self):
        self.tareas_pendientes = []

    def agregar_tarea(self, tarea):
        self.tareas_pendientes.append(tarea)
        print(f"Tarea agregada: {tarea}")

    def completar_tarea(self):
        if self.tareas_pendientes:
            tarea_completada = self.tareas_pendientes.pop(0)
            print(f"Tarea completada: {tarea_completada}")
        else:
            print("No hay tareas pendientes para completar.")

    def mostrar_proxima_tarea_pendiente(self):
        if self.tareas_pendientes:
            print(f"Próxima tarea pendiente: {self.tareas_pendientes[0]}")
        else:
            print("No hay tareas pendientes.")

# Ejemplo de uso
sistema_tareas = SistemaGestionTareas()

sistema_tareas.agregar_tarea("Hacer la compra")
sistema_tareas.agregar_tarea("Llamar al cliente")
sistema_tareas.agregar_tarea("Enviar informe")

sistema_tareas.mostrar_proxima_tarea_pendiente()

sistema_tareas.completar_tarea()

sistema_tareas.mostrar_proxima_tarea_pendiente()



### Ejercicio 05 
###Implementar una función que cuente la cantidad de nodos en el árbol.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos(arbol):
    if not arbol:
        return 0
    else:
        cantidad_nodos = 1  # Contar el nodo actual
        for hijo in arbol.hijos:
            cantidad_nodos += contar_nodos(hijo)  # Recursivamente contar los nodos de cada hijo
        return cantidad_nodos

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)

raiz.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4]
nodo3.hijos = [nodo5]

# Contamos los nodos del árbol
cantidad_nodos = contar_nodos(raiz)
print("Cantidad de nodos en el árbol:", cantidad_nodos)


### Ejercicio 06 
### Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_hoja(arbol):
    if not arbol:
        return 0
    elif not arbol.hijos:
        return 1  # El nodo es una hoja
    else:
        cantidad_nodos_hoja = 0
        for hijo in arbol.hijos:
            cantidad_nodos_hoja += contar_nodos_hoja(hijo)
        return cantidad_nodos_hoja

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

raiz.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4]
nodo3.hijos = [nodo5, nodo6]

# Contamos los nodos hoja del árbol
cantidad_nodos_hoja = contar_nodos_hoja(raiz)
print("Cantidad de nodos hoja en el árbol:", cantidad_nodos_hoja)

### Ejercicio 07 
###Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def contar_nodos_internos(arbol):
    if not arbol:
        return 0
    elif not arbol.hijos:
        return 0  # El nodo es una hoja
    else:
        cantidad_nodos_internos = 1  # Contar el nodo actual como interno
        for hijo in arbol.hijos:
            cantidad_nodos_internos += contar_nodos_internos(hijo)
        return cantidad_nodos_internos

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

raiz.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4]
nodo3.hijos = [nodo5, nodo6]

# Contamos los nodos internos del árbol
cantidad_nodos_internos = contar_nodos_internos(raiz)
print("Cantidad de nodos internos en el árbol:", cantidad_nodos_internos)

### Ejercicio 08 
### Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz
### hasta una hoja).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def altura_arbol(arbol):
    if not arbol:
        return 0
    elif not arbol.hijos:
        return 1
    else:
        alturas_subarboles = [altura_arbol(hijo) for hijo in arbol.hijos]
        return max(alturas_subarboles) + 1


# Creamos un árbol de ejemplo
raiz = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

raiz.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4]
nodo3.hijos = [nodo5, nodo6]

# Calculamos la altura del árbol
altura = altura_arbol(raiz)
print("Altura del árbol:", altura)


### Ejercicio 09 
### Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz
### hasta el nodo).

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def profundidad_nodo(raiz, valor_nodo, profundidad=0):
    if raiz is None:
        return -1  # Si no hay nodo, la profundidad es -1
    if raiz.valor == valor_nodo:
        return profundidad  # Si encontramos el nodo, devolvemos la profundidad actual
    for hijo in raiz.hijos:
        profundidad_hijo = profundidad_nodo(hijo, valor_nodo, profundidad + 1)
        if profundidad_hijo != -1:
            return profundidad_hijo
    return -1  # Si el nodo no está en el subárbol, devolvemos -1

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo5 = Nodo(5)
nodo6 = Nodo(6)

raiz.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4]
nodo3.hijos = [nodo5, nodo6]

# Calculamos la profundidad del nodo con valor 5
valor_nodo = 5
profundidad = profundidad_nodo(raiz, valor_nodo)
print(f"Profundidad del nodo {valor_nodo}: {profundidad}")

### Ejercicio 10 
### Implementar una función que encuentre el nodo con el valor mínimo en el árbol.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

def encontrar_minimo(raiz):
    if raiz is None:
        return float('inf')  # Si el árbol está vacío, devolvemos infinito
    min_valor = raiz.valor
    for hijo in raiz.hijos:
        min_hijo = encontrar_minimo(hijo)
        min_valor = min(min_valor, min_hijo)
    return min_valor

# Ejemplo de uso
# Creamos un árbol de ejemplo
raiz = Nodo(10)
nodo2 = Nodo(5)
nodo3 = Nodo(15)
nodo4 = Nodo(3)
nodo5 = Nodo(7)
nodo6 = Nodo(12)

raiz.hijos = [nodo2, nodo3]
nodo2.hijos = [nodo4, nodo5]
nodo3.hijos = [nodo6]

# Encontramos el valor mínimo en el árbol
minimo = encontrar_minimo(raiz)
print("Valor mínimo en el árbol:", minimo)

### Ejercicio 11 
### Implementar una función que encuentre el nodo con el valor máximo en el árbol.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

def nodo_maximo(arbol):
    if arbol is None:
        return None
    while arbol.derecha:
        arbol = arbol.derecha
    return arbol

# Ejemplo de uso
# Creamos un árbol de ejemplo
arbol = Nodo(10)
arbol.izquierda = Nodo(5)
arbol.derecha = Nodo(15)
arbol.izquierda.izquierda = Nodo(3)
arbol.izquierda.derecha = Nodo(8)
arbol.derecha.derecha = Nodo(20)

# Encontramos el nodo con el valor máximo
nodo_max = nodo_maximo(arbol)
print("El valor máximo en el árbol es:", nodo_max.valor)



