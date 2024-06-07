from tkinter import *
from PIL import Image, ImageTk

# Crear la ventana
ventana = Tk()
ventana.title("Ejemplo de inserción de imagen")

# Cargar la imagen con PIL y convertirla a PhotoImage
imagen = Image.open("Imagenes/Nike-Kobe-6-Protro-Reverse-Grinch-Product-_1_.jpg")
tk_image = ImageTk.PhotoImage(imagen)

# Crear un widget de etiqueta para mostrar la imagen
label_imagen = Label(ventana, image=tk_image)
label_imagen.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()