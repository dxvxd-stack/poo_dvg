class Silla:
    def __init__(self, material, tipo, altura, resistencia_peso, comodidad, num_patas, color, marca, esta_entera):
        self.material = material
        self.tipo = tipo
        self.altura = altura
        self.resistencia_peso = resistencia_peso
        self.comodidad = comodidad
        self.num_patas = num_patas
        self.color = color
        self.marca = marca
        self.esta_entera = esta_entera

        print(f"De que material es? {self.material}")
        print(f"Que tipo de silla es? {self.tipo}")
        print(f"A que altura esta? {self.altura}")
        print(f"Cuanto peso aguanta? {self.resistencia_peso}")
        print(f"Es comoda? {self.comodidad}")
        print(f"Cuantas patas tiene? {self.num_patas}")
        print(f"De que color es? {self.color}")
        print(f"De que marca es? {self.marca}")
        print(f"Esta en buenas condiciones? {self.esta_entera}")


    def soportar_peso(self):
        print(f"La silla de {self.material} si aguanta a dos personas")

    def ajustar_altura(self):
        print(f"Se subio la altura a {self.altura}")

    def reclinar(self):
        print(f"La silla {self.tipo} sepuede reclinar")

    def mover(self):
        print(f"La silla de color {self.color} se patino")

    def romper(self):
        self.esta_entera = False
        print("Una pata se quebró. La silla ya no está en buenas condiciones")


silla = Silla("Plastico", "Ergonómica", "90 cm", "120 kg", True, 4, "Negro mate", "Muebleria modelo", True)

silla.soportar_peso()
silla.ajustar_altura()
silla.reclinar()
silla.mover()
silla.romper()