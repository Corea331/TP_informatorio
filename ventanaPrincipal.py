import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from utilidades.menu import agregar_menu
from utilidades.reloj import crear_reloj, obtener_mes_anio
from utilidades.scrollbar import crear_area_con_scroll
from datosPersonales import personalDomestico
from datosPago import DatosPago
#llame a la funcion calcular sueldo desde el archivo caluladora.py
from caluladora import calcular_sueldo
from exelManager import crear_archivo_excel
import os

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Sueldos - Personal Doméstico")
        self.root.geometry("415x640")

        # Agregar menú, reloj y scrollbar
        agregar_menu(self.root)
        crear_reloj(self.root)
        self.frame_con_scroll = crear_area_con_scroll(self.root)

        # Variables auxiliares
        self.descuentos = []
        self.historial = []

        # Crear campos de entrada
        self.crear_campos_entrada()

    def crear_campos_entrada(self):
        campos = ["Nombre", "Apellido","CUIL", "DNI", "Domicilio", "Telefono", ]
        self.campos_entrada = {}

        for i, campo in  enumerate(campos):
            ttk.Label(self.frame_con_scroll, text=campo + ":").grid(row=i,sticky="w", column=0, padx=(10,0), pady=2)
            entrada = ttk.Entry(self.frame_con_scroll, width=40)
            entrada.grid(row=i,column=0,sticky="w", padx=(120,0), pady=2)
            self.campos_entrada[campo.lower()] = entrada

        fila = len(campos)

        # Fecha de ingreso
        ttk.Label(self.frame_con_scroll, text="Fecha de Ingreso (dd/mm/aaaa):").grid(row=fila,columnspan=2, column=0, sticky="w", padx=10, pady=5)
        self.fecha_ingreso = ttk.Entry(self.frame_con_scroll, width=20)
        self.fecha_ingreso.grid(row=fila,sticky="w", column=0, padx=(240,31), pady=8)
        fila += 1

        # Modalidad de pago
        ttk.Label(self.frame_con_scroll, text="Modalidad:").grid(row=fila, column=0, sticky="w", padx=10, pady=5)
        self.modalidad_var = tk.StringVar()
        modalidades = [("Mensual sin retiro", "mensual_sin_retiro"), 
                        ("Mensual con retiro", "mensual_con_retiro"), 
                        ("Por hora (menos 23 horas semanales)", "por_hora")]
        for i, (texto, valor) in enumerate(modalidades):
            ttk.Radiobutton(self.frame_con_scroll, text=texto, variable=self.modalidad_var, value=valor).grid(row=fila+i, column=0, sticky="w", padx=(100,0), pady=5)
        fila += len(modalidades)

        # Horas trabajadas
        ttk.Label(self.frame_con_scroll, text="Horas trabajadas:").grid(row=fila, column=0, sticky="w", padx=10, pady=5)
        self.horas_entrada = ttk.Entry(self.frame_con_scroll, width=20)
        self.horas_entrada.grid(row=fila, column=0, padx=(95,0), pady=5)
        fila += 1

        # Antigüedad
        ttk.Label(self.frame_con_scroll, text="Antigüedad (en años):").grid(row=fila, column=0, sticky="w", padx=10, pady=5)
        self.antiguedad_entrada = ttk.Entry(self.frame_con_scroll, width=20)
        self.antiguedad_entrada.grid(row=fila, column=0, padx=(95,0), pady=5)
        fila += 1

        # Aumentos paritarios
        self.aplicar_aumento = tk.BooleanVar(value=True)
        ttk.Checkbutton(self.frame_con_scroll, text="Aplicar aumentos paritarios", variable=self.aplicar_aumento).grid(row=fila, column=0, sticky="w", padx=10, pady=5)
        fila += 1

        # Valor del aumento en caso de aplicar
        ttk.Label(self.frame_con_scroll, text="Valor del aumento:").grid(row=fila, column=0, sticky="w", padx=10, pady=5)
        self.valor_aumento = ttk.Entry(self.frame_con_scroll, width=20)
        self.valor_aumento.insert(0, "0")  # Valor por defecto
        self.valor_aumento.grid(row=fila, column=0, padx=(95,0), pady=5)
        fila += 1

        # Agregar descuentos
        ttk.Label(self.frame_con_scroll, text="Descuentos (nombre y monto):").grid(row=fila, column=0, sticky="w", columnspan=2, padx=10, pady=5)
        fila += 1
        self.descuento_nombre = ttk.Entry(self.frame_con_scroll)
        self.descuento_monto = ttk.Entry(self.frame_con_scroll)
        self.descuento_nombre.grid(row=fila,sticky="w", column=0, padx=(10,0), pady=5)
        self.descuento_monto.grid(row=fila, column=0, padx=(40,0), pady=5)
        fila += 1
        ttk.Button(self.frame_con_scroll, text="Agregar Descuento", command=self.agregar_descuento).grid(row=fila, column=0, padx=10, pady=5)
        fila += 1

        # Botones de acción
        ttk.Button(self.frame_con_scroll, text="Calcular Sueldo", command=self.boton_calcular).grid(row=fila, column=0, padx=10, pady=5)
        fila += 1
        ttk.Button(self.frame_con_scroll, text="Salir", command=self.boton_salir).grid(row=fila, column=0, padx=10, pady=5)
        fila += 1

    def agregar_descuento(self):
        nombre = self.descuento_nombre.get().strip()
        try:
            monto = float(self.descuento_monto.get())
            if nombre and monto >= 0:
                self.descuentos.append((nombre, monto))
                messagebox.showinfo("Descuento agregado", f"{nombre}: ${monto}")
                self.descuento_nombre.delete(0, tk.END)
                self.descuento_monto.delete(0, tk.END)
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Debe ingresar un nombre y un monto válido")

    def boton_calcular(self):
        try:
            empleado = personalDomestico(
                #Renombre algunas variables porque estaban ocacionando conflictos
                nombre=self.campos_entrada["nombre"].get(),
                apellido=self.campos_entrada["apellido"].get(),
                cuil=self.campos_entrada["cuil"].get(),
                dni=self.campos_entrada["dni"].get(),
                domicilio=self.campos_entrada["domicilio"].get(),
                telefono=self.campos_entrada["telefono"].get(),
                #email=self.campos_entrada["email"].get(),
                modalidad=self.modalidad_var.get(),
                horasTrabajadas=int(self.horas_entrada.get()),
                antiguedad=int(self.antiguedad_entrada.get())
            )
            empleado.fecha_ingreso = self.fecha_ingreso.get()

            datos_pago = DatosPago(empleado)
            for desc in self.descuentos:
                datos_pago.descuentos.append(desc)
            #implemente la funcion calcular sueldo y le pase la instancia "datos_pago"
            resultado = calcular_sueldo(datos_pago)

            if self.aplicar_aumento.get():
                porcentaje = float(self.valor_aumento.get())
                resultado["sueldo_final"] += resultado["sueldo_final"] * (porcentaje / 100)

            self.datos_pago = datos_pago
            self.ultimo_empleado = empleado
            self.ultimo_pago = resultado

            messagebox.showinfo("Resultado",
                f"Sueldo Base: ${resultado['sueldo_base']:,.2f}\n"
                f"Antigüedad: ${resultado['antiguedad_extra']:,.2f}\n"
                f"Aporte: ${resultado['aporte']:,.2f}\n"
                f"Descuentos: ${resultado['total_descuentos']:,.2f}\n"
                f"Sueldo Final: ${resultado['sueldo_final']:,.2f}")

        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

    def boton_guardar_excel(self):
        try:
            nombre_mes, anio = obtener_mes_anio()
            nombre_archivo = f"Pago_{self.ultimo_empleado.nombre}_{self.ultimo_empleado.cuil}.xlsx"

            if os.path.exists(nombre_archivo):
                messagebox.showinfo("Aviso", f"Se agregará una nueva hoja con el nombre {nombre_mes}_{anio} al archivo existente.")
            else:
                messagebox.showinfo("Aviso", f"Se creará un nuevo archivo llamado {nombre_archivo}.")

            crear_archivo_excel(self.ultimo_empleado, self.ultimo_empleado, self.ultimo_pago, nombre_mes, anio)
            messagebox.showinfo("Guardado", "Archivo guardado correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo guardar el archivo: {e}")

    def boton_salir(self):
        if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    #Confiuracion de los temas y estilos
    #cambie el "column" de algunos campos y los separe usando "padx"
    #porque si no qudaban muy separados
    styles = ttk.Style(root)
    styles.theme_use = ('clam') 
    styles.configure('TFrame',
                background="#000000",
                borderwidth=0)
    styles.configure('TButton',
                background="#71a8fc",
                foreground="#000000",
                padding=6,
                relief='flat')
    styles.configure('TLabel',
                background="#def3f3",
                foreground="#000",
                font=('Arial', 12),
                padding=0
                )
    styles.configure('TEntry',
                background='#def3f3',
                foreground='#000',
                )
    styles.configure('TCheckbutton',
                background="#def3f3",
                foreground="#000000",
                font=('Arial', 12),)
    styles.configure('TRadiobutton',
                background="#def3f3",
                foreground="#000000",
                font=('Arial', 12),)
    styles.configure('TScrollbar',
                background="#def3f3",)
    
    root.resizable(False, False)
    app = VentanaPrincipal(root)
    root.mainloop()
