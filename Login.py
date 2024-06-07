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
                               height=300,
                               bg_color="green",
                               fg_color="grey",
                               corner_radius=10)
frame.pack(padx=20, pady=100)


label_titulo = customtkinter.CTkLabel(master = frame,
                               text='Iniciar Sesion',
                               width= 120,
                               height= 25,
                               fg_color=('gray'),
                               corner_radius=8)

label_titulo.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)


id_ingresado= customtkinter.CTkEntry(master = frame, 
                                     placeholder_text=('Usuario'),
                                     width=200,
                                     height=35,
                                     border_width=2,
                                     corner_radius=10
                                     )
id_ingresado.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)

clave_ingresada= customtkinter.CTkEntry(master = frame,
                 placeholder_text='Contraseña',
                 width=200,
                 height=35,
                 show='*',
                 border_width=2,
                 corner_radius=10
                 )
clave_ingresada.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)

usuario = 'Chicago Athletics'
clave = '12345'

def boton_evento ():
    if (id_ingresado.get() == usuario and clave_ingresada == clave_ingresada):
        text_var.set('ingresaste')
    else:
        text_var.set('Ingresaste mal el usuario o la clave')


boton_login = customtkinter.CTkButton(master = frame, text='Iniciar Sesion',command=boton_evento)
boton_login.place(relx=0.5, rely= 0.8, anchor=tkinter.CENTER)

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