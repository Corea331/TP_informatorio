import tkinter as tk
from tkinter import messagebox

    """def crear_interfaz(self):
        # Título
        tk.Label(self.root, text="Calculadora de Sueldo Doméstico", font=("Arial", 14, "bold")).pack(pady=10)
        
        # Frame para datos del empleado
        frame_datos = tk.Frame(self.root)
        frame_datos.pack(pady=10)
        
        # Nombre del empleado
        tk.Label(frame_datos, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.nombre = tk.Entry(frame_datos, width=30)
        self.nombre.grid(row=0, column=1, padx=5, pady=5)
        
        # Categoría
        tk.Label(frame_datos, text="Categoría:").grid(row=1, column=0, padx=5, pady=5, sticky="ne")
        self.categoria = tk.StringVar(value="A")
        
        # Botones con las categorias de sueldo
        tk.Radiobutton(frame_datos, 
                        text="Mensual sin aportes", 
                        variable=self.categoria, 
                        value="A").grid(row=1, column=1, sticky="w")
        
        tk.Radiobutton(frame_datos, 
                        text="Por hora - hasta 23hs semanales ($2,897/hora)", 
                        variable=self.categoria, 
                        value="B").grid(row=2, column=1, sticky="w")
        
        tk.Radiobutton(frame_datos, 
                        text="Mensual - más de 23hs semanales", 
                        variable=self.categoria, 
                        value="C").grid(row=3, column=1, sticky="w")
        
        # Horas trabajadas (Categoria B)
        self.label_horas = tk.Label(frame_datos, text="Horas trabajadas:")
        self.entry_horas = tk.Entry(frame_datos, width=10)
        self.entry_horas.insert(0, "0")
        
        # Mostrar/ocultar horas según categoría seleccionada
        self.categoria.trace("w", self.actualizar_interfaz)
        
        # Botón de cálculo
        tk.Button(self.root, 
                text="Calcular Sueldo", 
                command=self.calcular_sueldo,
                bg="#4CAF50",  # Color verde
                fg="white",
                padx=10,
                pady=5).pack(pady=15)
        
        # Área de resultados
        self.resultado = tk.Text(self.root, height=8, width=50, state="disabled", bg="#f0f0f0")
        self.resultado.pack(pady=10)
    
    def actualizar_interfaz(self, *args):
        # Categoria por hora
        if self.categoria.get() == "B":
            self.label_horas.grid(row=4, column=0, padx=5, pady=5, sticky="e")
            self.entry_horas.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        else:
            self.label_horas.grid_remove()
            self.entry_horas.grid_remove()
    
    def calcular_sueldo(self):
        try:
            nombre = self.nombre.get()
            categoria = self.categoria.get()
            
            if not nombre: 
                messagebox.showwarning("Advertencia", "Por favor ingrese el nombre del empleado")
                return
            
            if categoria == "B":  # Categorias por hora
                horas = float(self.entry_horas.get())
                if horas <= 0:
                    messagebox.showwarning("Advertencia", "Las horas trabajadas deben ser mayores a 0")
                    return
                sueldo = self.sueldos["B"] * horas
            else:
                sueldo = self.sueldos[categoria]
                horas = "N/A"
            
            # Mostrar resultados
            self.resultado.config(state="normal")
            self.resultado.delete(1.0, tk.END)
            self.resultado.insert(tk.END, f"Empleado: {nombre}\n")
            self.resultado.insert(tk.END, f"Categoría: {self.obtener_descripcion_categoria(categoria)}\n")
            if categoria == "B":
                self.resultado.insert(tk.END, f"Horas trabajadas: {horas}\n")
            self.resultado.insert(tk.END, f"\nSueldo calculado: ${sueldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
            self.resultado.config(state="disabled")
            
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese valores numéricos válidos")
    
    def obtener_descripcion_categoria(self, categoria):
        descripciones = {
            "A": "Mensual sin aportes",
            "B": "Por hora (hasta 23hs semanales)",
            "C": "Mensual (más de 23hs semanales)"
        }
        return descripciones.get(categoria, "Desconocida")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraSueldo(root)
    root.mainloop()"""