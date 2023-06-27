#se define el metodo que sera el decorador

def verificar_login(funcion):
    user=str(input("Ingresa un usuario: "))
    password=str(input("ingrese la contraseña: "))
    #hasheo
    hash_value=hash(password)
    print(hash_value)
    
    #se declara una funcion retornda por el decorador
    
    def nueva_funcion():
     if user=='admin' and password=='123':
        funcion() #esta func es la que nos dice si pudimos ingresar
     else:
        print("Usuario o contraseña incorrecta, intente de nuevo por favor")
    return nueva_funcion

@verificar_login
def mostrar_menzaje():
    print("bienvenido a muebleria brandonAnt")
#llamado al metodo decorado
mostrar_menzaje()