import tkinter as tk
import tkinter.messagebox as messagebox
from tkinter import filedialog
from tkinter import ttk

def copiar_campo(campo):
    if isinstance(campo, tk.Text):
        valor = campo.get("1.0", tk.END).strip()
    else:
        valor = campo.get()
    root.clipboard_clear()
    root.clipboard_append(valor)
    if campo in campos:
        messagebox.showinfo("Copia exitosa", f"El campo ha sido copiado al portapapeles.")

def restablecer_campo(campo):
    if isinstance(campo, tk.Text):
        campo.delete("1.0", tk.END)
    else:
        campo.delete(0, tk.END)

def copiar_todo():
    informacion = "\n".join([f"{label} {campo.get('1.0', tk.END).strip()}" if isinstance(campo, tk.Text) else f"{label} {campo.get()}" for label, campo in campos if (isinstance(campo, tk.Text) and campo.get("1.0", tk.END).strip()) or (isinstance(campo, tk.Entry) and campo.get())])
    if informacion:
        root.clipboard_clear()
        root.clipboard_append(informacion)
        messagebox.showinfo("Copia exitosa", "Toda la información ha sido copiada al portapapeles.")
    else:
        messagebox.showwarning("Nada que copiar", "No hay campos con datos para copiar.")

def restablecer_todo():
    for _, campo in campos:
        if isinstance(campo, tk.Text):
            campo.delete("1.0", tk.END)
        else:
            campo.delete(0, tk.END)

def guardar_registro():
    global registro_actual
    informacion = "\n".join([f"{label} {campo.get('1.0', tk.END).strip()}" if isinstance(campo, tk.Text) else f"{label} {campo.get()}" for label, campo in campos if (isinstance(campo, tk.Text) and campo.get("1.0", tk.END).strip()) or (isinstance(campo, tk.Entry) and campo.get())])
    if informacion:
        registro_actual += 1
        registro_guardado = f"{registro_actual:02d}\n{informacion}\n"
        registros_temporales.append(registro_guardado)
        messagebox.showinfo("Registro guardado", f"Registro {registro_actual:02d} guardado correctamente.")
    else:
        messagebox.showwarning("Nada que guardar", "No hay registros para guardar.")

def guardar_todo():
    if registros_temporales:
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if archivo:
            with open(archivo, "w") as f:
                f.write("\n\n".join(registros_temporales))  
            messagebox.showinfo("Guardado exitoso", "Todos los registros han sido guardados correctamente.")
            registros_temporales.clear()
            reset_registro_actual()
    else:
        messagebox.showwarning("Nada que guardar", "No hay registros para guardar.")

def reset_registro_actual():
    global registro_actual
    registro_actual = 0

root = tk.Tk()
root.title("REG KEVIN")
root.geometry("900x600")  
root.configure(bg="lightgray")  

campos = []
registros_temporales = []
registro_actual = 0

