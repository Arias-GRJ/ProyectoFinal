import tkinter as tk
import string
import random

# Función para generar la contraseña
def generar_contraseña():
    try:
        longitud = int(entry_longitud.get())  # Obtener longitud desde el campo de entrada

        # Validar longitud
        if longitud < 8 or longitud > 20:
            label_resultado.config(text="La longitud debe estar entre 8 y 20 caracteres.")
            return

        # Obtener los caracteres seleccionados por el usuario
        caracteres = ""
        if var_letras.get():
            caracteres += string.ascii_letters
        if var_numeros.get():
            caracteres += string.digits
        if var_simbolos.get():
            caracteres += string.punctuation

        if caracteres == "":
            label_resultado.config(text="Debe seleccionar al menos un tipo de carácter.")
            return

        # Generar la contraseña aleatoria
        contraseña = "".join(random.choice(caracteres) for i in range(longitud))

        # Mostrar la contraseña generada
        label_resultado.config(text="Contraseña generada: " + contraseña)

    except ValueError:
        label_resultado.config(text="Por favor ingrese un número válido para la longitud.")

# Función para copiar la contraseña al portapapeles
def copiar_contraseña():
    try:
        ventana.clipboard_clear()  # Limpiar el portapapeles
        ventana.clipboard_append(label_resultado.cget("text").replace("Contraseña generada: ", ""))  # Copiar contraseña
        label_resultado.config(text="Contraseña copiada al portapapeles.")
    except Exception as e:
        label_resultado.config(text="Primero genere una contraseña.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Generador de Contraseñas")

# Etiqueta para la longitud
label_longitud = tk.Label(ventana, text="Ingrese el tamaño de la contraseña (8-20):")
label_longitud.pack(pady=10)

# Campo de entrada para la longitud
entry_longitud = tk.Entry(ventana)
entry_longitud.pack(pady=5)

# Variables para los tipos de caracteres
var_letras = tk.BooleanVar(value=True)
var_numeros = tk.BooleanVar(value=True)
var_simbolos = tk.BooleanVar(value=True)

# Checkbox para seleccionar caracteres
checkbox_letras = tk.Checkbutton(ventana, text="Incluir letras (a-z, A-Z)", variable=var_letras)
checkbox_letras.pack(pady=5)

checkbox_numeros = tk.Checkbutton(ventana, text="Incluir números (0-9)", variable=var_numeros)
checkbox_numeros.pack(pady=5)

checkbox_simbolos = tk.Checkbutton(ventana, text="Incluir símbolos (!, @, #, $, etc.)", variable=var_simbolos)
checkbox_simbolos.pack(pady=5)

# Botón para generar la contraseña
boton_generar = tk.Button(ventana, text="Generar Contraseña", command=generar_contraseña)
boton_generar.pack(pady=10)

# Etiqueta para mostrar el resultado
label_resultado = tk.Label(ventana, text="Contraseña generada: ")
label_resultado.pack(pady=20)

# Botón para copiar la contraseña
boton_copiar = tk.Button(ventana, text="Copiar Contraseña", command=copiar_contraseña)
boton_copiar.pack(pady=5)

# Ejecutar la ventana
ventana.mainloop()
