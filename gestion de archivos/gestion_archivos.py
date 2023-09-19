p = open('gestion_archivos_prueba.txt') #abres archivo, despues de la coma se declaran los permisoso que le daremos a la lectura o modificacion del archivo, write = 'w', append = 'a', create = 'x', read = 'read'
#print(p.read()) #lees el archivo completo
#print(p.readline()) #Sirve para leer linea por linea el archivo, usar un readline x cada linea del archivo

#leer cada linea sin escribir cada readline x cada linea
for x in p:
    print(x)

p.close() #cierra la ejecucion de la variable 

