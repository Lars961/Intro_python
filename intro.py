#Asi se realizan comentarios en python
if 3>5:
    print('Esto no se va a imprimir')

if 5>3:
    print('5 es mayor a 3')

x = 5
y = 'prueba de variables'

#print(x,y)

email = 'lars@mail.com'

#print (email)

#formas de crear variables
_mi_var = 'Variable 1\n'
MIVAR = 'Variable 2\n'
a, b, c = 'variable a\n','variable b\n','variable c\n'

#print(_mi_var, MIVAR, a, b, c)

valor1 = valor2 = valor3 = 'hola mundo en python xD'

#print(valor1 + '\n' + valor2 + '\n' + valor3 + '\n')

inicio = 'Hola'
final = 'mundo'

#print(inicio + ' ' + final)

#Tipos de datos

palabra = 'hola mundo en string y comilla simple!'
oracion = "hola mundo en string con comiilas dobles!"

entero = 20 #Integer
conDecimales = 20.2 #float
numComplejo = 1j #numero complejo se define agregando una "j"

#print(palabra, oracion, entero, conDecimales, numComplejo, '\n')

#Listas
lista = [1,2,3]
lista2 = lista.copy()
#append agrega mas metodos a nuestra lista
lista.append(4)
#clear limpia el contenido de la lista
lista.clear()
print(lista, lista2)

#contar elementos dentro de una lista
lista3 = [3,3,3,4,4,5,5,6]
#count busca el elemento deseado dentro de la lista y regresa el numero de veces que se repite
print (lista3.count(3))
#len cuenta el numero de elementos dentro de la lista
print(len(lista3))

#ingresar a un elemento especifico de la lista
#print(lista3[6])

#eliminar elementos de una lista, .pop() elimina ultimo elemento, .remove() elimina elemento especifico
lista3.pop()
lista3.remove(4)
print(lista3)

#Ordenar listas, los elementos de la lista deben ser del mismo tipo de dato #Reversa a una lista, .reverse()
lista4 = [2,5,8,3,6,9,1,4,7]
lista4.sort()
lista4.reverse()


print(lista4)


#Tuplas
tupla = ('hola', 'mundo','pero','en','tuplas')
print(tupla)
#transformar tupla a lista, mandamos a llamar la funcion list()
tuplaToList = list(tupla)
tuplaToList.append('convertido a lista')
print(tuplaToList)

#Rangos
rango = range(6)
print(rango)

#Diccionarios
diccionario = {
    "nombre": "Nala",
    "raza": "unica",
    "edad": 4
}
#impresion completa del diccionario
print(diccionario)

#accesso a un elemento en especifico
print(diccionario['nombre'])

#metodo para evitar utilizar corchetes
print(diccionario.get('raza'))

#Modificar un elemento dentro del diccionario
diccionario['nombre'] = 'Tommy'
diccionario['raza'] = 'Schnawzer'
diccionario['edad'] = '11'
print(diccionario)

#podemos contar elementos con len
print(len(diccionario))

#agregar elementos a diccionarios
diccionario['peso'] = '8kg'
print(diccionario)

#Eliminar elemento dentro del diccionario, dos fromas diferentes, mismo resultado
diccionario.pop('peso')
#del diccionario['peso']
print(diccionario)

#Eliminar ultimo valor agregado al diccionario
#diccionario.popitem()
#print(diccionario)

#Copiar diccionario, dos formas diferentes, mismo resultado
#copiaDiccionario = dict(diccionario)
copiaDiccionario = diccionario.copy()
print(diccionario, copiaDiccionario)

#Eliminar todos los elementos de un diccionario
copiaDiccionario.clear()
print(copiaDiccionario)

#Diccionario anidado
misMascotas = {
    "Blanco": {
        "nombre": "Blanco",
        "Edad": 12
    },

    "Tommy": {
        "nombre":"Tommy",
        "Edad": 11
    },

    "Nala": {
        "Nombre": "Nala",
        "Edad": 4
    }
}

print(misMascotas)

#Constructor dict(), para crear diccionarios, otra manera para crearlos, mismo resultado
misPerros = dict(nombre="Blanco", edad=12)
print(misPerros)

#Booleanos
verdadero = True
falso = False

print(verdadero, falso)