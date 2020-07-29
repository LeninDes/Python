from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter.messagebox import *
from random import randint
from PIL import ImageTk

letrasUsadas=[]
vidas = 6
letrasAcertadas=0
def colocarLetras():
    x=50
    y=150
    contador = 0
    Label(canvas, text = "Estas son tus letras que te faltan Utilizar").place(x=50, y=100)
    
    for i in range(26):
        contador += 1
        letrasLabel[i].place(x=x, y=y)
        x+=30
        if contador == 5:
            y+=35
            contador = 0
            x=50
def probarletraFuncion():
    global vidas
    global letrasAcertadas
    # get() = cobtener el contenido de dicha variable
    letrasUsadas.append(letraObtenida.get())
    print(letrasUsadas)
    letrasLabel[ord(letraObtenida.get())-97].config(text="")

    if letraObtenida.get() in palabra:
        if palabra.count(letraObtenida.get())>1:
            letrasAcertadas+=palabra.count(letraObtenida.get())
            for i in range(len(palabra)):
                if palabra[i]==letraObtenida.get():
                    guiones[i].config(text=""+ letraObtenida.get())
        else:
            letrasAcertadas +=1
            guiones[palabra.index(letraObtenida.get())].config(text=""+ letraObtenida.get())
        if letrasAcertadas ==len(palabra):
            showwarning(title="Victoria", message="Felicitaciones has ganado")
    else:
        vidas-=1
        canvas.itemconfig(imagen_id, image=imagenes[vidas-1])
        if(vidas == 0):
            showwarning(title="Derrota", message="Se te terminaron las vidas" )

#-----------TKINTER--------
ventana = Tk()
ventana.geometry("1000x600")
ventana.resizable(0,0)
ventana.iconbitmap("./JuegoFP/ima/una.ico")
ventana.title("FUNDAMENTOS DE PROGRAMACION - UNAP")


def salir():
    resultado= MessageBox.askquestion("Salir" ,"¿Desea seguir ejecutando el programa?")

    if resultado != "yes":
        ventana.destroy()

# ------------Mi Menu---------------
mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

archivo = Menu(mi_menu, tearoff=0)
archivo.add_command(label="Ajustes")
archivo.add_separator()
archivo.add_command(label="Salir", command=salir)

mi_menu.add_command(label="Archivo")
mi_menu.add_command(label="Juego")
mi_menu.add_command(label="Configuraciones")
mi_menu.add_cascade(label="Usuario", menu=archivo)

archivo = open("./JuegoFP/palabras.txt", "r")
conjuntoPalabras = list(archivo.read().split("\n"))
palabra = conjuntoPalabras[randint(0, len(conjuntoPalabras)-1)].lower()

letraObtenida=StringVar()

texto = Label(ventana, text="JUGANDO CON COVILETRAS")
texto.pack()

texto.config(
            fg="white",
            bg="#44CDC7",
            padx=50,
            pady=7,
            font=("Consolas", 30 )
)
texto.pack(side=TOP, fill=X)

pregunta = Label(ventana, text="Responda: ¿Cual es uno de los sintomas mas habituales del covid-19 ?")
pregunta.pack()

pregunta.config(
            fg="white",
            bg="#5C757F",
            padx=20,
            pady=1,
            font=("Consolas", 10 )
)
pregunta.pack(side=TOP, fill=X)




ventana.config(
    width=1000,
    height=600
)

canvas = Canvas(ventana, width=1000, height=600)
canvas.pack(expand=True, fill="both")

imagenes = [
    PhotoImage(file = "./JuegoFP/img7.png"),
    PhotoImage(file = "./JuegoFP/img5.png"),
    PhotoImage(file = "./JuegoFP/img4.png"),
    PhotoImage(file = "./JuegoFP/img3.png"),
    PhotoImage(file = "./JuegoFP/img2.png"),
    PhotoImage(file = "./JuegoFP/img2.png"),
    PhotoImage(file = "./JuegoFP/img1.png"),
]
imagen_id = canvas.create_image(750, 300, image=imagenes[6])

Label(canvas, text="Introduce una letra", font=("Verdana", 24)
    ).grid(row=0, column=0, padx=10, pady=10)
letra = Entry(canvas, width=2, font=("Verdana", 24),textvariable=letraObtenida
    ).grid(row=0, column=1, padx=10, pady=10)
probarLetra = Button(canvas, text="Probar", bg="#44CDC7",padx=5, pady=3, font=("Consolas", 10 ), command=probarletraFuncion
    ).grid(row=1, column=0, pady=10)


letrasLabel = [Label(canvas, text=chr(j+97), font=("Verdana",20)) for j in range(26)]
colocarLetras()

guiones = [Label(canvas, text="_", font=("verdana", 30)) for _ in palabra]
inicialX=200
for i in range(len(palabra)):
    guiones[i].place(x=inicialX, y=400)
    inicialX += 50

ventana.mainloop()