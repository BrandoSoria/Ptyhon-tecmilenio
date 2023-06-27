#mandar a llamar funciones para convertir archivo json a csv
from reporteCSV import lectorJSON

nombre_archivo = "semana_9_pt2/generador_de_reportes/posts.json"
coleccion = 'posts'
archivo_salida = 'semana_9_pt2/generador_de_reportes/reporte.csv'
reporteador = lectorJSON()
reporteador.convertirJSONaCSV(nombre_archivo,coleccion,archivo_salida)