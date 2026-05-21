class Libro:
    def __init__(self,nombre, autor, codigo, num_paginas, editorial, genero, año_publicacion, seccion, esta_disponible, dias_prestamo):
        
        self.nombre = nombre                 
        self.autor = autor                   
        self.codigo = codigo                  
        self.num_paginas = num_paginas      
        self.editorial = editorial           
        self.genero = genero                
        self.año_publicacion = año_publicacion 
        self.seccion = seccion              
        self.esta_disponible = esta_disponible 
        self.dias_prestamo = dias_prestamo   

        print(f"Título: {self.nombre}")
        print(f"Autor: {self.autor}")
        print(f"Código: {self.codigo}")
        print(f"Páginas: {self.num_paginas}")
        print(f"Editorial: {self.editorial}")
        print(f"Género: {self.genero}")
        print(f"Año: {self.año_publicacion}")
        print(f"Ubicación en estante: {self.seccion}")
        print(f"Esta disponible? {self.esta_disponible}")
        print(f"Días de préstamo permitidos: {self.dias_prestamo} días")



        print()


    def abrir(self):
        print(f"El libro {self.nombre} a sido abierto")

    def buscar_pc(self):
        print(f"Buscando palabras en el libro {self.nombre}")

    def prestar(self):
        print(f"El libro {self.nombre} a sido prestado")

    def renovar(self):
        print(f"Se extendio el tiempo de prestamo para el libro {self.nombre} por otros {self.dias_prestamo} dias mas")

    def devolver(self):
        print(f"Se a devuelto el libro {self.nombre}")

habitos = Libro("Hábitos Atómicos","James Clear", "978-6073800419", 328, "Paidós", "Desarrollo Personal",2018, "Pasillo D - Estante 1", True, 5)


habitos.abrir()
habitos.buscar_pc()
habitos.prestar()
habitos.renovar()
habitos.devolver()