### Ejercicio 01
###Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números primos.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


def numeros_primos(conjunto):
    primos = set()
    for numero in conjunto:
        if es_primo(numero):
            primos.add(numero)
    return primos

### Ejemplo de uso
conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
primos_en_conjunto = numeros_primos(conjunto_numeros)
print("Números primos en el conjunto:", primos_en_conjunto)

### Ejercicio 02 
#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
#comienzan con una letra determinada.

def palabras_que_comienzan_con_letra(conjunto_palabras, letra):
    palabras_seleccionadas = set()

    for palabra in conjunto_palabras:
        if palabra.startswith(letra):
            palabras_seleccionadas.add(palabra)

    return palabras_seleccionadas
conjunto_palabras = {"matematica", "geometria", "algebra", "economia", "matrices"}
letra_inicial = "m"
resultado = palabras_que_comienzan_con_letra(conjunto_palabras, letra_inicial)

print(f"Palabras que comienzan con '{letra_inicial}': {resultado}")

### Ejercicio 03
###Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
###son divisibles por un número determinado.

def numeros_divisibles(conjunto, divisor):
    divisibles = set()
    for numero in conjunto:
        if numero % divisor == 0:
            divisibles.add(numero)
    return divisibles

# Ejemplo de uso
conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
divisor = 2
numeros_divisibles_por_2 = numeros_divisibles(conjunto_numeros, divisor)
print(f"Números en el conjunto divisibles por {divisor}:", numeros_divisibles_por_2)


#########EJERCICIO 04
#Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
#están en ambos conjuntos
def igualdad_numeros(num_1, num_2):

    return num_1.intersection(num_2)
num_1 = {1,2,3,4,5}
num_2 = {3,4,5,6,7}
resultado_2= igualdad_numeros(num_1,num_2)
print(f"Los numeros en comunes entre los dos conjuntos son  {resultado_2}")

### Ejercicio 05
###Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
###están en el primer conjunto pero no7 en el segundo.

def diferencia_conjuntos(conjunto1, conjunto2):
    diferencia = conjunto1 - conjunto2
    return diferencia

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {3, 4, 5, 6, 7}
resultado = diferencia_conjuntos(conjunto1, conjunto2)
print("Diferencia entre los conjuntos:")
print(resultado)

######### EJERCICIO 06
###Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
###están en el segundo conjunto pero no en el primero.

def desigualdad_numeros(num_3,num_4):
    new = num_4.difference(num_3)
    return new
num_3 ={1,2,3,4,5,6,7,8,9}
num_4 ={2,4,6,8,10,11,12}

resultado_3= desigualdad_numeros(num_3,num_4)
print(f"Los numeros que estan en el segundo grupo pero no en el primero son {resultado_3}")

### Ejercicio 07
###Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son anagramas

#Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
#anagramas
def encontrar_anagramas(conjunto_palabras):
    anagramas = set()

    # Crear un diccionario para almacenar palabras anagramas
    anagramas_dict = {}

    for palabra in conjunto_palabras:
        # Ordenar las letras de la palabra y convertir a tupla
        palabra_ordenada = tuple(sorted(palabra))

        # Agregar la palabra al conjunto de anagramas correspondiente
        anagramas_dict.setdefault(palabra_ordenada, set()).add(palabra)

    # Filtrar las palabras que tienen más de un anagrama
    anagramas = {palabra for conjunto in anagramas_dict.values() if len(conjunto) > 1 for palabra in conjunto}

    return anagramas

# Ejemplo de uso
conjunto_palabras_ejemplo = {"ramon", "alvaro", "iman", "top", "pot", "opt", "car", "arc"}
resultado_anagramas = encontrar_anagramas(conjunto_palabras_ejemplo)

# Mostrar el resultado
print("Conjunto de palabras:", conjunto_palabras_ejemplo)
print("Palabras que son anagramas:", resultado_anagramas)

