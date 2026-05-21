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

        print()

    def encender(self):
        print(f"{self.modelo} se a encendido")

    def tomar_foto(self):
        print(f"{self.modelo} a tomado una foto")

    def hacer_llamadas(self):
        print(f"{self.modelo} a realizado una llamada")

    def instalar_apps(self):
        print(f"En {self.modelo} se a instalado una app")

    def pagar(self):
        print(f"{self.modelo} a pagado usando apple pay ")


iphone_13 = Smartphone("Apple", "iPhone 13", "Azul marino", 128, 4, "iOS 26", 84, 4, "2556 x 1179", 3)

iphone_13.encender()
iphone_13.tomar_foto()
iphone_13.hacer_llamadas()
iphone_13.instalar_apps()
iphone_13.pagar()