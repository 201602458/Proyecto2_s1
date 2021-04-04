import re
import guardar

class leer:
    lista = []
    def __init__(self, archivo):
        self.archivo=archivo
        self.lectura(archivo)

    
    
    def lectura(self, arch):
        #self.lista = re.split('<|>|'+chr(32)+'|'+chr(9)+'|'+chr(34)+'|\n|'+chr(10)+'|'+chr(0),arch) 
        self.lista = re.split('<|>|'+chr(32)+'|'+chr(9)+'|'+chr(34),arch) 
       
        b=0
        c=len(self.lista)

        while b <= c:
          
            if self.lista[b] == '':
                self.lista.pop(b) 
                c=c-1
            b=b+1
        
        #print(self.lista)

        cadena=""
        fila=""
        colum=""
        nombre=""
        
        b=0
       
        while b < len(self.lista): 

            if self.lista[b]=="nombre":
                nombre=self.lista[b+1]
            if self.lista[b]=="filas":
                fila=self.lista[b+1]
            if self.lista[b]=="columnas":
                colum=self.lista[b+1]
                
            if self.lista[b]=="imagen":
                i = b
                while self.lista[i]!="/imagen":
                    i=i+1
                    cadena=cadena+self.lista[i]
                    
                #print(cadena)
                var=guardar.guardar_Matriz()
                var.guardado(int(fila),int(colum),nombre,cadena)
                cadena=""
                    
            b=b+1
        

    