######## EJERCICIO 08
def palindromos_v(palabra):
    return palabra == palabra[::-1]

def palindromos_conjunto(cadena):
    palindromos= set()
    for palabra in cadena:
        if palindromos_v(palabra):
            palindromos.add(palabra)
    return palindromos

cadena={"carro","comer","rapar","reconocer"}
resultado = palindromos_conjunto(cadena)
print(f"Los palindromos  del conjunto son {resultado}")

### Ejercicio 09
### Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
###tienen una longitud determinada.

def palabras_longitud(conjunto_palabras, longitud):
    palabras_con_longitud = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    return palabras_con_longitud

# Ejemplo de uso
conjunto_palabras = {"casa", "perro", "gato", "playa", "sol", "luna"}
longitud = 4
resultado = palabras_longitud(conjunto_palabras, longitud)
print(f"Palabras en el conjunto de longitud {longitud}:")
print(resultado)

###########EJERCICIO 10
def letra_determinada(cadena_1,letra):
    contenedor = set()
    for i in cadena_1:
        if letra in i:
            contenedor.add(i)
    return contenedor
cadena_1={"amarillo","azul","celeste","rojo","rosado","jade","morado"}
letra ="o"
resultado =letra_determinada(cadena_1,letra)
print(f"{resultado}")

### Ejercicio 11
### Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
### están ordenados de menor a mayor.

def numeros_ordenados(conjunto):
    lista_ordenada = sorted(conjunto)
    return set(lista_ordenada)

# Ejemplo de uso
conjunto_numeros = {3, 1, 5, 2, 4}
numeros_ordenados_set = numeros_ordenados(conjunto_numeros)
print("Conjunto de números ordenados de menor a mayor:")
print(numeros_ordenados_set)

###########EJERCICIO 12
###Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
###están ordenados de menor a mayor.

def revertir(ordenados):
    reversion= list(ordenados)[::-1]
    conjunto_nuevo= set(reversion)
    return conjunto_nuevo
def ordenamiento(numeros):
    ordenado = list(numeros)
    ordenado.sort()
    ordenados = set(ordenado)
    return revertir(ordenados)


numeros = {2,3,43,6,8,78,9}
resultado_4 = ordenamiento(numeros)
print(f"El nuevo conjunto es {resultado_4}")

### Ejercicio 13
###Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
###están duplicados.

def numeros_duplicados(conjunto):
    numeros_duplicados = set()
    numeros_vistos = set()

    for numero in conjunto:
        if numero in numeros_vistos:
            numeros_duplicados.add(numero)
        else:
            numeros_vistos.add(numero)

    return numeros_duplicados

# Ejemplo de uso
conjunto_numeros = {1, 2, 3, 3, 4, 5, 6, 6, 7, 8}
numeros_duplicados_set = numeros_duplicados(conjunto_numeros)
print("Conjunto de números duplicados:")
print(numeros_duplicados_set)

### Ejercicio 14
### Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que no
###están duplicados.

def numeros_no_duplicados(conjunto):
    numeros_no_duplicados = {numero for numero in conjunto if list(conjunto).count(numero) == 1}
    return numeros_no_duplicados

# Ejemplo de uso
conjunto_numeros = {1, 2, 3, 3, 4, 5, 6, 6, 7, 8}
numeros_no_duplicados_set = numeros_no_duplicados(conjunto_numeros)
print("Conjunto de números no duplicados:")
print(numeros_no_duplicados_set)

### Ejercicio 15
###Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
###son primos y están ordenados de menor a mayor.

def es_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    for i in range(3, int(numero ** 0.5) + 1, 2):
        if numero % i == 0:
            return False
    return True
def numeros_primos_ordenados(conjunto):
    primos = {numero for numero in conjunto if es_primo(numero)}
    primos_ordenados = sorted(primos)
    return primos_ordenados

