class Coche:
    def __init__(self, marca, modelo, anio, color, placa, puertas, combustible, tanque_max, gas_actual, transmision):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.placa = placa
        self.puertas = puertas
        self.combustible = combustible
        self.tanque_max = tanque_max
        self.gas_actual = gas_actual
        self.transmision = transmision
        self.velocidad_actual = 0
        self.en_movimiento = False

    def arrancar(self):
        self.en_movimiento = True
        print(f" El V8 Supercargado de la {self.marca} {self.modelo} arrancó.")

    def detener(self):
        self.en_movimiento = False
        self.velocidad_actual = 0
        print(f"La {self.modelo} se apagó.")

    def acelerar(self, cantidad):
        self.velocidad_actual += cantidad
        print(f"Acelerando  Vas a {self.velocidad_actual} Km/h.")

    def frenar(self, cantidad):
        self.velocidad_actual = max(0, self.velocidad_actual - cantidad)
        print(f"Frenando. Velocidad actual: {self.velocidad_actual} Km/h.")

    def repostar(self, litros):
        self.gas_actual = min(self.gas_actual + litros, self.tanque_max)
        print(f"Gasolina actual: {self.gas_actual} L.")

    def abrir_puertas(self):
        print(f"Abriendo las {self.puertas} puertas de la Raptor R.")

    def verificar_combustible(self):
        print(f"Nivel de gasolina: {self.gas_actual} L.")

    def cambiar_marcha(self, marcha):
        print(f"Cambio a marcha número: {marcha}")

    def obtener_info(self):
        print(f"{self.marca} {self.modelo} ({self.anio}) | Placa: {self.placa} | Transmisión: {self.transmision}")



coche1 = Coche("Ford", "F-150 Raptor R", 2024, "Negro Mate", "RAP-T0R", 4, "Gasolina", 136, 40, "Automática 10v")

coche1.arrancar()
coche1.acelerar(100)
coche1.cambiar_marcha(5)
coche1.frenar(40)
coche1.repostar(50)
coche1.abrir_puertas()
coche1.verificar_combustible()
coche1.detener()
coche1.obtener_info()