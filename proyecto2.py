from tkinter import filedialog
from tkinter import *
from tkinter import filedialog as fd
import sys
import lectura

class proyecto:
    ventana=Tk()

    def __init__(self):
        self.crearMenu()
        proyecto.ventana.geometry("900x500+0+0")
        
        proyecto.ventana.mainloop()


    def crearMenu(self):
        barra=Menu(proyecto.ventana)
        

        menu1=Menu(barra)
        menu2=Menu(barra)
        menu3=Menu(barra)
        menu4=Menu(barra)

        menu1.add_command(label="Cargar Archivo", command=self.cargarArchivo)

        menu2.add_command(label="Rotación horizontal de una imagen")
        menu2.add_command(label="Rotación vertical de una imagen")
        menu2.add_command(label="Transpuesta de una imagen")
        menu2.add_command(label="Limpiar zona de una imagen")
        menu2.add_command(label="Agregar línea horizontal a una imagen")
        menu2.add_command(label="Agregar línea vertical a una imagen")
        menu2.add_command(label="Agregar rectángulo")
        menu2.add_command(label="Agregar triángulo rectángulo")

        menu3.add_command(label="Reporte")

        menu4.add_command(label="Informacion")
        menu4.add_command(label="Documentacion")

        barra.add_cascade(label="Cargar", menu=menu1)
        barra.add_cascade(label="Operaciones", menu=menu2)
        barra.add_cascade(label="Reportes", menu=menu3)
        barra.add_cascade(label="Ayuda", menu=menu4)
        proyecto.ventana.config(menu=barra)

    def cargarArchivo(self):
        #nombreArch=proyecto.ventana.filename
        nombreArch= filedialog.askopenfilename(initialdir = r"C:\Users\Administrator\Desktop",title = "Select file",filetypes = (("xml files","*.xml"),("all files","*.*")))
        #nombreArch = fd.askopenfilename(initialdir=r"C:\Users\Administrator\Desktop\proyecto2\proyecto2.py", title="Seleccione archivo", filetypes=("xml files","*.xml"))
        if nombreArch != '':
            arch=open(nombreArch, "r", encoding="utf-8")
            contenido=arch.read()
            arch.close()
            leer=lectura.leer(contenido)
        #print(contenido)


    

cosa = proyecto()

#Rotación horizontal de una imagen: lectura de abajo hacia arriba normal
#Rotación vertical de una imagen: lectura de derecha a izquierda
#Transpuesta de una imagen: primero recorrer desde la ultima columna hasta la primera normal, despues de abajo hacia arriba normal

        






