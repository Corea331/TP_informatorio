from datosPersonales import personalDomestico

class DatosPago:

    # montos de sueldo según la modalidad
    montos = {
        "mensual_sin_retiro": 395253,
        "mensual_con_retiro": 355447,
        "por_hora": 2897,
    }

    # Los aportes inluyen jubilaión, obra social y ART
    aportes = {
        "1" : 6816.05,      #Hasta 11 horas
        "2" : 10735.77,     #Desde 12 hasta 15 horas
        "3" : 28688.55,     #16 horas o más
    }

    def __init__(self, empleado):
        self.empleado = empleado    # Datos del empleado
        self.descuentos = []        # Lista de tuplas (concepto, monto)
        self.historial = []         # Lista de tuplas (mes, monto)

    def agregar_descuento(self, concepto, monto):
        if monto < 0:
            self.descuentos.append((concepto, monto))
            raise ValueError("El monto del descuento no puede ser negativo.")
        
    def calcular_aporte(self):
        #renombre de horas_trabajadas a horasTrabajadas porque no coincidia con la clase "personalDomestico"
        h = self.empleado.horasTrabajadas
        if h is None or self.empleado.modalidad == "por_hora":
            return 0
        if h <= 12:
            return self.aportes["1"]
        elif 12 < h <= 15:
            return self.aportes["2"]
        else:
            return self.aportes["3"]
        
    def agregar_historial(self, mes, monto):
        if mes and monto >= 0:
            self.historial.append((mes, monto))
        else:
            raise ValueError("El mes no puede ser vacío y el monto debe ser positivo.")