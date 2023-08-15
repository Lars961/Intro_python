#En este ejercicio se pedira al usuario un dato para adivinar si este dato esta incluido dentro de una lista ya establecida.

dato = input('ingrese dato: ')

lista = ['hola', 'mundo', 'primer', 'ejercicio', 'seccion', '7']

if lista.count(dato) > 0:
    print('El dato existe')
else: 
    print('El dato no existe:', dato)