# ...
def agregar_campo(label_text, height=1, width=80):  
    campo_frame = tk.Frame(root, bg="lightgray")  
    campo_frame.grid(row=len(campos), column=0, padx=10, pady=5, sticky="w")

    tk.Label(campo_frame, text=label_text, bg="lightgray", fg="black", width=10).pack(side=tk.LEFT, padx=(0, 10))
    if label_text == "Dirección:":
        # ...
       # ...
        entry_combobox = ttk.Combobox(campo_frame, font=("Arial", 10), width=77)  # Ajustar el ancho de la lista desplegable
        entry_combobox.pack(side=tk.LEFT, padx=(0, 10), fill="x", expand=True)
        entry_combobox['values'] = [
    "Alto Hospicio - Avenida la Pampa 3121, L-16",
    "Ancud - Pudeto 341, L-13",
    "Angol - Chorillos 468, L-1",
    "Antofagasta - Arturo Prat 444",
    "Antofagasta Mall Plaza - Balmaceda 2355 L-H y K",
    "Arauco - Esmeralda 323, L-1",
    "Arica - 21 de Mayo 372",
    "Arica - 21 de mayo 477",
    "Calama - Balmaceda 4063",
    "Calama - Eleuterio Ramírez 1897",
    "Castro - Blanco Encalada 286",
    "Cañete - Séptimo de línea 654",
    "Chillán - El Roble 533",
    "Chillán - El Roble 580",
    "Concepcion - Mall Plaza Bíobío - Av Los Carrera Poniente 301, L-127, 131 y 135",
    "Concepción - Lincoyán 569",
    "Concepción - OHiggins 475",
    "Constitución - Prieto 345",
    "Copiapó - Atacama 456",
    "Copiapó - Los Carrera 3202",
    "Coquimbo - Aldunate 1181",
    "Coquimbo - Aldunate 1568",
    "Coronel - Carlos Cousiño, L-115-119",
    "Coyhaique - José de Moraleda 442",
    "Curicó - Peña 596",
    "Curicó - Yungay 630",
    "Iquique - Bartolomé Vivar 738",
    "Iquique - Tarapacá 30",
    "La Ligua - Ortiz de las Rzas 522, L-102",
    "La Serena - Prat 575",
    "La Serena Mall plaza - Alberto Solari 1400, L-C-159",
    "Linares - Independencia 489",
    "Linares - Yumbel 520",
    "Limache - Urmeneta 93",
    "Lota - Pedro Aguirre Cerda 463, L-11",
    "Los Ángeles - Valdivia 409",
    "Los Ángeles Mall plaza - Valdivia 440, L-137 , 139",
    "Los Andes - Bernardo OHiggins 442",
    "Melipilla - Serrano 542",
    "Osorno - Eleuterio - Ramírez 944",
    "Osorno - Eleuterio Ramírez 1190",
    "Ovalle - Vicuña Mackenna 292",
    "Parral - Anibal Pinto 573",
    "Puerto Montt - Chillán 80",
    "Puerto Montt - Urmeneta 320",
    "Punta Arenas - Gobernador Carlos Bories 847-B",
    "Quillota - Chacabuco 241",
    "Quillota - Maipú 210",
    "Quilpué - Los Carrera 700",
    "Quilpué - Portales 711",
    "Rancagua - Eduardo Frei Montalva 340 L-10",
    "Rancagua - OCarrol 438 Maule",
    "San Antonio Mall Arauco - Av Ramón Barros Luco 105, L-23 - 25",
    "San Fernando - Manuel Rodriguez 971",
    "San Felipe Open Plaza - Av Libertador Bernardo O Higgins 1150, L-116",
    "San Javier - Arturo Prat 2345",
    "San Miguel - Av José Miguel Carrera 5371-D, L-4",
    "San Miguel - Gran Avenida Jose Miguel Carrera 5371 L-C",
    "Santiago (Cerrillos) Mall Plaza Oeste - Av Américo Vespucio Sur 1501 Santiago",
    "Santiago (Estacion central) - Mall Plaza Alameda - Ohiggins 3470 L-CZ-101",
    "Santiago (Huechuraba) Mall Plaza Norte - Av Américo Vespucio 1737 L-1012-1017",
    "Santiago (Las Condes) - Av Apoquindo 2968",
    "Santiago (Las Condes) Av Las Condes 9166 - L-9",
    "Santiago (Las Condes) - Av las Condes 9146, L-5",
    "Santiago (La Cisterna) - Av. Américo Vespucio 33, L-13-A",
    "Santiago (La florida) Mall Florida Center - Av Vicuña Mackenna 6100, L-3037",
    "Santiago (La florida) - Mall Plaza Vespucio - Av Vicuña Mackenna Oriente 7110, L-105",
    "Santiago (Maipu) - Avenida Cinco de Abril 33, L-10",
    "Santiago (Maipu) Mall Arauco - Av Américo Vespucio 399, L-8",
    "Santiago (Maipu) - Av Pajaritos - 3090, torre B L-8",
    "Santiago (Maipu) - Pinochet le Brun L-37 Santiago",
    "Santiago (Nunoa) - Avenida Irarrázabal 3439",
    "Santiago (Nunoa) - Av Pedro de Valdivia 3545",
    "Santiago (Vitacura) - Av Las Condes 11380",
    "Santiago (Providencia) Costanera Center - Av Andrés Bello 2425, L-128 - 133",
    "Santiago (Puente Alto) - Av Concha y Toro 1060",
    "Santiago (Puente Alto) - Av Manuel Rodriguez 047",
    "Santiago (Quilin) Mall Plaza Quilín - Mar Tirreno 3349, L-1108",
    "Santiago (San Bernardo) - Av Colón 625",
    "Santiago (San Bernardo) - Eyzaguirre 650, L-217",
    "Santiago (San Miguel) - Av José Miguel Carrera 5371-D, L-4",
    "Santiago Centro - Ahumada 268",
    "Santiago Centro - Estado 47",
    "Santiago Centro - Huérfanos 1219",
    "Santiago Centro - Merced 849",
    "Santiago Centro - Ohiggins 1475",
    "Santiago Centro - San Antonio 467",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 1",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 2",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 3",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 4",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 5",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 6",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 7",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 8",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 9",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 10",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 11",
    "Santiago Edificio Corporativo - El Salto 5450 - Piso 12",
    "Talagante - Bernardo Ohiggins 1061",
    "Talca - 1 Norte 1367",
    "Talca - 1 Sur 1601 - Maule VII",
    "Talcahuano Bulnes 33",
    "Talcahuano Mall Plaza Trébol - Av Jorge Alessandri 3177, L-H-104, 112, 120 y 128",
    "Temuco - Antonio Varas 832",
    "Temuco - Av Alemania 890",
    "Tomé - Mariano Egaña 1093, L-101",
    "Valdivia - Arauco 136",
    "Valdivia - Av Alemania 667",
    "Valparaíso - Av Pedro Montt 2033",
    "Valparaíso - Av Pedro Montt 2352",
    "Valparaíso - Av Valparaíso 741",
    "Vallenar - Av. Brasil 602",
    "Villa Alemana - Av Valparaíso 741",
    "Villarrica - Camilo Henriquez 569",
    "Viña Del Mar- 13 Norte 856",
    "Viña Del Mar - Av Valparaíso 637",
    "Viña Del Mar Mall marina arauco - Libertad 1348, L-E-04"
]  # Lista de direcciones
        entry_combobox.set("Seleccione una dirección")  # Valor por defecto
        entry = entry_combobox  # Utilizar entry_combobox como referencia
