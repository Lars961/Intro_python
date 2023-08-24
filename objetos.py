#Creando clases #Las clases se definne por la primera letra en mayuscula
class Usuario:
    def __init__(self, nombre, apellido): #init es una palabra reservada y se ejecuta siempre que nosotros creamos una instancia de nuestra clase 
        self.nombre=nombre #self hace referencia a una instancia que creamos para poder modificar los valores de dicha instancia 
        self.apellido=apellido
        


usuario = Usuario('Luis', 'Reos')
#usuario2 = Usuario()
print(usuario.nombre, usuario.apellido)