#Se realiza una calculadora que suma
print('Calculadora suma')

primero = input('Ingrese primer numero: ')

try:
    primero = int(primero)
except:
    primero = 'string'


segundo = input('ingrese segundo numero: ')

try:
    segundo = int(segundo)
except:
    segundo = 'string'

if primero == 'string' or segundo == 'string':
    print('Tipo de dato invalido, solo se admiten numeros')
else:
    resultado = primero + segundo
    print(resultado)