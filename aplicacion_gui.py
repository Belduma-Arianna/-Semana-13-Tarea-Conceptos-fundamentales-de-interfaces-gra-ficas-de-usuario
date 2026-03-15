Import tkinter as tk
from tkinter import messagebox, ttk


class GestorDatosApp:
    def __init__(self, ventana):
        # Configuración de la ventana principal
        self.ventana = ventana
        self.ventana.title("Sistema de Gestión de Información - Registro Académico")
        self.ventana.geometry("480x520")
        self.ventana.configure(bg="#f2f2f2")

        # --- SECCIÓN 1: DISEÑO DE LA INTERFAZ ---

        # Etiqueta de encabezado
        self.lbl_titulo = tk.Label(ventana, text="Panel de Control de Datos", font=("Helvetica", 14, "bold"),
                                   bg="#f2f2f2", pady=15)
        self.lbl_titulo.pack()

        # Frame contenedor para la entrada de texto
        self.frame_entrada = tk.Frame(ventana, bg="#f2f2f2")
        self.frame_entrada.pack(pady=10)

        tk.Label(self.frame_entrada, text="Nombre del elemento:", font=("Arial", 10), bg="#f2f2f2").grid(row=0,
                                                                                                         column=0,
                                                                                                         padx=5)

        # Campo de texto (Entry)
        self.campo_texto = tk.Entry(self.frame_entrada, width=30, font=("Arial", 11))
        self.campo_texto.grid(row=0, column=1, padx=5)

        # Evento: Permite agregar datos al presionar la tecla Enter
        self.campo_texto.bind('<Return>', lambda e: self.agregar_informacion())

        # --- SECCIÓN 2: BOTONES Y EVENTOS ---

        self.frame_botones = tk.Frame(ventana, bg="#f2f2f2")
        self.frame_botones.pack(pady=15)

        # Botón para la funcionalidad de Agregar
        self.btn_add = tk.Button(self.frame_botones, text="Agregar", command=self.agregar_informacion, bg="#28a745",
                                 fg="white", width=12, font=("Arial", 9, "bold"))
        self.btn_add.grid(row=0, column=0, padx=10)

        # Botón para la funcionalidad de Limpiar
        self.btn_clear = tk.Button(self.frame_botones, text="Limpiar Lista", command=self.limpiar_tabla, bg="#d33",
                                   fg="white", width=12, font=("Arial", 9, "bold"))
        self.btn_clear.grid(row=0, column=1, padx=10)

        # --- SECCIÓN 3: TABLA DE DATOS (Treeview) ---

        self.tabla = ttk.Treeview(ventana, columns=("Columna1"), show='headings', height=10)
        self.tabla.heading("Columna1", text="Lista de Datos Ingresados")
        self.tabla.column("Columna1", width=400, anchor="center")
        self.tabla.pack(pady=10, padx=20)

    # --- FUNCIONALIDADES DEL SISTEMA ---

    def agregar_informacion(self):
        # Captura el valor del campo de texto
        dato = self.campo_texto.get()

        # Validación para asegurar que el campo no esté vacío
        if dato.strip():
            self.tabla.insert("", tk.END, values=(dato,))
            self.campo_texto.delete(0, tk.END)  # Limpiar el campo tras el éxito
        else:
            messagebox.showwarning("Atención", "El campo de texto no puede estar vacío.")

    def limpiar_tabla(self):
        # Obtiene todos los elementos de la tabla
        registros = self.tabla.get_children()

        if registros:
            # Ventana de confirmación antes de eliminar
            if messagebox.askyesno("Confirmar", "¿Está seguro de que desea borrar todos los registros?"):
                for r in registros:
                    self.tabla.delete(r)
        else:
            messagebox.showinfo("Aviso", "La tabla ya se encuentra vacía.")


# Inicialización del programa
if __name__ == "__main__":
    root = tk.Tk()
    app = GestorDatosApp(root)
    root.mainloop()
