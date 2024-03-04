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



### ejercicio 09



### PARTE 02

### EJERCICIO 11
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

### Ejercicio 12
### Crea una función que devuelva la longitud de una lista enlazada simple.


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

    def suma_nodos(self):
        suma = 0
        actual = self.cabeza
        while actual:
            suma += actual.valor
            actual = actual.siguiente
        return suma

# Ejemplo de uso
lista = ListaEnlazada()
lista.insertar_al_principio(1)
lista.insertar_al_principio(2)
lista.insertar_al_principio(3)

print("Suma de todos los nodos de la lista enlazada:", lista.suma_nodos())

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



