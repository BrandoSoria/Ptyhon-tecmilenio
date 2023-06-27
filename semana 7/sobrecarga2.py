# conversion de tipos de datos

class Convertidor():
    def ConvertirValor(self,valor):
        if type(valor)==int:
            return str(valor)
        elif type(valor)==str:
            return int(valor)
        
miObjeto= Convertidor()
valorPrimero=miObjeto.ConvertirValor(20)
valorSegundo= miObjeto.ConvertirValor("32")

print("el valor del primero objeto es {}".format(type (valorPrimero)))

print("el valor del primero objeto es {}".format(type (valorSegundo)))
        
        
        

