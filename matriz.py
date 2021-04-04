class nodo_dato:

    def __init__(self, x, y, dato):
        self.dato=dato
        self.x=x
        self.y=y
        self.anterior=None
        self.siguiente=None
        self.arriba=None
        self.abajo=None

class matriz_dato:
    def __init__(self, x, y, dato):
        
        self.inicio = nodo_dato(x, y, dato)

    def crear(self, fila, columna):
        i=0
        j=0
        aux_x=self.inicio
        aux_y=self.inicio

        while i <= fila:            
            nuevo = nodo_dato(i, 0, 0)
            aux_x.siguiente=nuevo
            nuevo.anterior=aux_x
            aux_x=nuevo
            i=i+1

        while j <= columna:           
            nuevo = nodo_dato(0, j, 0)
            aux_y.abajo=nuevo
            nuevo.arriba=aux_y
            aux_y=nuevo
            j=j+1

        #relleno
        i=1
        j=1
        aux_x=self.inicio.siguiente
        aux_y=self.inicio.abajo
        temp=self.inicio.abajo

        n=1
        while i<= fila:
            while j<= columna+1:
                nuevo = nodo_dato(i, j, str(n)) 
                n=n+1          
                aux_y.siguiente=nuevo
                nuevo.anterior=aux_y

                aux_x.abajo=nuevo
                nuevo.arriba=aux_x

                aux_y=nuevo
                aux_x=aux_x.siguiente

                j=j+1
            #while fin j
            temp=temp.abajo
            aux_y=temp
            aux_x=self.verificar_y(self.inicio.siguiente)
            i=i+1
            j=1


    def verificar_y(self, nodo):
        regreso=nodo        
        while regreso.abajo != None:
            regreso=regreso.abajo        
        return regreso

    def verificar_x(self, nodo):
        regreso=nodo
        while regreso.siguiente != None:
            regreso=regreso.siguiente
        return regreso

    def recorrer(self):
        temporal=self.inicio.abajo
        aux=self.inicio.siguiente

        while temporal.abajo != None:
            while aux.siguiente != None:
                print(str(aux.abajo.x)+'/'+str(aux.abajo.y)+'/'+aux.abajo.dato)

                aux=aux.siguiente
            aux=temporal.siguiente
            temporal=temporal.abajo


    def reemplazo(self, j, i, dato):       
        temporal=self.inicio.abajo
        aux=self.inicio.siguiente

        while temporal.abajo != None:
            while aux.siguiente != None:

                if str(i)==str(aux.abajo.x) and str(j)==str(aux.abajo.y):
                    if dato == "-":
                        aux.abajo.dato=" "
                    
                    if dato == "*":
                        aux.abajo.dato="*"

                    #print(str(aux.abajo.x)+'/'+str(aux.abajo.y)+'/'+aux.abajo.dato)

                aux=aux.siguiente
            aux=temporal.siguiente
            temporal=temporal.abajo
        
    def recorido_normal(self):
        temporal=self.inicio.abajo
        aux=self.inicio.siguiente
        cadena=""

        while temporal.abajo != None:
            while aux.siguiente != None:
                #print(aux.abajo.x)
                #print(aux.abajo.y)
                #print(aux.abajo.dato)
                cadena=cadena+aux.abajo.dato
                #print(str(aux.abajo.x)+'/'+str(aux.abajo.y)+'/'+aux.abajo.dato)

                aux=aux.siguiente
            aux=temporal.siguiente
            temporal=temporal.abajo
            cadena=cadena+'\n'
        print(cadena)
    
    #Rotación horizontal de una imagen: lectura de abajo hacia arriba normal
    def rotacion_Horizontal (self):
        cadena=""
        temporal=self.inicio.abajo

        while temporal.abajo != None:
            temporal=temporal.abajo
            #temporal esta hasta abajo
        
        bandera=temporal.arriba
        aux=bandera.siguiente

        while temporal.arriba != self.inicio:
            while aux.siguiente != None:
                #print(aux.abajo.x)
                #print(aux.abajo.y)
                #print(aux.abajo.dato)
                cadena=cadena+str(aux.dato)

                aux=aux.siguiente
            cadena=cadena+'\n'
            temporal=temporal.arriba
            bandera=temporal.arriba
            aux=bandera.siguiente
        
        print(cadena)

    #Rotación vertical de una imagen: lectura de derecha a izquierda

    def rotacion_Vertical (self):
        cadena=""
        temporal=self.inicio.abajo
        aux=self.inicio.siguiente
        bandera=self.inicio.siguiente

        while temporal.abajo != None:

            while aux.siguiente != None:               
                aux=aux.siguiente

            while aux.anterior != None:
                #print(aux.abajo.x)
                #print(aux.abajo.y)
                #print(aux.abajo.dato)
                
                cadena=cadena+str(aux.abajo.dato)
                aux=aux.anterior
                
                
            cadena=cadena+'\n'
            aux=temporal.siguiente
            temporal=temporal.abajo

        print(cadena)

#Transpuesta de una imagen: primero recorrer desde la ultima columna hasta la primera normal, despues de abajo hacia arriba normal











