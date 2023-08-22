#Se realiza una calculadora que suma
print('Calculadora suma')

primero = input('Ingrese primer numero: ')

try:
    primero = int(primero)
except:
    primero = 'string'

if primero == 'string':
    print('Tipo de dato invalido, solo se admiten numeros')
    exit()

segundo = input('ingrese segundo numero: ')

try:
    segundo = int(segundo)
except:
    segundo = 'string'

if segundo == 'string':
    print('Tipo de dato invalido, solo se admiten numeros')
    exit()


resultado = primero + segundo
print(resultado)