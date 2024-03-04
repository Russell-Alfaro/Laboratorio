### LABORATORIO 10 Y 11

### Ejercicio 01
### Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime la lista original y la lista
###duplicada hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.anterior
        print("None")

def duplicar_nodos(lista):
    actual = lista.cabeza
    while actual:
        duplicado = Nodo(actual.valor)
        siguiente = actual.siguiente
        actual.siguiente = duplicado
        duplicado.anterior = actual
        if siguiente:
            duplicado.siguiente = siguiente
            siguiente.anterior = duplicado
        else:
            lista.cola = duplicado
        actual = siguiente

# Crear la lista original
lista_original = ListaEnlazada()
lista_original.insertar_al_principio(4)
lista_original.insertar_al_principio(3)
lista_original.insertar_al_principio(2)
lista_original.insertar_al_principio(1)

# Duplicar los nodos de la lista original
duplicar_nodos(lista_original)

# Imprimir la lista original hacia adelante y hacia atrás
print("Lista original hacia adelante:")
lista_original.imprimir_adelante()
print("Lista original hacia atrás:")
lista_original.imprimir_atras()

### Ejercicio 02
###Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato
###impar e imprime la lista hacia adelante y hacia atrás.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.anterior
        print("None")

    def contar_pares_impares(self):
        pares = impares = 0
        actual = self.cabeza
        while actual:
            if actual.valor % 2 == 0:
                pares += 1
            else:
                impares += 1
            actual = actual.siguiente
        return pares, impares

# Crear la lista
lista = ListaEnlazada()
lista.insertar_al_principio(9)
lista.insertar_al_principio(8)
lista.insertar_al_principio(7)
lista.insertar_al_principio(6)
lista.insertar_al_principio(5)
lista.insertar_al_principio(4)
lista.insertar_al_principio(3)
lista.insertar_al_principio(2)
lista.insertar_al_principio(1)

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()

# Contar nodos con datos pares e impares
pares, impares = lista.contar_pares_impares()
print("Nodos con dato par:", pares)
print("Nodos con dato impar:", impares)

### Ejercicio 03
###Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la
###lista hacia adelante y hacia atrás.


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def insertar_en_posicion(self, valor, posicion):
        nuevo_nodo = Nodo(valor)
        if posicion == 1:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for _ in range(2, posicion):
                if actual.siguiente:
                    actual = actual.siguiente
                else:
                    break
            siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual
            if siguiente:
                nuevo_nodo.siguiente = siguiente
                siguiente.anterior = nuevo_nodo
            else:
                self.cola = nuevo_nodo

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.anterior
        print("None")

# Crear la lista
lista = ListaEnlazada()
lista.insertar_al_principio(5)
lista.insertar_al_principio(4)
lista.insertar_al_principio(3)
lista.insertar_al_principio(2)
lista.insertar_al_principio(1)

# Insertar un nuevo nodo en la posición 3 con el dato 15
lista.insertar_en_posicion(15, 3)

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
lista.imprimir_adelante()
print("Lista hacia atrás:")
lista.imprimir_atras()

### EJERCICIOS 04
###Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando
###solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def eliminar_duplicados(self):
        valores_vistos = set()
        actual = self.cabeza
        while actual:
            if actual.valor in valores_vistos:
                siguiente = actual.siguiente
                if siguiente:
                    actual.anterior.siguiente = siguiente
                    siguiente.anterior = actual.anterior
                else:
                    actual.anterior.siguiente = None
                    self.cola = actual.anterior
            else:
                valores_vistos.add(actual.valor)
            actual = actual.siguiente
# Función para imprimir la lista enlazada hacia adelante
    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
# Función para imprimir la lista enlazada hacia atras
    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.anterior
        print("None")

# Crear la lista con nodos duplicados
lista = ListaEnlazada()
lista.insertar_al_principio(3)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)
lista.insertar_al_principio(4)
lista.insertar_al_principio(5)
lista.insertar_al_principio(4)
lista.insertar_al_principio(6)

# Eliminar los nodos duplicados
lista.eliminar_duplicados()

# Imprimir la lista hacia adelante y hacia atrás
print("Lista sin nodos duplicados hacia adelante:")
lista.imprimir_adelante()
print("Lista sin nodos duplicados hacia atrás:")
lista.imprimir_atras()

