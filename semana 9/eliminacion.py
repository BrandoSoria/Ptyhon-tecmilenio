# eliminar archivo .txt

import os #saber si existe un archvo con la ayuda del so

if os.path.exists("semana 9/archivo.txt"):
    os.remove("semana 9/archivo.txt")
    print("el archivo se ha eliminado")
else:
    print("archivo no encontrado")