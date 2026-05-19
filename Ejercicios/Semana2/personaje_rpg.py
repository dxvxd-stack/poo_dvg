class PersonajeRPG:
    def __init__(self, nombre, clase, nivel, vida_max, vida_act, mana, fuerza, agilidad, esta_vivo, arma):
        self.nombre = nombre
        self.clase = clase
        self.nivel = nivel
        self.vida_maxima = vida_max
        self.vida_actual = vida_act
        self.mana = mana
        self.fuerza = fuerza
        self.agilidad = agilidad
        self.esta_vivo = esta_vivo
        self.arma_equipada = arma


        print(f"Nombre del héroe: {self.nombre}")
        print(f"Clase: {self.clase}")
        print(f"Nivel de personaje: {self.nivel}")
        print(f"Vida máxima: {self.vida_maxima}")
        print(f"Vida actual: {self.vida_actual}")
        print(f"Mana disponible: {self.mana}")
        print(f"Puntos de fuerza: {self.fuerza}")
        print(f"Agilidad: {self.agilidad}")
        print(f"¿Sigue vivo?: {self.esta_vivo}")
        print(f"Arma en uso: {self.arma_equipada}")

    def atacar(self):
        print(f"{self.nombre} está atacando")

    def curar(self):
        print(f"{self.nombre} se está curando")

    def subir_nivel(self):
        print(f"{self.nombre} subió de nivel")

    def equipar_arma(self):
        print(f"{self.nombre} cambió su arma")

    def morir(self):
        print(f"{self.nombre} ha muerto")





Wemby = PersonajeRPG("Wemby_Alien", "Guerrero Galáctico", 99, 1000, 850, 500, 95, 110, True, "Balón de Fuego")

Wemby.atacar()
Wemby.curar()
Wemby.subir_nivel()
Wemby.equipar_arma()
Wemby.morir()