"""ejercicio N1
La función max() del ejercicio 1 (primera parte) y la función max_de_tres() del ejercicio 2 (primera parte), 
solo van a funcionar para 2 o 3 números. Supongamos que tenemos mas de 3 números o no sabemos cuantos números son. 
Escribir una función max_in_list() que tome una lista de números y devuelva el mas grande.
"""

def max_in_list(lista:list):
    """
    return max(lista)
    """
    max_number = 0
    for item in lista:
        if item > max_number:
            max_number = item        
    return max_number

"""ejercicios N2
Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
"""
def palabra_mas_larga(lista:list):
    palabra_larga = ''
    for item in lista:
        if len(item) > len(palabra_larga):
            palabra_larga = item
    return palabra_larga
        
"""ejercicio N3
Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva las palabras que tengan mas de n caracteres.
"""
def filtrar_palabras(lista:list, n:int):
    palabras_filtradas = []
    for i in lista:
        if len(i) == n:
            palabras_filtradas.append(i)
    return palabras_filtradas


"""ejercicio N4
Escribir un programa que le diga al usuario que ingrese una cadena. El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
"""
def letra_mayuscula():
    cadena = str(input("ingrese una cadena: "))
    cantidad_mayusculas = 0
    for i in range(len(cadena)):
        if cadena[i] != cadena[i].lower():
            cantidad_mayusculas +=1            
    return cantidad_mayusculas

"""ejercicio N5
Construir un pequeño programa que convierta números binarios en enteros.
"""
def conversor_binario_entero():
    binario = input("Ingrese un Numero Binario")
    print(int(binario,2))

"""ejercicio N6
Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso. 
- Se imprime en pantalla.

"""
def calcular_year():
    year_currenty= int(input("Ingresa el año en curso: "))
    for i in range(3):
        nombre= (input('Ingrese el nombre: '))
        year = int(input('Ingrese el año de nacimiento: '))
        print(f'{nombre} va cumplir {year_currenty - year} en el año {year_currenty}')


"""ejercicio N7
Definir una tupla con 10 edades de personas.
Imprimir la cantidad de personas con edades superiores a 20.
Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
"""

def mayor20(tup:tuple):
    cont = 0
    for i in tup:
        if i >20:
            cont += 1
    return f"La cantidad de persona mayores son {cont}"

"""ejercicio N8
Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
También se puede hacer elegir al usuario la letra a buscar.  (Un poco mas emocionante)
"""
def inicial():
    lista_nombres = ['Jose','Raul',"Mauricio",'Camilo',"Marcos","Christian",'Daniel','Nicolas','Matias','Felipe']
    comienzo = input("Con que letra empieza el nombre?: ")
    cont = 0
    for i in lista_nombres:
        if i[0] == comienzo.lower() or i[0] == comienzo.upper() :
            cont += 1
    return cont

"""ejercicio N9
Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, cuantas letras "e" tiene y así hasta completar todas las vocales.
Se puede hacer que el usuario sea quien elija la palabra.

"""
def contar_vocales(palabra:str):
    vowels = input('Que vocal desea contar: ')
    contador = 0
    for i in range(len(palabra)):
        if palabra[i] == vowels:
            contador += 1
    return f'{palabra} contiene {contador} veces la vocal {vowels}'

print(contar_vocales('origami'))


"""ejercicio N10
Escriba una función es_bisiesto() que determine si un año determinado es un año
bisiesto.Un año bisiesto es divisible por 4, pero no por 100. También es divisible por 400
"""
def es_bisiesto():
    print( "Comprueba años bisiestos")
    a = input("Escriba un años y le dire si es bisiesto: ")
    if a % 4 == 0 and (not(a % 100 == 0)):
        print ("El año", a, "es un año bisiesto porque es multiplo de 4")
    elif a % 400 == 0:
        print ("El año", a, "es un año bisiesto porque es multiplo de 400")
    else:
        print ("El año", a, "no es bisiesto")