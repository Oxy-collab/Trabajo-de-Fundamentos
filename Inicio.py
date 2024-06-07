import customtkinter, tkinter
from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from customtkinter import CTkButton  # Importa la clase CTkButton desde customtkinter


ventana = customtkinter.CTk()

# Tema que tendrá la ventana
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

# Título de la ventana
ventana.title("Chicago Athletics")

# Dimensiones de la ventana
ventana.geometry("1366x768")

# Crear un canvas para contener los widgets con desplazamiento
canvas = Canvas(ventana, bg="white")
canvas.pack(side=LEFT, fill=BOTH, expand=True)





# Agregar una barra de desplazamiento vertical al canvas
scrollbar = Scrollbar(ventana, orient=VERTICAL, command=canvas.yview)
scrollbar.pack(side=RIGHT, fill=Y)

# Configurar la relación entre el canvas y la barra de desplazamiento
canvas.configure(yscrollcommand=scrollbar.set)


# Frame barra inicio
frameop = customtkinter.CTkFrame(canvas, width=1366, height=100, fg_color="white", corner_radius=0)
canvas.create_window((0, 0), window=frameop, anchor='nw',)

# Logo
logo = Image.open("Imagenes/logo.jpg")
logoR = logo.resize((140,81))
ilogo = ImageTk.PhotoImage(logoR)

i2 = customtkinter.CTkLabel(canvas, image=ilogo,text="",                        
                                    width= 0,
                                    height= 0,
                                    fg_color=('black'),
                                     corner_radius=8)
canvas.create_window((30,10), window=i2, anchor='nw')

# Configurar el estilo de los botones
estilo_botones = {'borderwidth': 0, 'font': ('Roboto', 14, 'bold'), 'bg': 'white', 'fg': 'black', 'activebackground': 'white', 'activeforeground': 'black'}

# Crear y personalizar los botones
boton_hombre = Button(master=frameop, text='HOMBER', **estilo_botones)
boton_hombre.place(relx=0.35, rely=0.45, anchor=tkinter.CENTER)

boton_mujer = Button(master=frameop, text='MUJER', **estilo_botones)
boton_mujer.place(relx=0.45, rely=0.45, anchor=tkinter.CENTER)

boton_acc = Button(master=frameop, text='ACCESORIOS', **estilo_botones)
boton_acc.place(relx=0.55, rely=0.45, anchor=tkinter.CENTER)

boton_m = Button(master=frameop, text='MARCAS',**estilo_botones)
boton_m.place(relx=0.65, rely=0.45, anchor=tkinter.CENTER)

boton_login = Button(master=frameop, text='INICIAR SESION', **estilo_botones)
boton_login.place(relx=0.90, rely=0.45, anchor=tkinter.CENTER)




# Frame imagen inicio
frame = customtkinter.CTkFrame(canvas, width=0, height=0,  bg_color="green", fg_color="black", corner_radius=10)
canvas.create_window((0, 100), window=frame, anchor='nw',)


# Cargar la imagen usando PIL
imagen = Image.open("Imagenes/j-balvin-rio.webp")
imagen_rede = imagen.resize((1366,500))
tk_image = ImageTk.PhotoImage(imagen_rede)

boton = tk.Button(frame, image=tk_image, bd=0, highlightthickness=0)
boton.pack()


# Crear un widget de etiqueta para mostrar la imagen
#imagenm = customtkinter.CTkLabel(master=frame, image=tk_image, text="")
#imagenm.pack()

#logoI = Image.open("Imagenes/banner-web-jordan-retro-4-vivid-sulfur-hype1.webp")
#tk_image = ImageTk.PhotoImage()




# Estilo del texto (negro y en negrita)
estilo1 = {'font': ('Roboto', 24, 'bold'), 'fg': 'black','bg': 'white',}

# Crear un marco para "Sneakers recomendados"
frame_tsr = Frame(canvas, width=10, height=10, bg="white", highlightthickness=0)
canvas.create_window((500, 650), window=frame_tsr, anchor='nw')

# Crear una etiqueta de texto dentro del marco con el estilo aplicado
tsr = Label(frame_tsr, text="Sneakers recomendados", fg='black')
tsr.pack()
tsr.config(**estilo1)



#Sneakers
estiloti = {'font': ('Roboto', 12), 'fg': 'grey','bg': 'white',}


frame_s_re1 = customtkinter.CTkFrame(canvas, width=220, height=320, bg_color="white", corner_radius=5,)
canvas.create_window((100, 700), window=frame_s_re1, anchor='nw')

ifsr1 = Image.open("Imagenes/ninos-nike-dunk-low-year-of-the-dragon-sp24-fz5528-101-hype-1_360x.jpg")
ifsr1r = ifsr1.resize((220,320))
ifsr1I = ImageTk.PhotoImage(ifsr1r)
bfsr1 = tk.Button(frame_s_re1, image=ifsr1I, bd=0, highlightthickness=0)
bfsr1.pack()

