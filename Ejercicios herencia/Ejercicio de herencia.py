class Animal:
    def __init__(self,nombre, onomatopeya):
        self.nombre = nombre
        self.onomatopeya = onomatopeya

    def saludo(self):
        print('Hola, soy', self.tipo, ' y mi sonido es el',self.onomatopeya) 


class Gato(Animal):
    #def __init__(self,nombre, onomatopeya):
        #self.nombre = nombre
        #self.onomatopeya = onomatopeya

    #def saludo(self):
        #print('Hola, soy un gato y mi sonido es el',self.onomatopeya)    
    tipo = 'gato'
    #Extendiendo el comportamiento de __init__ de la clase padre
    def __init__(self, nombre, onomatopeya):
        Animal.__init__(self, nombre, onomatopeya)
        print('Hola, soy un gato extendido')

class Perro(Animal):
    #def __init__(self,nombre, onomatopeya):
        #self.nombre = nombre
        #self.onomatopeya = onomatopeya

    #def saludo(self):
        #print('Hola, soy un perro y mi sonido es el',self.onomatopeya)  
    tipo = 'perro'
    #Otra forma de extender el comportamiento de init del padre
    def __init__(self, nombre, onomatopeya):
        super().__init__( nombre, onomatopeya)
        print('instanciando un perro') 

class Canario(Animal):
    tipo = 'canario' 

gato = Gato('Michi', 'maullido')
gato.saludo()

perro = Perro('Nala', 'ladrido')
perro.saludo()

canario = Canario('Piolin', 'silvido')
canario.saludo()