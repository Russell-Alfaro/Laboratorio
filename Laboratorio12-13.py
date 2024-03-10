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





### Ejercicio 05 
###Implementar una función que cuente la cantidad de nodos en el árbol.


### Ejercicio 06 
### Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos).



### Ejercicio 07 
###Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo).


### Ejercicio 08 
### Implementar una función que calcule la altura del árbol (la longitud del camino más largo desde la raíz
### hasta una hoja).


### Ejercicio 09 
### Implementar una función que calcule la profundidad de un nodo (la longitud del camino desde la raíz
### hasta el nodo).



### Ejercicio 10 
### Implementar una función que encuentre el nodo con el valor mínimo en el árbol.


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



