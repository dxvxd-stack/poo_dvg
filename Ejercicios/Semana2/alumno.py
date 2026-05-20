class Alumno:
    def __init__(self,nombre,apellido,matricula,edad,genero,telefono,correo,direccion,curp,fecha_nac):

        self.nombre = nombre
        self.apellido = apellido
        self.matricula = matricula
        self.edad = edad
        self.genero = genero
        self.telefono = telefono 
        self.correo = correo
        self.direccion = direccion
        self.curp = curp
        self.fecha_nac = fecha_nac

        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"NO matricula: {self.matricula}")
        print(f"Edad: {self.edad}")
        print(f"Genero: {self.genero}")
        print(f"Telefono: {self.telefono}")
        print(f"Correo {self.correo}")
        print(f"Direccion: {self.direccion}")
        print(f"Curp: {self.curp}")
        print(f"Fecha de nacimiento: {self.fecha_nac}")

        print()

    def inscribir(self):
        print(f"{self.nombre} {self.apellido} se inscribio")

    def jugar(self):
        print(f"{self.nombre} {self.apellido} esta jugando basquetball")

    def comer(self):
        print(f"{self.nombre} {self.apellido} esta comiendo")

    def pagar(self):
        print(f"{self.nombre} {self.apellido} esta pagando su desayuno")

    def hablar(self):
        print(f"{self.nombre} {self.apellido} esta hablando")


yo=Alumno("David","Vargas","172511","18 años","Masculino",775164,"172511@gmail.com","Bosques","GDYUAFGD","8/10/1998")

yo.inscribir()
yo.jugar()
yo.comer()
yo.pagar()
yo.hablar()