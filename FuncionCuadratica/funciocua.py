from tkinter import *
from tkinter import messagebox
import math
from tkinter.font import Font


#ICONO, IMAGEN Y COLORES DE LA VENTANA
interfaz=Tk()
interfaz.geometry("600x300")
interfaz.title("Calcular raices de una Función Cuadrática")
interfaz.config(bg="#F9858B")
interfaz.iconbitmap("707961.ico")
miImagen=PhotoImage(file="funcioncua.gif")
Label(image= miImagen).place(x=260, y=30)


# EJECUCÍON DE LA FÓRMULA Y SUS RESPECTIVOS RESULTADOS EN MENSAJES
def formula():

    n1Aux = n1.get()
    n2Aux = n2.get()
    n3Aux = n3.get()
    if n1Aux == 0:
        messagebox.showinfo("Respuesta", "El valor de A no puede ser cero")
    # EXCEPCÍON SI LA RAíZ CONTIENE UN NÚMERO NEGATIVO
    try:
       raiz = math.sqrt(n2Aux ** 2 - 4 * n1Aux * n3Aux)
    except ValueError:
        messagebox.showinfo("Respuesta", "La función no tiene soluciones reales")
    # EJECUCÍON SI LA FUNCíON TIENE SOLUCIONES REALES
    else:
        primer = (- n2Aux + raiz) / (2 * n1Aux)
        segundo = (- n2Aux - raiz) / (2 * n1Aux)
        if raiz == 0:
            messagebox.showinfo("Respuesta", "La función tiene una única raíz doble " + str(primer))
        else:
            messagebox.showinfo("Respuesta", "La primer raiz es "+ str(primer) + "\nLa segunda raiz es " + str(segundo))


#INGRESO DE CADA VALOR DE LA FUNCÍON Y EL BOTON PARA CALCULAR

Pregunta1= Label(interfaz, text="Ingrese el valor  A ", bg= "#ED335F", padx=5, pady=2, font="Italic", fg="#fff",relief= "groove").place(x=15, y=15)
n1=DoubleVar()
txtPregunta1= Entry(interfaz, textvariable=n1).place(x=15, y=46)

Pregunta2= Label(interfaz, text="Ingrese el valor  B ",bg= "#ED335F", padx=5, pady=2, font="Italic",fg="#fff", relief= "groove").place(x=15, y=75)
n2=DoubleVar()
txtPregunta2= Entry(interfaz, textvariable=n2).place(x=15, y=106)

Pregunta3= Label(interfaz, text="Ingrese el valor  C ",bg= "#ED335F", padx=5, pady=2, font="Italic", fg="#fff", relief= "groove").place(x=15, y=135)
n3=DoubleVar()
txtPregunta3= Entry(interfaz, textvariable=n3).place(x=15, y=166)

botonDesolucion = Button(interfaz, font="Italic", width=12, height=2, text="Calcular", command=formula, relief="raised", cursor="hand2",bg="#761137", fg="#fff").place(x=15, y=195)


interfaz.mainloop()

