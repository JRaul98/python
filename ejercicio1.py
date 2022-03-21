""" ejercicio N1
Definir una función max() que tome como argumento dos números y 
devuelva el mayor de ellos. (Es cierto que python tiene una función 
max() incorporada, pero hacerla nosotros mismos es un muy buen 
ejercicio.
"""
def function_max(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

"""ejercicio N2
Definir una función max_de_tres(), que tome tres números como 
argumentos y devuelva el mayor de ellos.
"""
def max_de_tres(n1,n2,n3):
    if n1 > n2 and n1 >n3:
        return n1
    if n2 > n1 and n2> n3:
        return n2
    if n3 > n1 and n3> n2:
        return n3


"""ejercicio N3
Definir una función que calcule la longitud de una lista o 
una cadena dada. (Es cierto que python tiene la función len() 
incorporada, pero escribirla por nosotros mismos resulta un muy 
buen ejercicio.
"""

def función_len(cadena): 
    cont = 0
    for i in cadena:
        cont += 1
    return cont

"""ejercicio N4
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

"""

def is_vocal(caracter):
    lista_vocales= ['a','e','i','o','u']
    if caracter in lista_vocales:
        return True
    return False

"""ejercicio N5
Escribir una función sum() y una función multip() que sumen y multipliquen respectivamente todos los números de una lista. 
Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.
"""

def funcion_sum(lista_numero):
    suma_total = 0
    for i in lista_numero:
        suma_total = suma_total + (i)
    return suma_total

def multip(lista_numero):
    suma_total = 1
    for i in lista_numero:
        suma_total *= i
    return suma_total

"""ejercicio N6
Definir una función inversa() que calcule la inversión de una cadena. 
Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"
"""
def inversa(cadena):
    longitud_cadena = len(cadena)
    palabra_inversa = str()
    for i in range(-(longitud_cadena),0):
        i = abs(i)
        palabra_inversa += cadena[i-1]     
    return palabra_inversa


"""ejercicio N7
Definir una función es_palindromo() que reconoce palíndromos 
(es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") 
tendría que devolver True.
"""
def es_palindromo(cadena):
    palabra_invertida = inversa(cadena)
    if palabra_invertida == cadena:
        return True
    else:
        return False

"""ejercicio N8
 Definir una función superposicion() que tome dos listas y devuelva True si tienen al menos 1 miembro en 
 común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado
"""
def superposicion(lista1,lista2):
    for elem1 in lista1:
        for elem2 in lista2:
            if elem1 == elem2:
                return True
    return False

"""ejercicio N9
Definir una función generar_n_caracteres() que tome un entero n y devuelva el caracter multiplicado por n.
Por ejemplo: generar_n_caracteres(5, "x") debería devolver "xxxxx".
"""
def generar_n_caracteres(n,caracter):
    print(n*caracter)

"""ejercicio N10
Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.
 Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""
def procedimiento(lista):
    for i in lista:
        print('*'* i+'\n')

procedimiento([6,18,9])