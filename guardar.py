import matriz
import re

class guardar_Matriz:

    var=""

    def guardado(self, x, y, nombre, cadena):

        self.var=matriz.matriz_dato(x, y, nombre)
        self.var.crear(x,y)
        self.reemplazo(x,y,cadena)

        #self.var.recorrer()

    def reemplazo(self, x, y, cadena):
        lista = re.split('',cadena) 

        i=1
        j=1
        b=0
        while b < len(lista): 
            if lista[b]=="*" or lista[b]=="-":
                self.var.reemplazo(i, j, lista[b])
                #print(lista[b])
                #print(i)
                #print(j)
                #print(str(i)+'/'+str(j)+'/'+lista[b])
                i=i+1
                if i == x+1:
                    j=j+1
                    i=1
                if j == y+1:
                    break
            b=b+1

        print("//////////////////////////")    
        #self.var.recorrer() 
        self.var.recorido_normal()
        self.var.rotacion_Horizontal()
        self.var.rotacion_Vertical()

        #print(lista)
        