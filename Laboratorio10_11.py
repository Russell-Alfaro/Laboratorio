###EJERCICIO 1
def Comprobar_edad(edad):
    assert edad >=0,"La edad no puede ser negativa"
    assert (edad,int), "La edad debe ser entero"
a = int(input("Ingresar edad: "))
try:
    Comprobar_edad(a)
    print("La edad es correcta")
except AssertionError as error:
    print("Error: ", error)


###EJERCICIO 3

def Validad_Rango(calificacion):
    nota = calificacion
    assert 0<= int(nota) <= 20, "La calificacion solo puede estar entre 0 y 20"

b = float(input("Introducir la calificacion: "))
try:
    Validad_Rango(b)
    print("La nota esta en el rango")
except AssertionError as error:
    print("Error: ", error)





###EJERCICIO 5

def Igualdad_objetos(objeto1,objeto2):
    assert objeto1 == objeto2, "Los objetos son distintos, deben de ser iguales"
c = input("Ingrese el primer dato: " )
d = input("Ingrese el segundo dato: ")

try:
    Igualdad_objetos(c,d)
    print("Los objetos son iguales")
except AssertionError as error:
    print("Error", error)

###EJERCICIO 7

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
    
###EJERCICIO 11