# ...

# ...

    elif label_text in ("Solicitud:", "Solución:"):
        entry = tk.Text(campo_frame, height=height, wrap=tk.WORD, width=width, font=("Arial", 10))  
    else:
        entry = tk.Entry(campo_frame, width=width, font=("Arial", 10))  
    entry.pack(side=tk.LEFT, padx=(0, 10), fill="x", expand=True)  

    campos.append((label_text, entry))

    botones_frame = tk.Frame(campo_frame, bg="lightgray")  
    botones_frame.pack(side=tk.RIGHT)  

    btn_copiar = tk.Button(botones_frame, text="Copiar", command=lambda campo=entry if label_text != "Dirección:" else entry_combobox: copiar_campo(campo), bg="green", fg="black", font=("Arial", 8, "bold"))
    btn_copiar.pack(side=tk.LEFT, padx=2)  
    btn_copiar.config(cursor="hand2")  

    btn_restablecer = tk.Button(botones_frame, text="Restablecer", command=lambda campo=entry if label_text != "Dirección:" else entry_combobox: restablecer_campo(campo), bg="orange", fg="black", font=("Arial", 8, "bold"))
    btn_restablecer.pack(side=tk.LEFT, padx=2)  
    btn_restablecer.config(cursor="hand2")  

# ...

def agregar_separador():
    tk.Frame(root, height=2, bg="gray").grid(row=len(campos) + 1, column=0, columnspan=3, padx=10, pady=5, sticky="ew")

def agregar_filas_vacias():
    tk.Label(root, text="", bg="lightgray").grid(row=len(campos) + 1, column=0)  
    tk.Label(root, text="", bg="lightgray").grid(row=len(campos) + 2, column=0)  

def agregar_botones():
    botones_frame = tk.Frame(root, bg="lightgray")  
    botones_frame.grid(row=len(campos) + 1, column=0, columnspan=4, padx=10, pady=10)  

    btn_copiar_todo = tk.Button(botones_frame, text="Copiar Todo", command=copiar_todo, bg="green", fg="black", font=("Arial", 8, "bold"))
    btn_copiar_todo.pack(side=tk.LEFT, padx=2, pady=2)  
    btn_copiar_todo.config(cursor="hand2")  

    btn_restablecer_todo = tk.Button(botones_frame, text="Restablecer Todo", command=restablecer_todo, bg="orange", fg="black", font=("Arial", 8, "bold"))
    btn_restablecer_todo.pack(side=tk.LEFT, padx=2, pady=2)  
    btn_restablecer_todo.config(cursor="hand2")  

    btn_guardar_registro = tk.Button(botones_frame, text="Guardar Registro", command=guardar_registro, bg="blue", fg="black", font=("Arial", 8, "bold"))
    btn_guardar_registro.pack(side=tk.LEFT, padx=2, pady=2)  
    btn_guardar_registro.config(cursor="hand2")  

    btn_guardar_todo = tk.Button(botones_frame, text="Guardar Todo", command=guardar_todo, bg="red", fg="black", font=("Arial", 8, "bold"))
    btn_guardar_todo.pack(side=tk.LEFT, padx=2, pady=2)  
    btn_guardar_todo.config(cursor="hand2")  

def agregar_separador():
    tk.Frame(root, height=2, bg="gray").grid(row=len(campos) + 2, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

agregar_campo("Nombre:")
agregar_campo("Dirección:")
agregar_campo("Rut:")
agregar_campo("Correo:")
agregar_campo("Contacto:")
agregar_campo("ID EQUIPO:")
agregar_campo("IP EQUIPO:")
agregar_campo("Solicitud:", height=4)  
agregar_campo("Solución:", height=6, width=80)
agregar_campo("MDA:")  

agregar_separador()
agregar_botones()

root.grid_rowconfigure(len(campos) + 2, weight=1)

reset_registro_actual()

root.mainloop()




