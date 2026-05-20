class Transporte: 
    def __init__(self, marca, modelo, anio, color, capacidad_de_pasajeros, peso, pais_de_origen, kilometraje, 
                 en_movimiento, velocidad_maxima):

                 
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.capacidad_de_pasajeros = capacidad_de_pasajeros
        self.velocidad_maxima = velocidad_maxima
        self.peso = peso
        self.pais_de_origen = pais_de_origen
        self.kilometraje = kilometraje
        self.en_movimiento = en_movimiento


        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.anio}")
        print(f"Color: {self.color}")
        print(f"Capacidad de pasajeros: {self.capacidad_de_pasajeros}")
        print(f"Peso: {self.peso} kg")
        print(f"País de origen: {self.pais_de_origen}")
        print(f"Kilometraje: {self.kilometraje} km")
        print(f"En movimiento: {'Sí' if self.en_movimiento else 'No'}")
        print(f"Velocidad máxima: {self.velocidad_maxima} km/h")

        print()


    def arrancar(self):
        self.en_movimiento = True
        print(f"{self.marca} {self.modelo} ha arrancado.")

    def detener(self):
        self.en_movimiento = False
        print(f"{self.marca} {self.modelo} se ha detenido.")
    
    def acelerar(self, velocidad):
        print(f"{self.marca} {self.modelo} está acelerando a {velocidad} km/h.")
    
    def frenar(self):
        print(f"{self.marca} {self.modelo} está frenando.")

    def abrir_puertas(self):
        print(f"{self.marca} {self.modelo} a habierto sus puertas")

transporte1 = Transporte("Mercedes Benz", "Marcopolo", 2010, "Rojo", 45, 2400, "Mexico(Nuevo leon)", 15000, False,"130 km/h" )

transporte1.arrancar()
transporte1.acelerar(60)
transporte1.frenar()
transporte1.detener()
transporte1.abrir_puertas()