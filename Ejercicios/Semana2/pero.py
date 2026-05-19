class PerroHusky:
    def __init__(self, nombre, raza, edad, peso, energia, temperamento, color_ojos, color_pelo, esta_vivo, correa):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.energia = energia
        self.temperamento = temperamento
        self.color_ojos = color_ojos
        self.color_pelo = color_pelo
        self.esta_vivo = esta_vivo
        self.correa = correa

        print(f"Nombre del perro {self.nombre}")
        print(f"De que raza es? {self.raza}")
        print(f"Que edad tiene? {self.edad}")
        print(f"Cuanto pesa? {self.peso}")
        print(f"Tiene mucha energia ? {self.energia}")
        print(f"Es bravo ? {self.temperamento}")
        print(f"De que color son sus ojos {self.color_ojos}")
        print(f"De que color es su pelaje {self.color_pelo}")
        print(f"Sigue vivo? {self.esta_vivo}")
        print(f"Tiene correa? {self.correa}")

    def ladrar(self):
        print(f"{self.nombre} está ladrando")

    def comer(self):
        print(f"{self.nombre} se está comiendo su pollo")

    def romper_correa(self):
        print(f"{self.nombre} rompio su correa")

    def escapar(self):
        print(f"{self.nombre} se escapo a jugar ")

    def dormir(self):
        print(f"{self.nombre} se quedó dormido")


husky = PerroHusky("Dante", "Husky Siberiano", 3, "25 kg", "Alta", "Juguetón", "Azul", "Gris y Blanco", True, "cadena larga")

husky.ladrar()
husky.comer()
husky.romper_correa()
husky.escapar()
husky.dormir()