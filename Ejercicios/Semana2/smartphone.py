class Smartphone:
    def __init__(self, marca, modelo, color, almacenamiento, ram, sistema_operativo, condicion_bateria, no_botones, resolucion_pantalla, num_camaras):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.almacenamiento = almacenamiento
        self.ram = ram
        self.sistema_operativo = sistema_operativo
        self.condicion_bateria = condicion_bateria
        self.no_botones = no_botones
        self.resolucion_pantalla = resolucion_pantalla
        self.num_camaras = num_camaras


        print(f"Marca del smartphone: {self.marca}")
        print(f"Modelo del dispositivo: {self.modelo}")
        print(f"Color del equipo: {self.color}")
        print(f"Capacidad de almacenamiento: {self.almacenamiento} GB")
        print(f"Memoria RAM: {self.ram} GB")
        print(f"Sistema Operativo: {self.sistema_operativo}")
        print(f"Condicion de batería: {self.condicion_bateria}%")
        print(f"¿Cuantos botones tiene?: {self.no_botones}")
        print(f"Resolución de pantalla: {self.resolucion_pantalla}")
        print(f"Número de cámaras: {self.num_camaras}")

iphone_13 = Smartphone("Apple", "iPhone 13", "Azul marino", 128, 4, "iOS", 84, 4, "2556 x 1179", 3)
