from tkinter import messagebox

def calcular_sueldo(self):
    modalidad = self.empleado.modalidad
    horas = self.empleado.horasTrabajadas
    antiguedad = self.empleado.antiguedad

    if modalidad not in self.montos:
        messagebox.showerror("Error", "Modalidad de pago no válida.")
        return None

    if modalidad == "por_hora":
        if horas is None or horas <= 0:
            messagebox.showwarning("Advertencia", "Las horas trabajadas deben ser mayores a 0.")
            return None
        sueldo_base = self.montos["por_hora"] * horas
    else:
        sueldo_base = self.montos[modalidad]

    extra_antiguedad = sueldo_base * (antiguedad * 0.01)
    aporte = self.calcular_aporte()
    total_descuentos = sum(monto for _, monto in self.descuentos)
    sueldo_final = sueldo_base + extra_antiguedad + aporte - total_descuentos

    return {
        "sueldo_base": sueldo_base,
        "antiguedad_extra": extra_antiguedad,
        "aporte": aporte,
        "total_descuentos": total_descuentos,
        "sueldo_final": sueldo_final,
        "detalle_descuentos": self.descuentos
    }