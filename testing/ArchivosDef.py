def CrearArchivo(NombreArchivo):
	archivo=open(NombreArchivo, 'w')
	archivo.close()
def InsertarTexto( Texto, NombreArchivo ):
	archivo=open(NombreArchivo, 'a')
	archivo.write(Texto)
	archivo.close

def LeerTexto(NombreArchivo):
	# Abro el Archivo
    archivo=open(NombreArchivo,'r')
    linea=archivo.readline()
    while linea!="":
        print (linea)
        # Notemos que durante la iteracion el puntero permanece abierto
        # En cada iteraccion leo una linea, hasta llegar al final del archivo
        linea=archivo.readline()
    # Cierro el archivo 
    archivo.close()
def LeerTextoALista(NombreArchivo):
	# Abro el Archivo
    archivo=open(NombreArchivo,'r')
    # Lo leo a una lista de texto (cada item contiene una linea del archivo)
    lineas=archivo.readlines()
    # Cierro el archivo seguidamente
    archivo.close()
    # puedo trabajar el contenido del archivo que se encuentra en la lista en memoria.
    for linea in lineas:
        print (linea)
