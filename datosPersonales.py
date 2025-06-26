# datos del personal doméstico y del empleador

class datosPersonales:
    def __init__(self, nombre, apellido, cuil, dni=None, domicilio=None, telefono=None, email=None):
        self.nombre = nombre
        self.apellido = apellido
        self.cuil = cuil
        self.dni = dni
        self.domicilio = domicilio
        self.telefono = telefono
        self.email = email

    def mostrarDatos(self):
        return {
            "Nombre": self.nombre,
            "Apellido": self.apellido,
            "CUIL": self.cuil,
            "DNI": self.dni,
            "Domicilio": self.domicilio,
            "Teléfono": self.telefono,
            "Email": self.email
        }
    
class personalDomestico(datosPersonales):
    def __init__(self, nombre, apellido, cuil, dni=None, fecha_ingreso=None, domicilio=None, telefono=None, email=None, modalidad="", horasTrabajadas=None, antiguedad=0):
        """
        modalidad: "mensual_con_retiro", "mensual_sin_retiro" o "por_hora"
        antiguedad: en años (int)
        horasTrabajadas: si modalidad es "por_hora" (int), si es None, no se aplica
        """
        super().__init__(nombre, apellido, cuil, dni, domicilio, telefono, email,)
        self.modalidad = modalidad.lower()      
        self.antiguedad = antiguedad            
        self.horasTrabajadas = horasTrabajadas  
        self.fecha_ingreso = fecha_ingreso
        

class empleador(datosPersonales):
    def __init__(self, nombre, apellido, cuil, dni=None, domicilio=None, telefono=None, email=None,):
        super().__init__(nombre, apellido, cuil, dni, domicilio, telefono, email,)