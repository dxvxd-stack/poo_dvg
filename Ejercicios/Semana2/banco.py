class Banco:
    def __init__(self, no_clientes, no_elementos_seguridad, no_edificios, sistema_informatico, nombre_Banco, no_cajeros, fiable, capital, horario_de_atencion, color):
        self.no_clientes = no_clientes
        self.no_elementos_seguridad = no_elementos_seguridad
        self.no_edificios = no_edificios
        self.sistema_informatico = sistema_informatico
        self.nombre_Banco = nombre_Banco
        self.no_cajeros = no_cajeros
        self.fiable = fiable
        self.capital = capital
        self.horario_de_atencion = horario_de_atencion
        self.color = color


   
        print(f"Numero de clientes {self.no_clientes}")
        print(f"Numero de seguridad {self.no_elementos_seguridad}")
        print(f"Numero de edificios {self.no_edificios}")
        print(f"Numero de sistema {self.sistema_informatico}")
        print(f"Nombre de Banco {self.nombre_Banco}")
        print(f"No. cajeros {self.no_cajeros}")
        print(f"Es fiable {self.fiable}")
        print(f"Capital total {self.capital}")
        print(f"Horario de atencion {self.horario_de_atencion}")
        print(f"Color {self.color}")


        print()

    def retirar(self):
        print(f"Se a retirado en un cajero de {self.nombre_Banco}")

    def consultar(self):
        print(f"Se a consultado el saldo en la app del banco {self.nombre_Banco}")

    def prestar(self):
        print(f"El banco {self.nombre_Banco} a prestado")

    def transferir(self):
        print(f"Se a transferido")

    def ahorrar(self):
        print(f"En la aplicacion del banco {self.nombre_Banco} se a ahorrado ")
        

acme = Banco(10000, None, None, "Acme0.1", "Acme", 10000, True, 1000000, "4:00am - 14:00pm", "Verde Pasto")

acme.retirar()
acme.consultar()
acme.prestar()
acme.transferir()
acme.ahorrar()
