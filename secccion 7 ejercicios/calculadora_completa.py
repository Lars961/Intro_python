#Se realiza una calculadora
print('Calculadora')

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

simbolo = input('Ingrese operacion: +, -, *, /\n')

if simbolo == '+':
    resultado = primero + segundo
    print('Suma: \n', resultado)
elif simbolo == '-':
    resultado = primero - segundo
    print('Resta: \n' , resultado)
elif simbolo == '*':
    resultado = primero * segundo
    print('Multiplicacion: \n' , resultado)
elif simbolo == '/':
    resultado = primero / segundo
    print('Division: \n' , resultado)
else:
    print('Tipo de dato invalido, solo se admiten numeros')
    exit()