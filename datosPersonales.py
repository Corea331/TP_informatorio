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
    def __init__(self, nombreCompleto, cuil, modalidad="", horasTrabajadas=0, categoria="", antiguedad=0):
        super().__init__(nombreCompleto, cuil)
        self.categoria = categoria
        self.modalidad = modalidad
        self.antiguedad = antiguedad
        self.horasTrabajadas = horasTrabajadas

class empleador(datosPersonales):
    def __init__(self, nombreCompleto, cuil):
        super().__init__(nombreCompleto, cuil)