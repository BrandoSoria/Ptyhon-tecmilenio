# crear contenido en un archivo nvo

archivo=open("semana 9/nuevo_archivo.txt","w")
contenido="este contenido es nuevo para un archivo"
archivo.write(contenido)
print(contenido)
archivo.close()