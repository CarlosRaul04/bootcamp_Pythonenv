
class Producto:
    #Atributos
    def __init__(self, nombre: str, descripcion:str, precio, cantidad_stock: int, categoria:str ):
        self.__nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.__cantidad_stock = cantidad_stock
        self.categoria = categoria

    def __str__(self):
        pass

    def __str__(self):
        return f"Producto: {self.getNombre()}, {self.descripcion}. Con un precio de {self.precio}; y de categoria {self.categoria}"
    
    #GETTERS Y SETTERS DE CANTIDAD Y NOMBRE

    def setCantidad(self, cantidad):
        self.__cantidad_stock = cantidad;
        return self.__cantidad_stock;

    def getCantidad(self):
        return f"Cantidad disponible: {self.__cantidad_stock}"      

    def setNombre(self, nombre):
        self.__nombre = nombre;
        return self.__nombre;

    def getNombre(self):
        return f"Nombre del Producto: {self.__nombre}"  
    



class Categoria: 
    def __init__(self, nombre:str, descripcion:str):
        self.nombre = nombre
        self.descripcion = descripcion


class Proveedor:
    def __init__(self, nombre:str, direccion:str, telefono: str, email:str):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.email = email 
        

class Venta:
    def __init__(self, producto: Producto, cantidad:int,  fecha: str, total):
        self.producto = producto
        self.cantidad = cantidad
        self.fecha = fecha
        self.total = total

    def __str__(self):
        return f"Datos de Venta: Producto = {self.producto}. Cantidad = {self.cantidad}. Fecha = {self.fecha}. Y el monto total es {self.total}"    


class ProductoDigital(Producto):
    def __init__(self, producto: Producto, url_descarga: str, tamanio_archivo):
        self.producto = producto
        self.url_descarga = url_descarga
        self.tamanio_archivo = tamanio_archivo
    
    def __str__(self):
        return f"{self.producto}. Datos extra: url de descarga = {self.url_descarga} y tamanio de archivo= {self.tamanio_archivo}. {self.producto.getCantidad()}"



Smartphone = Producto("Samsung Galaxy S21","Celular nuevo de alta gama", 2500.00, 350, "Tecnología");
Videojuego = ProductoDigital(Producto("God of war", "Juego de PS5", 240.00, 120, "Acción"), "https://sdaa.com", "100gb");

print("Smartphone: ", Smartphone)
print("Videojuego: ", Videojuego)

Smartphone.setNombre("Samsung Galaxy S24")
print(Smartphone)


venta1 = Venta(Videojuego, 2, "2024-06-23", 240)
venta2 = Venta(Smartphone, 1, "2024-06-25", 2500.00)
print("Detalles de la venta 1: ", venta1)
print("Detalles de la venta 2: ", venta2)
