#Creando clases #Las clases se definne por la primera letra en mayuscula
class Usuario:
    def __init__(self, nombre, apellido): #init es una palabra reservada y se ejecuta siempre que nosotros creamos una instancia de nuestra clase 
        self.nombre=nombre #self hace referencia a una instancia que creamos para poder modificar los valores de dicha instancia 
        self.apellido=apellido
    #metodos    
    def saludo(self):
        print('Hola! mi nombre es', self.nombre, self.apellido)

#Creando la clase hijo para herencia
class Admin(Usuario):
    def superSaludo(self):
        print('Hola!, me llamo', self.nombre, self.apellido, 'y soy administrador')

usuario = Usuario('Luis', 'Reos')
#usuario2 = Usuario()
print(usuario.nombre, usuario.apellido)

#Llamando metodos
usuario.saludo()

#cambiar valor de un elemento en el objeto
usuario.nombre = 'Alam'
usuario.saludo()

#Borrar un elemento del objeto
#del usuario.nombre

#Borrar un objeto
#del usuario

#creando instancia de Admin
admin = Admin('Luis Alam', 'Reos ')
admin.saludo()
admin.superSaludo()