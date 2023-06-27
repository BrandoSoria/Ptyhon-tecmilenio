# anulacion de metodo (method overriding)

class Empleado():
    def CalcularSueldo(self,DiasPagados,PagoPorDia):
        return DiasPagados * PagoPorDia
    
class EmpleadoTemporal(Empleado):
    def CalcularSueldo(self, DiasPagados, PagoPorDia, Bono):
        return DiasPagados * PagoPorDia+Bono

base=Empleado()
ventas=EmpleadoTemporal()


dias=int (input("dias laborados: "))
sueldodia=float (input("sueldo por dia:"))
bono=float (input("bono"))

print("\n el pago al empleado base es de:{}".format(base.CalcularSueldo(dias,sueldodia)))

print("\n el pago al empleado de ventas es de:{}".format(ventas.CalcularSueldo(dias,sueldodia,bono)))

