# datos del personal doméstico y del empleador

class datosPersonales:
    def __init__(self, nombreCompleto, cuil):
        self.nombreCompleto = nombreCompleto
        self.cuil = cuil

    def mostrarDatos(self):
        return {
            "Nombre Completo": self.nombreCompleto,
            "CUIL": self.cuil,
        }
    
class personalDomestico(datosPersonales):
    def __init__(self, nombreCompleto, cuil, modalidad="", horasTrabajadas=None, antiguedad=0):
        """
        modalidad: "mensual_con_retiro", "mensual_sin_retiro" o "por_hora"
        antiguedad: en años (int)
        horasTrabajadas: si modalidad es "por_hora" (int), si es None, no se aplica
        """
        super().__init__(nombreCompleto, cuil)
        self.modalidad = modalidad.lower()      
        self.antiguedad = antiguedad            
        self.horasTrabajadas = horasTrabajadas  

class empleador(datosPersonales):
    def __init__(self, nombreCompleto, cuil):
        super().__init__(nombreCompleto, cuil)