#estructura basica de un decordar 
def decorador(funcion):
    def funcion_decorada():
        print("Antes de ejecutar la funcion")
        funcion()
        print("despues de ejecutar la funcion")
    return funcion_decorada

# UN DECORADOR: es una funcion que imprime al momento de ser llamada va y abre otra funcion que hace lo que hace la original y puedes agregar mas cosas
@decorador
def mi_funcion():
    print("hola mundo")
    
mi_funcion()
