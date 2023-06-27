# programa para cafeteria
#30-05-2023

class Menu: # clase con el menu
    
    #atributos
    bebidas={
        "espresso":{
            "nombre": "Espresso original",
            "costo": 10.50,
            "ingredientes": {
                "agua": 50,
                "cafe": 20
            }
        },
        "latte": {
            "nombre": "Latte",
            "costo": 12.80,
            "ingredientes": {
                "agua": 100,
                "leche": 50,
                "cafe": 16
            }
        },
        
         "capuchino": {
            "nombre": "Capuchino",
            "costo": 15.00,
            "ingredientes": {
                "agua": 100,
                "leche": 100,
                "café": 18
            }
        },
        "americano": {
            "nombre": "Americano",
            "costo": 8.75,
            "ingredientes": {
                "agua": 120,
                "café": 24
            }
        }
    
        
        
     }
    
    @staticmethod
    
    #es un metodo que pertenece a esta clase, no requiere intancias para su uso, tampoco requiere self, sirve para clarificar el uso de las clases para users
    
    def obtener_menu(): #mostrar el menu
        print("MENU DE BEBIDAS")
        
        for bebida, detalles in Menu.bebidas.items():
            print(f"{bebida.capitalize()}: {detalles['nombre']} - Costo: ${detalles['costo']:.2f}")
            #el 2f es un formato con dos decimales y con dos digitos
        
        
        
    @staticmethod
  
    def buscar_bebida(tipo_bebida): #muestra los detalles de la bebida seleccionada
        bebida = Menu.bebidas.get(tipo_bebida)
        if bebida:
            print(f"\nBebida: {bebida['nombre']}")
            print("Ingredientes:")
            for ingrediente, cantidad in bebida["ingredientes"].items():
                print(f"{ingrediente.capitalize()}: {cantidad}")
            print(f"Costo: ${bebida['costo']:.2f}")
        else:
            print("Bebida no encontrada en el menú.")
            #capitalize es para poner la letra inicial de una palabra a mayudculas
    
    
class MaquinaCafetera: #ejecuta el cobro y regresa el cambio
    def __init__(self):
        self.menu = Menu()
        self.total_insertado = 0.0
    
    def pago(self,costo):
        self.total_insertado = 0.0
        while self.total_insertado < costo:
            moneda = float(input("Inserte moneda (10, 5, o 1): "))
            if moneda not in [10, 5, 1]:
                print("Moneda no válida. Intente de nuevo.")
            else:
                self.total_insertado += moneda

        if self.total_insertado >= costo:
            print("Pago aceptado.")
            return True
        else:
            print("Pago insuficiente.")
            return False
        
          
    def devuelvecambio(self,costo):
        cambio = self.total_insertado - costo
        if cambio > 0:
            print(f"Devolviendo cambio: ${cambio:.2f}")
            return cambio
        else:
            print("No requiere cambio")
            return 0.0
      
# menu principal
sigue=True
while sigue:
    
     maquina= MaquinaCafetera()
     maquina.menu.obtener_menu()
     tipo_bebida =input("Selecciona el tipo de cafe que desea")
     maquina.menu.buscar_bebida(tipo_bebida.lower())
     costo = maquina.menu.bebidas.get(tipo_bebida.lower(), {}).get("costo", 0)
     if costo > 0:
        if maquina.pago(costo):
            print("Sirviendo café.")
            maquina.devuelvecambio(costo)
        else:
            print("Transacción cancelada.")
            
     respuesta = input("\n¿Deseas pedir algo más? (s/n)\n")
     if respuesta.lower() != 's':
        sigue = False
        print("Gracias por tu compra")
        #break
        


    