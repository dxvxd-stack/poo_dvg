class HolaMundo:
    
    def __init__(self):
        print("Constructor")

    def metodoUno(self):
        print("Metodo Uno")

    def metodoDos(self,numero_uno:int,numero_dos:int)->int:
        """
        Este metodo realiza la suma de dos numeros enteros y tregresa 
        el resultado

        Args:
            numero_uno:int - Primer numero para la suma
            numero_dos:int - Segundo numero para la suma 
        
        Returns:
        
            resultado:int - Variable con el resultado de la suma
        
        """



        resultado = numero_uno + numero_dos
        return resultado



nombre_objeto = HolaMundo()