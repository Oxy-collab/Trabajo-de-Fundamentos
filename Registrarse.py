import customtkinter, tkinter
from tkinter import *

ventana = customtkinter.CTk()

#Tema que tendra la ventana
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

# Título de la ventana
ventana.title("Chicago Athletics")

# Dimensiones de la ventana
ventana.geometry("1366x768")


frame = customtkinter.CTkFrame(master = ventana,
                               width=350,
                               height=400,
                               bg_color="green",
                               fg_color="grey",
                               corner_radius=10
                               )
frame.pack(padx=20, pady=100)


label_titulo = customtkinter.CTkLabel(master = frame,
                                    text='Regístrarse',
                                    width= 120,
                                    height= 25,
                                    fg_color=('gray'),
                                    corner_radius=8
                                    )
label_titulo.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)


nombre_nuevo = customtkinter.CTkEntry(master = frame, 
                                     placeholder_text=('Nombre'),
                                     width=200,
                                     height=35,
                                     border_width=2,
                                     corner_radius=10
                                     )
nombre_nuevo.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)


apellido_nuevo = customtkinter.CTkEntry(master = frame, 
                                     placeholder_text=('Apellido'),
                                     width=200,
                                     height=35,
                                     border_width=2,
                                     corner_radius=10
                                     )
apellido_nuevo.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)


correo_nuevo = customtkinter.CTkEntry(master = frame, 
                                     placeholder_text=('Correo'),
                                     width=200,
                                     height=35,
                                     border_width=2,
                                     corner_radius=10
                                     )
correo_nuevo.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)


clave_nueva= customtkinter.CTkEntry(master = frame,
                                         placeholder_text='Contraseña',
                                         width=200,
                                         height=35,
                                         show='*',
                                         border_width=2,
                                         corner_radius=10
                                         )
clave_nueva.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)


def boton_evento():
        text_var.set('Te has registrado')


boton_registrar = customtkinter.CTkButton(master = frame, text='Registrarse', command= boton_evento)
boton_registrar.place(relx=0.5, rely= 0.8, anchor=tkinter.CENTER)

text_var = StringVar()

label = customtkinter.CTkLabel(master = frame,
                               textvariable = text_var,
                               width= 120,
                               height= 25,
                               fg_color=('black','gray'),
                               corner_radius=8
                               )
label.place(relx=0.5, rely=0.95, anchor=tkinter.CENTER)


ventana.mainloop()