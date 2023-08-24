#Funciones
def miFuncion():
    print('mi primera funcion')

#llamado a la funcion
miFuncion()

#Entre los parentesis debemos indicarle a la funcione le elemento a esperar
def imprimeDato(argumentoUno):
    print('Mi primer argumento es: ', argumentoUno)

#esto sirve para indicarle que el valor de argumentoUno es parametro 1, esto sirve para pasar valores mediante el argumento esperado por la funcion
imprimeDato('parametro 1')

#Funcion con dos argumentos
def dosArgumentos(nombre, apellido):
    print('Nombre completo: ', nombre, apellido)

dosArgumentos('Luis', 'Reos')

#Funcion que recibe duplas como parametros
def tupla(*tupla): #'*' es un comando reservado de sistema, indica que la funion recibe mas de un argumento de entrada y los trabaja como duplas pero no pueden ser modificados
    print('tupla: ',tupla)
    #print('dupla: ',dupla[0]) #estos [] sirven para acceder a un elemento en especifico dentro de la dupla
tupla('Luis', 'Alam', 'Reos', 'Sanchez')

#Funcion con el comando **kwargs, sirve para ordenar los argumentos esperados por una funcion en forma de diccionario y podemos acceder a estso elementos si tenemos las palabras clave del diccionario
def nombreCompleto(**kwargs):
    print(kwargs['nombre'],kwargs['apellido'])#Definimos las palabras clave dentro del diccionario

nombreCompleto(nombre='Luis', apellido='Reos')#Forzosamente se deben definir aqui los valores de las palabras clave

#Funcion con un valor definido
def valorDefinido(argumentoDefinido = 'Este es un argumento definido'):
    print(argumentoDefinido) #Imprimira el argumento definido en la linea anterior
valorDefinido('argumento modificado') #Si pasamos un argumento diferente al definido, primero imprimira el argumento diferente pero si ya no hya modificaciones, vuelve a imprimir el valor definido
valorDefinido()

#Funcion con una lista como argumento
# def valorLista(lista):
#     for e in lista:
#         print(e)

# valorLista(['Luis', 'Reos']) #Debemos definir los valores dentro de la lista para pasar el argumento

#Concatenar valores en una lista
def concatenarNombres(lista2):
    i = ''
    for elemento in lista2:
        i = i + elemento + ' '
        return i #Si retornamos un valor no se imprimira
    

valorCapturado = concatenarNombres(['Luis', 'Reos'])
print(valorCapturado)