frame_tsr1 = Frame(canvas, width=10, height=10, bg="white", highlightthickness=0)
canvas.create_window((100, 1030), window=frame_tsr1, anchor='nw')
tsr1 = Label(frame_tsr1, text="NIKE DUNK LOW YEAR OF THE \nDRAGON", fg='black')
tsr1.pack() 
tsr1.config(**estiloti)


frame_s_re2 = customtkinter.CTkFrame(canvas, width=220, height=320, bg_color="white", corner_radius=5)
canvas.create_window((411, 700), window=frame_s_re2, anchor='nw')

ifsr2 = Image.open("Imagenes/mujer-nike-air-more-uptempo-pink-foam-dv1137-600-hype-1_360x.jpg")
ifsr2r = ifsr2.resize((220,320))
ifsr2I = ImageTk.PhotoImage(ifsr2r)
bfsr2 = tk.Button(frame_s_re2, image=ifsr2I, bd=0, highlightthickness=0)
bfsr2.pack()

frame_tsr2 = Frame(canvas, width=10, height=10, bg="white", highlightthickness=0)
canvas.create_window((411, 1030), window=frame_tsr2, anchor='nw')
tsr2 = Label(frame_tsr2, text="NIKE MORE UPTEMPO PINK \nFOAM - MUJER", fg='black')
tsr2.pack()
tsr2.config(**estiloti)


frame_s_re3 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=5)
canvas.create_window((717, 700), window=frame_s_re3, anchor='nw')

ifsr3 = Image.open("Imagenes/kobe-8-protro-venice-beach-fq3548-001-hype-1.jpg")
ifsr3r = ifsr3.resize((220,320))
ifsr3I = ImageTk.PhotoImage(ifsr3r)
bfsr3 = tk.Button(frame_s_re3, image=ifsr3I, bd=0, highlightthickness=0)
bfsr3.pack()

frame_tsr3 = Frame(canvas, width=10, height=10, bg="white", highlightthickness=0)
canvas.create_window((717, 1030), window=frame_tsr3, anchor='nw')
tsr3 = Label(frame_tsr3, text="NIKE KOBE 8 PROTRO VENICE \nBEACH", fg='black')
tsr3.pack()
tsr3.config(**estiloti)


frame_s_re4 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=5)
canvas.create_window((1026, 700), window=frame_s_re4, anchor='nw')

ifsr4 = Image.open("Imagenes/nike-air-max-plus-3-black-wolf-grey-ho23-cj9684-002-hype-1_360x.jpg")
ifsr4r = ifsr4.resize((220,320))
ifsr4I = ImageTk.PhotoImage(ifsr4r)
bfsr4 = tk.Button(frame_s_re4, image=ifsr4I, bd=0, highlightthickness=0)
bfsr4.pack()

frame_tsr4 = Frame(canvas, width=10, height=10, bg="white", highlightthickness=0)
canvas.create_window((1026, 1026), window=frame_tsr4, anchor='nw')
tsr4 = Label(frame_tsr4, text="NIKE AIR MAX PLUS 3 BLACK \nWOLF GREY", fg='black')
tsr4.pack() 
tsr4.config(**estiloti)


frame_s_re5 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=5)
canvas.create_window((100, 1110), window=frame_s_re5, anchor='nw')

ifsr5 = Image.open("Imagenes/nike-air-max-plus-drift-all-day-fd4290-003-hype-1_360x.jpg")
ifsr5r = ifsr5.resize((220,320))
ifsr5I = ImageTk.PhotoImage(ifsr5r)
bfsr5 = tk.Button(frame_s_re5, image=ifsr5I, bd=0, highlightthickness=0)
bfsr5.pack()

frame_tsr5 = Frame(canvas, width=10, height=10, bg="white", highlightthickness=0)
canvas.create_window((100, 1440), window=frame_tsr5, anchor='nw')
tsr5 = Label(frame_tsr5, text="NIKE AIR MAX PLUS DRIFT \nALL DAY", fg='black')
tsr5.pack() 
tsr5.config(**estiloti)


frame_s_re6 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=5)
canvas.create_window((411, 1110), window=frame_s_re6, anchor='nw')

ifsr6 = Image.open("Imagenes/nike-air-force-1-low-evo-hf3630-100-hype-1_360x.jpg")
ifsr6r = ifsr6.resize((220,320))
ifsr6I = ImageTk.PhotoImage(ifsr6r)
bfsr6 = tk.Button(frame_s_re6, image=ifsr6I, bd=0, highlightthickness=0)
bfsr6.pack()

frame_tsr6 = Frame(canvas, width=10, height=10, bg="white", highlightthickness=0)
canvas.create_window((411, 1440), window=frame_tsr6, anchor='nw')
tsr6 = Label(frame_tsr6, text="NIKE AIR FORCE 1 LOW EVO", fg='black')
tsr6.pack() 
tsr6.config(**estiloti)


frame_s_re7 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=5)
canvas.create_window((717, 1110), window=frame_s_re7, anchor='nw')

