p = open('gestion_archivos_prueba.txt', 'a') #abres archivo, despues de la coma se declaran los permisoso que le daremos a la lectura o modificacion del archivo, write = 'w', append = 'a', create = 'x', read = 'read'
#print(p.read()) #lees el archivo completo
#print(p.readline()) #Sirve para leer linea por linea el archivo, usar un readline x cada linea del archivo

#agregar nueva linea de texto al archivo
p.write('\nagregando nueva linea de texto')

p.close() #cierras variable

#https://www.freecodecamp.org/espanol/news/python-como-escribir-en-un-archivo-abrir-leer-escribir-y-otras-funciones-de-archivos-explicadas/#:~:text=El%20modo%20%22a%22%20(append,al%20final%20del%20contenido%20existente.&text=Y%20queremos%20agregarle%20una%20l%C3%ADnea,que%20queremos%20agregar%20como%20argumento.
