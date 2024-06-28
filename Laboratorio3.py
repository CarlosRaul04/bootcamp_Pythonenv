
class Persona: 
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.__edad = edad
        self.ciudad = ciudad

    def getEdad(self):
        return self.__edad;

    def setEdad(self, edadNueva):
        if (edadNueva != 0):
            self.__edad = edadNueva;
        else :
            print("La edad tiene que ser mayor que 0")


    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.__edad} años";

    def cumplir_años(self):
        self.__edad +=1

    def cambiar_ciudad(self, nuevaCiudad):
        self.ciudad = nuevaCiudad;

    


#Creo 3 objetos
Jhon = Persona("Jhon", 20, "Lima")
Sofia = Persona("Sofia", 18, "Huancayo")
Juan = Persona("Juan", 43, "Pueblo Libre")

Jhon.cumplir_años()
Jhon.cambiar_ciudad("Miraflores")
print(Jhon.presentarse())
print(Jhon.ciudad)

Sofia.cumplir_años()
Sofia.cambiar_ciudad("Chosica")
print(Sofia.presentarse())
print(Sofia.ciudad)

Juan.cumplir_años()
Juan.cambiar_ciudad("San Juan de Lurigancho")
print(Juan.presentarse())
print(Juan.ciudad)


#ESTUDIANTE

class Estudiante(Persona):
    def __init__(self, nombre, edad, ciudad, grado):
        super().__init__(nombre, edad, ciudad)
        self.grado = grado

    

    def estudiar(self):
        return f"{self.nombre} está estudiando"
    

Carlos = Estudiante("Carlos", 20, "Lima", "5 de Secundaria")
print(Carlos.presentarse() + ", vivo en " + Carlos.ciudad)
Carlos.cumplir_años()
Carlos.cambiar_ciudad("San Borja")
print(Carlos.presentarse() + ", vivo en " + Carlos.ciudad)
print(Carlos.estudiar())

Carlos.setEdad(0)


#Animal 

class Animal():
    def __init__(self, nombre:str):
        self.nombre = nombre

    def hacer_sonido(self):
        pass



class Perro(Animal):
    def hacer_sonido(self):
        return "Wof Wof"
    
class Gato(Animal):
    def hacer_sonido(self):
        return "Miaau"
    


def hacer_que_suenen(lista_animales: list):
    for animal in lista_animales:
        print(animal.hacer_sonido())

Firulais = Perro("Firulais")
Tito = Gato("Tito")

animales = [Firulais, Tito]

hacer_que_suenen(animales);


#ENCAPSULAMIENTO

Noemi = Persona("Noemí", 25, "La Molina")
print(Noemi.presentarse())
Noemi.setEdad(22)
print(Noemi.getEdad())
print(Noemi.presentarse())


       
    