ifsr7 = Image.open("Imagenes/mujer-jordan-2-retro-sail-black-sp24-dx4400-100-hype-1_360x.jpg")
ifsr7r = ifsr7.resize((220,320))
ifsr7I = ImageTk.PhotoImage(ifsr7r)
bfsr7 = tk.Button(frame_s_re7, image=ifsr7I, bd=0, highlightthickness=0)
bfsr7.pack()

frame_tsr7 = Frame(canvas, width=10, height=10, bg="white", highlightthickness=0)
canvas.create_window((711, 1440), window=frame_tsr7, anchor='nw')
tsr7 = Label(frame_tsr7, text="JORDAN 2 RETO SAILL BLACK \n- MUJER", fg='black')
tsr7.pack()
tsr7.config(**estiloti)


frame_s_re8 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=5)
canvas.create_window((1026, 1110), window=frame_s_re8, anchor='nw')

ifsr8 = Image.open("Imagenes/jordan-spizike-low-sail-fq1759-100-hype-1.jpg")
ifsr8r = ifsr8.resize((220,320))
ifsr8I = ImageTk.PhotoImage(ifsr8r)
bfsr8 = tk.Button(frame_s_re8, image=ifsr8I, bd=0, highlightthickness=0)
bfsr8.pack()

frame_tsr8 = Frame(canvas, width=10, height=10, bg="white", highlightthickness=0)
canvas.create_window((1026, 1440), window=frame_tsr8, anchor='nw')
tsr8 = Label(frame_tsr8, text="JORDAN SPIZIKE LOW SAIL", fg='black')
tsr8.pack() 
tsr8.config(**estiloti)

#Boton ver todo
bvt = Button(canvas, text='Ver Todo', font=('Roboto', 14, 'bold'), bg='black', fg='white', activebackground='white', activeforeground='black')
bvt.config(highlightthickness=0, relief="flat")
canvas.create_window((620, 1500), window=bvt, anchor='nw')



framemujer = customtkinter.CTkFrame(canvas, width=400, height=500, fg_color="black", corner_radius=0)
canvas.create_window((50, 1700), window=framemujer, anchor='nw',)

imagenm = Image.open("Imagenes/mujer.jpg")
imagenmr = imagenm.resize((350,500))
imagenmI = ImageTk.PhotoImage(imagenmr)

botonm = tk.Button(framemujer, image=imagenmI, bd=0, highlightthickness=0)
botonm.pack()

framesneaker = customtkinter.CTkFrame(canvas, width=400, height=500, fg_color="black", corner_radius=0)
canvas.create_window((475, 1700), window=framesneaker, anchor='nw',)

imagens = Image.open("Imagenes/Cactus Jack.jpg")
imagensr = imagens.resize((350,500))
imagensI = ImageTk.PhotoImage(imagensr)

botons = tk.Button(framesneaker, image=imagensI, bd=0, highlightthickness=0)
botons.pack()

framehombre = customtkinter.CTkFrame(canvas, width=400, height=500, fg_color="black", corner_radius=0)
canvas.create_window((900, 1700), window=framehombre, anchor='nw',)

imagenh = Image.open("Imagenes/Asap rocky.jpg")
imagenhr = imagenh.resize((350,500))
imagenhI = ImageTk.PhotoImage(imagenhr)

botonh = tk.Button(framehombre, image=imagenhI, bd=0, highlightthickness=0)
botonh.pack()



#Accesorios


# Crear un marco para "Sneakers recomendados"
frame_tac = Frame(canvas, width=10, height=10, bg="white", highlightthickness=0)
canvas.create_window((600, 2300), window=frame_tac, anchor='nw')

# Crear una etiqueta de texto dentro del marco con el estilo aplicado
tac = Label(frame_tac, text="Accesorios", fg='black')
tac.pack()
tac.config(**estilo1)


frame_s_d1 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=0)
canvas.create_window((100, 2400), window=frame_s_d1, anchor='nw')

frame_s_d2 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=0)
canvas.create_window((411, 2400), window=frame_s_d2, anchor='nw')

frame_s_d3 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=0)
canvas.create_window((717, 2400), window=frame_s_d3, anchor='nw')

frame_s_d4 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=0)
canvas.create_window((1026, 2400), window=frame_s_d4, anchor='nw')

frame_s_d5 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=0)
canvas.create_window((100, 2919), window=frame_s_d5, anchor='nw')

frame_s_d6 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=0)
canvas.create_window((411, 2919), window=frame_s_d6, anchor='nw')

frame_s_d7 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=0)
canvas.create_window((717, 2919), window=frame_s_d7, anchor='nw')

frame_s_d8 = customtkinter.CTkFrame(canvas, width=234, height=419, bg_color="white", corner_radius=0)
canvas.create_window((1026, 2919), window=frame_s_d8, anchor='nw')

#Boton ver todo
bvtd= customtkinter.CTkButton(canvas, text='Ver Todo', bg_color="white", corner_radius=0)
canvas.create_window((610, 3400), window=bvtd, anchor='nw')



# Configurar el tamaño del canvas
frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

ventana.mainloop()



