class Coche: 
    def __init__(self, marca, modelo, anio, color, placa, num_puertas, combustible,capacidad, transmision, velocidad_actual, en_movimiento):   
        
        
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.placa = placa
        self.num_puertas = num_puertas
        self.combustible = combustible
        self.capacidad = capacidad
        self.transmision = transmision
        self.velocidad_actual = velocidad_actual
        self.en_movimiento = en_movimiento



        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Color: {self.color}")
        print(f"Placa: {self.placa}")
        print(f"Número de puertas: {self.num_puertas}")
        print(f"Combustible: {self.combustible}")
        print(f"Capacidad del tanque: {self.capacidad} litros")





    def arrancar(self):
        self.en_movimiento = True
        print(f"{self.marca} {self.modelo} ha arrancado.")

    def detener(self):
        self.en_movimiento = False
        self.velocidad_actual = 0
        print(f"{self.marca} {self.modelo} se ha detenido.")

    def frenar(self):
        print(f"{self.marca} {self.modelo} está frenando. Velocidad actual: {self.velocidad_actual} km/h.")
    
    def abrir_puertas(self):
        print(f"{self.marca} {self.modelo} está abriendo las puertas.")

    def cambiar_marcha(self, marcha):
        print(f"{self.marca} {self.modelo} está cambiando a la marcha {marcha}.")




coche1 = Coche("Ford", "Ranger", 1994, "Blanca", "HER-5814", 2, "Gasolina", "60 Litros", "Estandar", 0, False)


coche1.arrancar()
coche1.frenar()
coche1.detener()
coche1.abrir_puertas()
coche1.cambiar_marcha(2)