### Ejercicio 05
###Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el
###primero y viceversa) e imprime la lista hacia adelante y hacia atrás.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
        self.anterior = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo

    def invertir(self):
        actual = self.cabeza
        nueva_cola = None
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = actual.anterior
            actual.anterior = siguiente
            nueva_cola = actual
            actual = siguiente
        self.cabeza, self.cola = nueva_cola, self.cabeza

    def imprimir_adelante(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def imprimir_atras(self):
        actual = self.cola
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.anterior
        print("None")

# Crear la lista con al menos 6 nodos
lista = ListaEnlazada()
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)
lista.insertar_al_principio(4)
lista.insertar_al_principio(5)
lista.insertar_al_principio(6)

# Invertir el orden de la lista
lista.invertir()

# Imprimir la lista hacia adelante y hacia atrás
print("Lista invertida hacia adelante:")
lista.imprimir_adelante()
print("Lista invertida hacia atrás:")
lista.imprimir_atras()

### Ejercicio 06
###Utilizar una pila para invertir el orden de los caracteres de una cadena.

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()


def invertir_cadena_con_pila(cadena):
    pila = Pila()
    for caracter in cadena:
        pila.apilar(caracter)

    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.desapilar()

    return cadena_invertida


# Ejemplo de uso
cadena_original = "Hola mundo!"
cadena_invertida = invertir_cadena_con_pila(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)

### Ejercicio 07
###Implementar un programa que convierta un número decimal a su representación en sistema binario
### utilizando una pila 

class Pila:
    def __ini__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self,elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pula esta vacia, No se puede desapilar")
    def cima(self):
        if not self.esta_vacia():
            return self.item[-1]
        else: print("La pila esta vacia")
def decimal_a_binario(numero):
    pila = Pila()
    binario = ""
    while numero > 0:
        residuo = numero %2
        pila.apilar(residuo)
        numero//=2

    while not pila.esta_vacia():
        binario += str(Pila.desapilar())

    return binario
a=(input("Escoja un numero: "))
binario = decimal_a_binario(a)
print(f"{binario}")

### Ejercicio 08
### Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pil
class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        else:
            print("La pila está vacía. No se puede desapilar.")
            return None

def evaluar_operacion(operando1, operando2, operador):
    if operador == '+':
        return operando1 + operando2
    elif operador == '-':
        return operando1 - operando2
    elif operador == '*':
        return operando1 * operando2
    elif operador == '/':
        return operando1 / operando2
    else:
        raise ValueError("Operador no válido.")

def evaluar_expresion_posfija(expresion):
    pila = Pila()

    for elemento in expresion.split():
        if elemento.isdigit():
            pila.apilar(int(elemento))
        else:
            segundo_operando = pila.desapilar()
            primer_operando = pila.desapilar()
            resultado = evaluar_operacion(primer_operando, segundo_operando, elemento)
            pila.apilar(resultado)

    return pila.desapilar()

# Ejemplo de uso
expresion_posfija = "3 4 + 2 *"
resultado = evaluar_expresion_posfija(expresion_posfija)
print("El resultado de la expresión posfija es:", resultado)

### Ejercicio 09
### Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una pila.

def validar_operadores_anidados(expresion):
    pila = []
    for caracter in expresion:
        if caracter == '(':
            pila.append(caracter)
        elif caracter == ')':
            if not pila or pila[-1] != '(':
                return False
            pila.pop()
    return len(pila) == 0

# Ejemplo de uso
expresion1 = "(a + b) * (c - d)"  # Correctamente anidados
expresion2 = "(a + b) * (c - d))" # Incorrectamente anidados
expresion3 = "((a + b) * (c - d)" # Incorrectamente anidados

print("Expresión 1:", validar_operadores_anidados(expresion1))
print("Expresión 2:", validar_operadores_anidados(expresion2))
print("Expresión 3:", validar_operadores_anidados(expresion3))


### Ejercicio 10
### Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.

