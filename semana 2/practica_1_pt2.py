# BRANDON ANTONIO SORIA GOMEZ 02-05-2023
# PROGRAMA PARA CALULAR EL IMC DE UNA PERSONA

#entradas 
peso =float(input("escibe tu peso: "))
estatura =float(input("escibe tu estatura: "))

#Proceso
imc= round((peso/estatura**2),2)
print("tu estado de imc es de: ",imc)

#** es el exponente

#estructura condicional
if imc >= 30:
  print("estas en obesidad")
  
elif  imc >= 25:
    print("estas en sobrepeso")
    
elif  imc >= 18.5:
    print("estas en peso normal")
    
else: 
  print("tu nivel de peso es bajo")