# Ejemplo de uso
conjunto_numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
primos_ordenados = numeros_primos_ordenados(conjunto_numeros)
print("Conjunto de números primos ordenados de menor a mayor:")
print(primos_ordenados)

### Ejercicio 16

def palabras_palindromos_ordenadas(conjunto_palabras):
    palindromos = {palabra for palabra in conjunto_palabras if palabra == palabra[::-1]}
    palindromos_ordenados = sorted(palindromos)
    return palindromos_ordenados

# Ejemplo
conjunto_palabras_ejemplo = {"radar", "civic", "hello", "level", "world", "deified"}
resultado_palindromos_ordenados = palabras_palindromos_ordenadas(conjunto_palabras_ejemplo)

# Mostrar el resultado
print("Conjunto de palabras:", conjunto_palabras_ejemplo)
print("Palíndromos ordenados:", resultado_palindromos_ordenados)

### Ejercicio 17

def palabras_longitud_ordenadas(conjunto_palabras, longitud):
    palabras_longitud = {palabra for palabra in conjunto_palabras if len(palabra) == longitud}
    palabras_longitud_ordenadas = sorted(palabras_longitud)
    return palabras_longitud_ordenadas

# Ejemplo
conjunto_palabras_ejemplo = {"apple", "banana", "kiwi", "orange", "grape", "peach"}
longitud_ejemplo = 5
resultado_palabras_longitud = palabras_longitud_ordenadas(conjunto_palabras_ejemplo, longitud_ejemplo)

# Mostrar el resultado
print("Conjunto de palabras:", conjunto_palabras_ejemplo)
print(f"Palabras de longitud {longitud_ejemplo} ordenadas:", resultado_palabras_longitud)

### Ejercicio 18

def palabras_con_letra_ordenadas(conjunto_palabras, letra):
    palabras_con_la_letra = {palabra for palabra in conjunto_palabras if letra in palabra}
    palabras_con_la_letra_ordenadas = sorted(palabras_con_la_letra, reverse=True)
    return palabras_con_la_letra_ordenadas

# Ejemplo
conjunto_palabras_ejemplo = {"apple", "banana", "kiwi", "orange", "grape", "peach"}
letra_ejemplo = "a"
resultado_palabras_con_letra = palabras_con_letra_ordenadas(conjunto_palabras_ejemplo, letra_ejemplo)

# Mostrar el resultado
print("Conjunto de palabras:", conjunto_palabras_ejemplo)
print(f"Palabras que contienen la letra '{letra_ejemplo}' ordenadas:", resultado_palabras_con_letra)


### Ejercicio 19

def numeros_ordenados_sin_duplicados(conjunto_numeros):
    numeros_ordenados = sorted(set(conjunto_numeros))
    return numeros_ordenados

# Ejemplo
conjunto_numeros_ejemplo = {3,12,2,3,6,5, 1, 5, 2, 2, 4, 5}

resultado_numeros_ordenados = numeros_ordenados_sin_duplicados(conjunto_numeros_ejemplo)

print("Conjunto de números:", conjunto_numeros_ejemplo)
print("Números ordenados sin duplicados:", resultado_numeros_ordenados)

### Ejercicio 20

def palabras_palindromos_longitud_ordenadas(conjunto_palabras, longitud):
    palindromos_longitud = {palabra for palabra in conjunto_palabras if palabra == palabra[::-1] and len(palabra) == longitud}
    palindromos_longitud_ordenados = sorted(palindromos_longitud)
    return palindromos_longitud_ordenados

# Ejemplo
conjunto_palabras_ejemplo = {"radar", "civic", "level", "hello", "deified", "world"}
longitud_ejemplo = 5
resultado_palindromos_longitud = palabras_palindromos_longitud_ordenadas(conjunto_palabras_ejemplo, longitud_ejemplo)

print("Conjunto de palabras:", conjunto_palabras_ejemplo)
print(f"Palíndromos de longitud {longitud_ejemplo} ordenados:", resultado_palindromos_longitud)