class Pila:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("La pila está vacía.")

    def ver_tope(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("La pila está vacía.")

def ordenar_pila_ascendente(pila):
    pila_temporal = Pila()

    while not pila.is_empty():
        elemento_actual = pila.desapilar()
        while not pila_temporal.is_empty() and pila_temporal.ver_tope() > elemento_actual:
            pila.apilar(pila_temporal.desapilar())
        pila_temporal.apilar(elemento_actual)

    return pila_temporal

# Ejemplo de uso
mi_pila = Pila()
mi_pila.apilar(5)
mi_pila.apilar(2)
mi_pila.apilar(7)
mi_pila.apilar(3)
mi_pila.apilar(9)

pila_ordenada = ordenar_pila_ascendente(mi_pila)

print("Pila original:")
while not mi_pila.is_empty():
    print(mi_pila.desapilar(), end=" ")
print()

print("Pila ordenada:")
while not pila_ordenada.is_empty():
    print(pila_ordenada.desapilar(), end=" ")
print()
### Ejercicio 11
###Eliminar los elementos duplicados de una pila.

class Pila:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("La pila está vacía.")

    def ver_tope(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("La pila está vacía.")

def eliminar_duplicados_pila(pila):
    elementos_vistos = set()
    pila_sin_duplicados = Pila()

    while not pila.is_empty():
        elemento_actual = pila.desapilar()
        if elemento_actual not in elementos_vistos:
            elementos_vistos.add(elemento_actual)
            pila_sin_duplicados.apilar(elemento_actual)

    return pila_sin_duplicados

# Ejemplo de uso
mi_pila = Pila()
mi_pila.apilar(5)
mi_pila.apilar(2)
mi_pila.apilar(7)
mi_pila.apilar(2)
mi_pila.apilar(3)
mi_pila.apilar(5)

pila_sin_duplicados = eliminar_duplicados_pila(mi_pila)

print("Pila original:")
while not mi_pila.is_empty():
    print(mi_pila.desapilar(), end=" ")
print()

print("Pila sin duplicados:")
while not pila_sin_duplicados.is_empty():
    print(pila_sin_duplicados.desapilar(), end=" ")
print()

### Ejercicio 12
### Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar expresiones.

class Pila:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("La pila está vacía.")

    def ver_tope(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("La pila está vacía.")

def evaluar_expresion_postfija(expresion_postfija):
    pila = Pila()

    for caracter in expresion_postfija:
        if caracter.isdigit():
            pila.apilar(int(caracter))
        elif caracter in ['+', '-', '*', '/']:
            operando2 = pila.desapilar()
            operando1 = pila.desapilar()
            resultado = None
            if caracter == '+':
                resultado = operando1 + operando2
            elif caracter == '-':
                resultado = operando1 - operando2
            elif caracter == '*':
                resultado = operando1 * operando2
            elif caracter == '/':
                resultado = operando1 / operando2
            pila.apilar(resultado)
    return pila.desapilar()

def convertir_infix_a_postfix(expresion_infix):
    precedencia = {'+': 1, '-': 1, '*': 2, '/': 2}
    pila = Pila()
    resultado = []
    for caracter in expresion_infix:
        if caracter.isdigit():
            resultado.append(caracter)
        elif caracter == '(':
            pila.apilar(caracter)
        elif caracter == ')':
            while not pila.is_empty() and pila.ver_tope() != '(':
                resultado.append(pila.desapilar())
            pila.desapilar()  # Desapilar el '('
        else:
            while not pila.is_empty() and precedencia.get(caracter, 0) <= precedencia.get(pila.ver_tope(), 0):
                resultado.append(pila.desapilar())
            pila.apilar(caracter)
    while not pila.is_empty():
        resultado.append(pila.desapilar())
    return ''.join(resultado)

def calcular_expresion(expresion):
    expresion_postfija = convertir_infix_a_postfix(expresion)
    resultado = evaluar_expresion_postfija(expresion_postfija)
    return resultado

# Ejemplo de uso
expresion = "3 + 4 * 2 / (1 - 5)"
resultado = calcular_expresion(expresion)
print(f"El resultado de la expresión '{expresion}' es: {resultado}")


### Ejercicio 13
### Utilizar una pila para comprobar si una palabra o frase es un palíndromo.



### Ejercicio 14
### Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los deshaceres.


### Ejercicio 15