### Laboratorio 1-2

#ejercicio 1
# ingrese dos números
num1 = 10
num2 = 8

sum = num1 + num2
suma = num1-num2
multiplicación = num1*num2
división = num1/num2
# Realizar las operaciones e imprimir los resultados
print(f"Suma: {num1 + num2}")
print(f"Resta: {num1 - num2}")
print(f"Multiplicación: {num1 * num2}")
print(f"división es:{num1/num2}")

### Ejercicio 02

n = float(input("ingrese numero: "))
if n % 2==0:
  print(f"el {n} es par")
else:
  print(f"el {n} es impar")

### Ejercicio 03

base = 10
altura = 8

area = (base * altura) / 2

print(f"El área del triángulo con base {base} y altura {altura} es: {area}")

### Ejercicio 04

def calcular_factorial(n):
    if n < 0:
        return "No se puede calcular el factorial de un número negativo."
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

### Ejercicio 05

#Verifica si un número ingresado por el usuario es primo o no

def es_primo(n):
    if n <= 1:
      return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
          return False
    return True

# ingrese un número
num_ingresado= int(input("Ingresa un número para verificar si es primo: "))

# Verificar si el número es primo o no
if es_primo(num_ingresado):
    print(f"El número {num_ingresado} es primo.")
else:

    print(f"El número {num_ingresado} no es primo.")

### Ejercicio 06

#introducir un texto e invertirla
def invertir_cadena(cadena):
    return cadena[::-1]

# Solicitar al usuario que ingrese una cadena de texto
cadena_ingresada = input("Ingrese una cadena de texto para invertirla: ")

# Invertir la cadena y mostrar el resultado
cadena_invertida = invertir_cadena(cadena_ingresada)
print(f"La cadena invertida es: {cadena_invertida}")

### Ejercicio 07

# Suma de Números Pares:
#Calcula la suma de los números pares en un rango especificado por el usuario

def suma_numeros_pares(rango_inicio, rango_fin):
    suma = 0
    for numero in range(rango_inicio, rango_fin + 1):
        if numero % 2 == 0:
            suma += numero
    return suma
#  ingrese el rango
inicio = int(input("Ingrese el inicio del rango: "))
fin = int(input("Ingrese el fin del rango: "))
# Calcular la suma de los números pares y mostrar el resultado
resultado_suma_pares = suma_numeros_pares(inicio, fin)
print(f"La suma de los números pares en el rango de {inicio} a {fin} es: {resultado_suma_pares}")

### Ejercicio 08

######## Lista de Cuadrados: Crea una lista de los cuadrados de los primeros 10 números naturales.
# Crear una lista de los cuadrados de los primeros 10 números naturales
cuadrados = [i ** 2 for i in range(1, 11)]

# Mostrar la lista resultante
print("Lista de cuadrados de los primeros 10 números naturales:")
print(cuadrados)


### Ejercicio 09

#Contador de Vocales: Cuenta el número de vocales en una cadena de texto.
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for caracter in cadena:
        if caracter in vocales:
            contador += 1
    return contador

# Solicitar al usuario que ingrese una cadena de texto
cadena_ingresada = input("Ingrese una cadena de texto para contar las vocales: ")

# Contar las vocales y mostrar el resultado
resultado_contador_vocales = contar_vocales(cadena_ingresada)
print(f"El número de vocales en la cadena es: {resultado_contador_vocales}")

### Ejercicio 10

#Genera los primeros 10 números de la serie Fibonacci.
def generar_serie_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

# Generar los primeros 10 números de la serie Fibonacci
n = 10
serie_fibonacci = generar_serie_fibonacci(n)

# Mostrar la serie resultante
print(f"Los primeros {n} números de la serie Fibonacci son:")
print(serie_fibonacci)

### Ejercicio 11

#Ordenamiento de Lista: Ordena una lista de números ingresados por el usuario de menor a mayor.
# Solicitar al usuario ingresar una lista de números separados por espacios
entrada_usuario = input("Ingrese una lista de números separados por espacios: ")

# Convertir la entrada del usuario en una lista de números
numeros = [float(numero) for numero in entrada_usuario.split()]

# Ordenar la lista de menor a mayor
numeros_ordenados = sorted(numeros)

# Mostrar la lista ordenada
print("Lista ordenada de menor a mayor:")
print(numeros_ordenados)

### Ejercicio 12

#Palíndromo: Verifica si una palabra ingresada por el usuario es un palíndromo
def es_palindromo(palabra):
    palabra = palabra.lower()  # Convertir la palabra a minúsculas para hacer la comparación insensible a mayúsculas
    palabra = ''.join(c for c in palabra if c.isalnum())  # Quitar caracteres no alfanuméricos
    return palabra == palabra[::-1]

# Solicitar al usuario que ingrese una palabra
palabra_ingresada = input("Ingrese una palabra para verificar si es un palíndromo: ")

# Verificar si la palabra es un palíndromo y mostrar el resultado
if es_palindromo(palabra_ingresada):
    print(f"{palabra_ingresada} es un palíndromo.")
else:
    print(f"{palabra_ingresada} no es un palíndromo.")

### Ejercicio 13
    
# Generador de Tablas de Multiplicar: Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario
# Solicitar al usuario que ingrese un número
numero_ingresado = int(input("Ingrese un número para generar su tabla de multiplicar: "))

# Generar y mostrar la tabla de multiplicar
print(f"Tabla de multiplicar del {numero_ingresado}:")
for i in range(1, 11):
    resultado = numero_ingresado * i
    print(f"{numero_ingresado} x {i} = {resultado}")

### Ejercicios 14
    
# Area de un circulo
import math

# Solicitar al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))
# Calcular el área del círculo
area = math.pi * (radio ** 2)
# Mostrar el resultado
print(f"El área del círculo con radio {radio} es: {area}")

### Ejercicio 15
#suma de digitos
# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingrese un número entero: "))

# Calcular la suma de los dígitos
suma_digitos = sum(int(digito) for digito in str(abs(numero)))

# Mostrar el resultado
print(f"La suma de los dígitos de {numero} es: {suma_digitos}")
