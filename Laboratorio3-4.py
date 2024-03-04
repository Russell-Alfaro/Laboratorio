################ LABORATORIO DE E.D. 03-04 ########################################


### Ejercicios 01
def imprimir_pares(n):
    if n <= 100:
        if n % 2 == 0:
            print(n)
        imprimir_pares(n + 2)

# Llamamos a la función con el primer número par, que es 2
imprimir_pares(2)

#### Ejercicios 02
def suma_hasta_n(n):
    if n == 1:
        return 1
    else:
        return n + suma_hasta_n(n - 1)

def imprimir_suma_hasta_n(n):
    suma = suma_hasta_n(n)
    return (f"La suma de los números del 1 al {n} es: {suma}")

# Ejemplo de uso
imprimir_suma_hasta_n(10)

### EJERCICIO 03 PIRAMIDEE
def imprimir_piramide(n, i=1):
    if i <= n:
        # Imprime espacios en blanco para alinear los números
        print(" " * (n - i), end="")
        
        # Imprime los números en orden ascendente
        for j in range(1, i + 1):
            print(j, end=" ")
        
        # Imprime los números en orden descendente
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        
        print()  # Salto de línea
        
        # Llama recursivamente a la función con el siguiente nivel de la pirámide
        imprimir_piramide(n, i + 1)

# Ejemplo de uso
imprimir_piramide(6)

### Ejercicio 04
def imprimir_piramide_invertida(n, i=1):
    if n == 0:
        return  # Caso base para evitar la recursión infinita
    
    if i <= n:
        # Imprime espacios en blanco para alinear los números
        print(" " * (n - i), end="")
        
        # Imprime los números en orden descendente
        for j in range(i, 0, -1):
            print(j, end=" ")
        
        print()  # Salto de línea
        
        # Llama recursivamente a la función con el siguiente nivel de la pirámide
        imprimir_piramide_invertida(n, i + 1)

# Ejemplo de uso
imprimir_piramide_invertida(5)

### Ejercicio 05
def imprimir_tabla_multiplicar(n, multiplicador=1):
    if multiplicador <= 12:
        print(f"{n} x {multiplicador} = {n * multiplicador}")
        imprimir_tabla_multiplicar(n, multiplicador + 1)

# Ejemplo de uso
imprimir_tabla_multiplicar(5)
 
###  Ejercicio 06
import numpy as np
# Creacion de la matriz con np.array
matriz = np.array([[2,3,2.5],[44,4,6],[14,23,1]])
print(matriz)

### Ejercicio 07

# Crear una matriz de 2x2 con números complejos
matriz_compleja = np.array([[1 + 2j, 3 - 1j],[4j, 2 - 5j]])
print(matriz_compleja)

### Ejercicio 08


# Crear una matriz de matrices
matriz_de_matrices = np.array([[np.array([1, 2, 3]), np.array([4, 5, 6])],
                               [np.array([7, 8, 9]), np.array([10, 11, 12])]], dtype=object)
print(matriz_de_matrices)

### Ejercicio 09


def elemento_central(matriz):
    # Obtener las dimensiones de la matriz
    filas, columnas = matriz.shape
    
    # Determinar si el número de filas y columnas es par o impar
    fila_central = filas // 2
    columna_central = columnas // 2
    
    # Acceder al elemento central
    elemento = matriz[fila_central, columna_central]
    print(fila_central)    
    return elemento

# Ejemplo de uso
matriz_impar = np.array([[1, 2, 3],
                         [4, 5, 6],
                         [7, 8, 9]])

# Acceder al elemento central de cada matriz
elemento_central_impar = elemento_central(matriz_impar)

print("Elemento central de la matriz impar:", elemento_central_impar)

### Ejercicio 10


def suma_matrices_diferentes_tamanos(matriz1, matriz2):
    # Obtener las dimensiones de ambas matrices
    filas1, columnas1 = matriz1.shape
    filas2, columnas2 = matriz2.shape
    
    # Crear una nueva matriz del mismo tamaño que la primera matriz
    resultado = np.zeros_like(matriz1)
    
    # Sumar las partes superpuestas de ambas matrices
    resultado[:filas2, :columnas2] += matriz2
    
    # Sumar la primera matriz
    resultado += matriz1
    
    return resultado

# Ejemplo de uso
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matriz2 = np.array([[7, 8],
                    [9, 10]])

resultado = suma_matrices_diferentes_tamanos(matriz1, matriz2)
print("Resultado de la suma de matrices:")
print(resultado)

### Ejercicio 11

def multiplicar_matriz_por_numero(matriz, numero):
    return matriz * numero

# Ejemplo de uso
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

numero = 2

resultado = multiplicar_matriz_por_numero(matriz, numero)
print("Resultado de multiplicar la matriz por el número:")
print(resultado)

### Ejercicio 12

def media_matriz(matriz):
    return np.mean(matriz)

# Ejemplo de uso
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

media = media_matriz(matriz)
print("Media de los elementos de la matriz:", media)

#### Parte 2
import random
### Ejercicio 01
### Crea una matriz de números aleatorios de tamaño 100x100.

import numpy as np

# Crear una matriz de números aleatorios de tamaño 100x100
matriz_aleatoria = np.random.rand(100, 100)

print("Matriz de números aleatorios de tamaño 100x100:")
print(matriz_aleatoria)  


### Ejercicio 02
###

import numpy as np

# Crear una matriz de ejemplo
matriz = np.random.rand(5, 5)

# Calcular la media
media = np.mean(matriz)

# Calcular la mediana
mediana = np.median(matriz)

# Calcular la desviación estándar
desviacion_estandar = np.std(matriz)

# Imprimir los resultados
print("Matriz:")
print(matriz)
print("Media:", media)
print("Mediana:", mediana)
print("Desviación estándar:", desviacion_estandar)

### Ejercicio 03
###Escribe una función que encuentre el elemento máximo de una matriz.

def encontrar_maximo(matriz):
    # Utiliza la función np.max() para encontrar el valor máximo en la matriz
    maximo = np.max(matriz)
    return maximo

# Ejemplo de uso
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

maximo = encontrar_maximo(matriz)
print("Elemento máximo de la matriz:", maximo)

### Ejercicio 04
###Escribe una función que encuentre la submatriz de mayor suma de una matriz.


### Ejercicio 05
###Encontrar la maatriz covarianza

import numpy as np

def matriz_covarianza(matriz1, matriz2):
    # Concatenar las dos matrices a lo largo del eje 0 para formar una matriz conjunta
    matriz_conjunta = np.vstack((matriz1, matriz2))
    
    # Calcular la matriz de covarianza
    covarianza = np.cov(matriz_conjunta)
    
    return covarianza

# Ejemplo de uso
matriz1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matriz2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

matriz_cov = matriz_covarianza(matriz1, matriz2)
print("Matriz de covarianza entre las dos matrices:")
print(matriz_cov)


