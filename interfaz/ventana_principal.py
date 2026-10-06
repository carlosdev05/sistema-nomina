import tkinter as tk
from tkinter import ttk, messagebox

from modelos.asalariado import EmpleadoAsalariado
from modelos.por_horas import EmpleadoPorHoras
from modelos.comision import EmpleadoPorComision
from modelos.temporal import EmpleadoTemporal

from servicios.nomina import CalculadoraNomina


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Nómina")
        self.root.geometry("1050x700")
        self.root.minsize(950, 650)

        self.calculadora = CalculadoraNomina()

        self.crear_estilos()
        self.crear_interfaz()

    def crear_estilos(self):
        estilo = ttk.Style()

        estilo.theme_use("clam")

        estilo.configure(
            "Titulo.TLabel",
            font=("Segoe UI", 24, "bold")
        )

        estilo.configure(
            "Subtitulo.TLabel",
            font=("Segoe UI", 11)
        )

        estilo.configure(
            "TButton",
            font=("Segoe UI", 10, "bold"),
            padding=8
        )

        estilo.configure(
            "Treeview",
            rowheight=30,
            font=("Segoe UI", 10)
        )

        estilo.configure(
            "Treeview.Heading",
            font=("Segoe UI", 10, "bold")
        )

    def crear_interfaz(self):
        encabezado = ttk.Frame(self.root, padding=20)
        encabezado.pack(fill="x")

        ttk.Label(
            encabezado,
            text="Sistema de Nómina",
            style="Titulo.TLabel"
        ).pack(anchor="w")

        ttk.Label(
            encabezado,
            text="Gestión de empleados y cálculo automático de nómina",
            style="Subtitulo.TLabel"
        ).pack(anchor="w", pady=(5, 0))

        formulario = ttk.LabelFrame(
            self.root,
            text="Información del empleado",
            padding=20
        )
        formulario.pack(
            fill="x",
            padx=20,
            pady=10
        )

        self.tipo = tk.StringVar(value="Asalariado")
        self.nombre = tk.StringVar()
        self.identificacion = tk.StringVar()
        self.valor1 = tk.StringVar()
        self.valor2 = tk.StringVar()
        self.valor3 = tk.StringVar()

        ttk.Label(
            formulario,
            text="Tipo de empleado:"
        ).grid(row=0, column=0, padx=8, pady=8, sticky="w")

        tipos = [
            "Asalariado",
            "Por Horas",
            "Por Comisión",
            "Temporal"
        ]

        combo = ttk.Combobox(
            formulario,
            textvariable=self.tipo,
            values=tipos,
            state="readonly",
            width=25
        )
        combo.grid(row=0, column=1, padx=8, pady=8)
        combo.bind(
            "<<ComboboxSelected>>",
            self.actualizar_campos
        )

        ttk.Label(
            formulario,
            text="Nombre:"
        ).grid(row=1, column=0, padx=8, pady=8, sticky="w")

        ttk.Entry(
            formulario,
            textvariable=self.nombre,
            width=28
        ).grid(row=1, column=1, padx=8, pady=8)

        ttk.Label(
            formulario,
            text="Identificación:"
        ).grid(row=1, column=2, padx=8, pady=8, sticky="w")

        ttk.Entry(
            formulario,
            textvariable=self.identificacion,
            width=28
        ).grid(row=1, column=3, padx=8, pady=8)

        self.label_valor1 = ttk.Label(formulario)
        self.label_valor1.grid(
            row=2,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.entry_valor1 = ttk.Entry(
            formulario,
            textvariable=self.valor1,
            width=28
        )
        self.entry_valor1.grid(
            row=2,
            column=1,
            padx=8,
            pady=8
        )

        self.label_valor2 = ttk.Label(formulario)
        self.label_valor2.grid(
            row=2,
            column=2,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.entry_valor2 = ttk.Entry(
            formulario,
            textvariable=self.valor2,
            width=28
        )
        self.entry_valor2.grid(
            row=2,
            column=3,
            padx=8,
            pady=8
        )

        self.label_valor3 = ttk.Label(formulario)
        self.label_valor3.grid(
            row=3,
            column=0,
            padx=8,
            pady=8,
            sticky="w"
        )

        self.entry_valor3 = ttk.Entry(
            formulario,
            textvariable=self.valor3,
            width=28
        )
        self.entry_valor3.grid(
            row=3,
            column=1,
            padx=8,
            pady=8
        )

        self.boton = ttk.Button(
            formulario,
            text="Calcular nómina",
            command=self.calcular
        )
        self.boton.grid(
            row=4,
            column=0,
            columnspan=4,
            pady=15
        )

        resultado = ttk.LabelFrame(
            self.root,
            text="Resultado",
            padding=15
        )
        resultado.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        columnas = (
            "nombre",
            "tipo",
            "bruto",
            "beneficios",
            "deducciones",
            "fondo",
            "neto"
        )

        self.tabla = ttk.Treeview(
            resultado,
            columns=columnas,
            show="headings"
        )

        encabezados = {
            "nombre": "Empleado",
            "tipo": "Tipo",
            "bruto": "Salario bruto",
            "beneficios": "Beneficios",
            "deducciones": "Deducciones",
            "fondo": "Fondo ahorro",
            "neto": "Salario neto"
        }

        for columna, texto in encabezados.items():
            self.tabla.heading(
                columna,
                text=texto
            )
            self.tabla.column(
                columna,
                width=130,
                anchor="center"
            )

        self.tabla.pack(
            fill="both",
            expand=True
        )

        self.actualizar_campos()

    def actualizar_campos(self, event=None):
        tipo = self.tipo.get()

        self.valor1.set("")
        self.valor2.set("")
        self.valor3.set("")

        if tipo == "Asalariado":
            self.label_valor1.config(
                text="Salario mensual:"
            )
            self.label_valor2.config(
                text="Años en empresa:"
            )
            self.label_valor3.config(
                text=""
            )

        elif tipo == "Por Horas":
            self.label_valor1.config(
                text="Tarifa por hora:"
            )
            self.label_valor2.config(
                text="Horas trabajadas:"
            )
            self.label_valor3.config(
                text="Años en empresa:"
            )

        elif tipo == "Por Comisión":
            self.label_valor1.config(
                text="Salario base:"
            )
            self.label_valor2.config(
                text="Ventas:"
            )
            self.label_valor3.config(
                text=""
            )

        elif tipo == "Temporal":
            self.label_valor1.config(
                text="Salario mensual:"
            )
            self.label_valor2.config(
                text="Duración contrato (meses):"
            )
            self.label_valor3.config(
                text=""
            )

    def convertir_numero(self, valor):
        valor = valor.replace(",", "").replace(".", "")

        return float(valor)

    def calcular(self):
        try:
            nombre = self.nombre.get()
            identificacion = self.identificacion.get()
            tipo = self.tipo.get()

            if tipo == "Asalariado":
                empleado = EmpleadoAsalariado(
                    nombre,
                    identificacion,
                    self.convertir_numero(self.valor1.get()),
                    int(self.valor2.get())
                )

            elif tipo == "Por Horas":
                empleado = EmpleadoPorHoras(
                    nombre,
                    identificacion,
                    self.convertir_numero(self.valor1.get()),
                    float(self.valor2.get()),
                    float(self.valor3.get()),
                    False
                )

            elif tipo == "Por Comisión":
                empleado = EmpleadoPorComision(
                    nombre,
                    identificacion,
                    self.convertir_numero(self.valor1.get()),
                    self.convertir_numero(self.valor2.get())
                )

            else:
                empleado = EmpleadoTemporal(
                    nombre,
                    identificacion,
                    self.convertir_numero(self.valor1.get()),
                    int(self.valor2.get())
                )

            resultado = self.calculadora.calcular(empleado)

            self.tabla.insert(
                "",
                "end",
                values=(
                    resultado["nombre"],
                    resultado["tipo"],
                    self.formatear(resultado["salario_bruto"]),
                    self.formatear(resultado["beneficios"]),
                    self.formatear(resultado["deducciones"]),
                    self.formatear(resultado["fondo_ahorro"]),
                    self.formatear(resultado["salario_neto"])
                )
            )

            messagebox.showinfo(
                "Nómina calculada",
                f"Salario neto: "
                f"{self.formatear(resultado['salario_neto'])}"
            )

        except ValueError as error:
            messagebox.showerror(
                "Error",
                str(error)
            )

    @staticmethod
    def formatear(valor):
        return f"${valor:,.0f}"