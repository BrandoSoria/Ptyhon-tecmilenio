
# BRANDON ANTONIO SORIA GOMEZ 02-05-2023

#ejercicio de estructuras de datos en python

#crear una lista
lista=["lunes", "Martes", "Miercoles"]
print(lista)
lista.append("Jueves")
lista.extend(["Viernes","sabado"]) #son varios elemento otraves usar []
lista.remove("Martes")
lista.pop(3)
lista.append("lunes")
print(lista)
numeros=[1,3,4,5,6]
numeros.remove(6)
numeros.pop(0)
print(numeros)

#crear tuplas

deportes=("futbol","baseball","tenis")
type(deportes)
len(deportes)

#diccionario
#tienen dos elementos llave y valor
dicNumeros={1:"texto",2:23.2,3:True,4:12}
type(dicNumeros)

# modificar elementos
dicNumeros[1]="brandon"
# si no existe un elemento se agrega
dicNumeros[5]="Alberto"
print(dicNumeros)

#eliminar elemento
del dicNumeros[2]
print(dicNumeros)

#set o conjuntos (no se usa mucho)
conjunto={1,2,3,4,5,6,7}
type(conjunto)
conjunto.add(8)
conjunto.add(7)
conjunto

conjunto2={"soria","alberto","marco"}
type(conjunto2)
conjunto2.add("Texto")
conjunto2

conjuntocongelado=frozenset([4,"texto",5,6])
type(conjuntocongelado)
conjuntocongelado.add("soria")
conjuntocongelado
