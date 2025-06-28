from tkinter import messagebox


#La funcion calcular_sueldo estaba implementada como si fuera un metodo de la clase DatosPago.
#Esto ocasionaba un clonficto porque la funcion no forma parte de la clase DatosPago.
#Asi que cambie el "self" por un parametro que recibe una instancia de DatosPago.
def calcular_sueldo(datos_pago):
    modalidad = datos_pago.empleado.modalidad
    horas = datos_pago.empleado.horasTrabajadas
    antiguedad = datos_pago.empleado.antiguedad

    if modalidad not in datos_pago.montos:
        raise ValueError("Modalidad de pago no válida.")

    if modalidad == "por_hora":
        if horas is None or horas <= 0:
            raise ValueError("Las horas trabajadas deben ser mayores a 0.")
        sueldo_base = datos_pago.montos["por_hora"] * horas
    else:
        sueldo_base = datos_pago.montos[modalidad]

    extra_antiguedad = sueldo_base * (antiguedad * 0.01)
    aporte = datos_pago.calcular_aporte()
    total_descuentos = sum(monto for _, monto in datos_pago.descuentos)
    sueldo_final = sueldo_base + extra_antiguedad + aporte - total_descuentos

    return {
        "sueldo_base": sueldo_base,
        "antiguedad_extra": extra_antiguedad,
        "aporte": aporte,
        "total_descuentos": total_descuentos,
        "sueldo_final": sueldo_final,
        "detalle_descuentos": datos_pago.descuentos
    }