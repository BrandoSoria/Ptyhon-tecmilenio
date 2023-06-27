# BRANDON ANTONIO SORIA GOMEZ 02-05-2023
# PRIMER PROGRAMA DE CALCULO DE PROPINAS

#entradas

print("BIENVENIDO A LA CALCULADORA DE PROPINAS")
cuenta= float(input("cual es el monto a pagar: "))
porcentaje=int(input("que porcentaje de propina desear: 10,15,20: "))
comensales=int(input("en cuantas personas se dividira la cuenta: "))

#procesos, formulas, calculos
porcentajeDecimal=porcentaje/100
propina=cuenta*porcentajeDecimal
totalCuenta=cuenta+propina
pagoPersona=totalCuenta/comensales
pagoTotal=round(pagoPersona,2)

#el round es para redondear

#salida
print("cada persona pagara: $",pagoTotal,"pesos")
