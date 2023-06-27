#brandon soria 
# dia 06-06-2023

class calculadora:
    def sumar(self, *args):
        total=sum(args)
        return total
    
#uso de la calculadora que suma

calc=calculadora()

#suma dos numeros
resultadosdosnumeros= calc.sumar(8,2)
print(resultadosdosnumeros)

#suma tres munemros
resultadostresnumeros = calc.sumar(9,3,5.3)
print(resultadostresnumeros)

resultadoscinconumeros = calc.sumar(9,3,5.3,2,5)
print(resultadoscinconumeros)
