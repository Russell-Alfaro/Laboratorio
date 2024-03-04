#### LABORATORIO 08-09


###Ejercicio 01
###Validar la edad de un usuario.

def Comprobar_edad(edad):
    assert edad >=0,"La edad no puede ser negativa"
    assert (edad,int), "La edad debe ser entero"
a = int(input("Ingresar edad: "))
try:
    Comprobar_edad(a)
    print("La edad es correcta")
except AssertionError as error:
    print("Error: ", error)

###Ejercicio 02

def verificar_tipo_dato(variable):
    assert isinstance(variable, (int, float, str, list, tuple, dict)), "El tipo de dato no es válido"

    # Si la aserción pasa, significa que el tipo de dato es válido
    print("El tipo de dato es válido")
#
dato_ingresado= input("ingrese una variable:  ")
# Ejemplos de uso
try:
    variable = eval(dato_ingresado)
    tipo_de_dato = type(variable).__name__  # Obtener el nombre del tipo de dato como una cadena
    print("El tipo de dato es:", tipo_de_dato)
except Exception as e:
    print("Error:", e)

###EJERCICIO 3
###Validar el rango de una calificacióN
def Validad_Rango(calificacion):
    nota = calificacion
    assert 0<= int(nota) <= 20, "La calificacion solo puede estar entre 0 y 20"

b = float(input("Introducir la calificacion: "))
try:
    Validad_Rango(b)
    print("La nota esta en el rango")
except AssertionError as error:
    print("Error: ", error)


###Ejercicio 04

def asegurar_lista_no_vacia(lista):
    assert len(lista) > 0, "La lista no puede estar vacía"

# Ejemplo de uso
mi_lista = input("ingrese una lista")

try:
    asegurar_lista_no_vacia(mi_lista)
    print("La lista no está vacía.")
except AssertionError as error:
    print("Error:", error)


###EJERCICIO 5
###Validar la igualdad de dos objetos
def Igualdad_objetos(objeto1,objeto2):
    assert objeto1 == objeto2, "Los objetos son distintos, deben de ser iguales"
c = input("Ingrese el primer dato: " )
d = input("Ingrese el segundo dato: ")

try:
    Igualdad_objetos(c,d)
    print("Los objetos son iguales")
except AssertionError as error:
    print("Error", error)

###Ejercicio 06
###Asegurar que un ciclo while se ejecuta al menos una vez

def while_al_menos_una_vez():
    flag_ejecutado = False

    while True:
        # Coloca el código que quieres ejecutar en el ciclo while aquí

        # Aquí estamos simulando algún tipo de condición o lógica
        continuar = input("¿Deseas continuar? (s/n): ")

        if continuar.lower() == 's':
            flag_ejecutado = True
            # Aquí puedes poner más lógica si es necesario
        else:
            break  # Romper el ciclo si el usuario no quiere continuar

    assert flag_ejecutado, "El ciclo while no se ejecutó al menos una vez"

###EJERCICIO 7
### Asegurar que una función retorna un valor específico.
    
def area_cuadrado(L):
    area= a**2
    return area
    assert area_cuadrado(a)==25,"el area de un cuadradaro de lado 5 no es 25"
e= int(input("Ingrese el lado del cuadrado: "))
try:
    area_cuadrado(e)
    print("La funcion es correcta")
except AssertionError as error:
    print("Error:", error)

###Ejercicio 08

def sumar(a, b):
    return a + b

# Ejemplo de uso
resultado = sumar(5, 7)

# Validar el estado de la variable 'resultado' después de la operación
assert resultado == 12, "El resultado de la suma no es el esperado"

print("El resultado de la suma es:", resultado)

### ejercicio 09

import math

try:
    assert 'sqrt' in dir(math), "El módulo math no se ha importado correctamente"
    print("El módulo math se ha importado correctamente.")
except AssertionError as error:
    print(error)

### PARTE 02

### EJERCICIO 10
#Desarrollar el código de buscar nodo en la lista enlazada simple.
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)

print(lista.buscar(2))  
print(lista.buscar(4))  

### Ejercicio 11
### Crea una función que devuelva la longitud de una lista enlazada simple.


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def suma_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

# Ejemplo de uso
lista = ListaEnlazada()
lista.agregar_al_principio(1)
lista.agregar_al_principio(2)
lista.agregar_al_principio(3)
lista.agregar_al_principio(4)

print("Suma de todos los nodos de la lista enlazada:", lista.suma_nodos())


### Ejercicio 12
### Crea una función que devuelva la longitud de una lista enlazada simple.

#Crea una función que devuelva la longitud de una lista enlazada simple.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def longitud(self):
        contador = 0
        actual = self.cabeza
        while actual is not None:
            contador += 1
            actual = actual.siguiente
        return contador

# Ejemplo de uso
lista = ListaEnlazadaSimple()
lista.agregar_al_final(1)
lista.agregar_al_final(2)
lista.agregar_al_final(3)
lista.agregar_al_final(4)

longitud_lista = lista.longitud()
print("Longitud de la lista:", longitud_lista)


### Ejercicio 13
###Implementa una función que concatene dos listas enlazadas simples.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

def concatenar_listas(lista1, lista2):
    if lista1.cabeza is None:
        return lista2
    if lista2.cabeza is None:
        return lista1

    actual = lista1.cabeza
    while actual.siguiente:
        actual = actual.siguiente
    actual.siguiente = lista2.cabeza
    return lista1

# Ejemplo de uso
lista1 = ListaEnlazada()
lista1.insertar_al_principio(1)
lista1.insertar_al_principio(2)
lista1.insertar_al_principio(3)

lista2 = ListaEnlazada()
lista2.insertar_al_principio(4)
lista2.insertar_al_principio(5)
lista2.insertar_al_principio(6)

print("Lista 1:")
lista1.imprimir_lista()
print("Lista 2:")
lista2.imprimir_lista()

concatenada = concatenar_listas(lista1, lista2)
print("Lista concatenada:")
concatenada.imprimir_lista()


### Ejercicio 14
###Crea una función que elimine los nodos duplicados de una lista enlazada simple

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def eliminar_duplicados(self):
        valores_vistos = set()
        actual = self.cabeza
        previo = None
        while actual:
            if actual.valor in valores_vistos:
                previo.siguiente = actual.siguiente
            else:
                valores_vistos.add(actual.valor)
                previo = actual
            actual = actual.siguiente

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)
lista.insertar_al_principio(2)
lista.insertar_al_principio(4)
lista.insertar_al_principio(1)

print("Lista original:")
lista.imprimir_lista()

lista.eliminar_duplicados()

print("Lista sin nodos duplicados:")
lista.imprimir_lista()



### Ejercicio 15
###Implementa una función que invierta el orden de una lista enlazada simple.

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_al_principio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def imprimir_lista(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    def invertir(self):
        previo = None
        actual = self.cabeza
        while actual:
            siguiente_temp = actual.siguiente
            actual.siguiente = previo
            previo = actual
            actual = siguiente_temp
        self.cabeza = previo

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)

print("Lista original:")
lista.imprimir_lista()

lista.invertir()

print("Lista invertida:")
lista.imprimir_lista()



