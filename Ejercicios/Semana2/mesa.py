class Mesa:
    def __init__(self, material, forma, dimensiones, tipo_patas, color, habitacion, esta_firme, mantel,capacidad_personas,costo):
        self.material = material
        self.forma = forma
        self.dimensiones = dimensiones
        self.tipo_patas = tipo_patas
        self.color = color
        self.habitacion = habitacion
        self.esta_firme = esta_firme
        self.mantel = mantel
        self.capacidad_personas = capacidad_personas
        self.costo = costo

        print(f"De que material es la mesa? {self.material}")
        print(f"Que forma tiene la mesa? {self.forma}")
        print(f"Que dimenciones tiene? {self.dimensiones}")
        print(f"Que tipo de patas tiene? {self.tipo_patas}")
        print(f"De que color es? {self.color}")
        print(f"En que abitacion esta? {self.habitacion}")
        print(f"Esta firme? {self.esta_firme}")
        print(f"Tiene mantel? {self.mantel}")
        print(f"La mesa tiene capacidad para {self.capacidad_personas} personas")
        print(f"La mesa costo mas o menos {self.costo}")

        print()

    def sostener_objetos(self):
        print(f"La mesa de {self.material} está sosteniendo platos y vasos")

    def limpiar(self):
        print(f"La mesa esta limpia {self.forma} ")

    def cambiar_mantel(self):
        print(f"Cambiaron el mantel por un {self.mantel}")

    def mover_de_lugar(self):
        print(f"Movieron la mesa a el {self.habitacion}")

    def tambalear(self):
        print(f"La mesa está firme? {self.esta_firme}")

mesa = Mesa("Madera", "Rectangular", "1.80m x 0.90m","De madera en cruz", "cafe", "Comedor", True, "Mantel de tela",6,7000)


mesa.sostener_objetos()
mesa.limpiar()
mesa.cambiar_mantel()
mesa.mover_de_lugar()
mesa.tambalear()