class Transporte:
    def __init__(self, marca, modelo, anio, color, velocidad, pasajeros, peso, origen, km, en_movimiento):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.velocidad = velocidad
        self.pasajeros = pasajeros
        self.peso = peso
        self.origen = origen
        self.km = km
        self.en_movimiento = en_movimiento

    def arrancar(self):
        self.en_movimiento = True
        print(f"El {self.marca} {self.modelo} ha arrancado.")

    def detener(self):
        self.en_movimiento = False
        print(f"El {self.marca} {self.modelo} se ha detenido.")

    def acelerar(self, cantidad):
        print(f"Acelerando a {cantidad} Km/h.")

    def frenar(self, cantidad):
        print(f"Frenando {cantidad} Km/h.")

    def obtener_info(self):
        print(f"""
        --- INFO DEL TRANSPORTE ---
        Marca: {self.marca} | Modelo: {self.modelo} ({self.anio})
        Color: {self.color} | País: {self.origen}
        Pasajeros: {self.pasajeros} | Peso: {self.peso} Kg
        Kilometraje: {self.km} Km | ¿Se mueve?: {self.en_movimiento}
        """)

    def cambiar_color(self, nuevo_color):
        self.color = nuevo_color
        print(f"Color cambiado a: {self.color}")

    def tipo_transporte(self):
        return "Transporte Terrestre"

    def calcular_autonomia(self):
        print("Autonomía no calculada todavía.")



transporte1 = Transporte("Mercedes", "Sprinter", 2020, "Blanco", 120, 20, 3500, "Alemania", 15000, False)

transporte1.arrancar()
transporte1.acelerar(60)
transporte1.frenar(20)
transporte1.cambiar_color("Gris")
transporte1.obtener_info()
transporte1.calcular_autonomia()
transporte1.detener()