# E3.1 · Deja este archivo con CERO avisos en PROBLEMS sin cambiar lo que
# hace el programa. Pista: también te pedirá un docstring para el módulo.
import random
import sys
def CalcularPrecioFinal(precio,descuento ,iva):
    PrecioConDescuento=precio-precio*descuento/100
    total =PrecioConDescuento*(1+iva/100)
    return round(total,2)
def tirar_dado( ):
  return random.randint(1,6)
def saludar(nombre):
      mensaje="Hola, "+nombre
      contador = 0
      return mensaje
print(CalcularPrecioFinal(100,10,21))
print( "Dado:",tirar_dado())
print(saludar( "DAM"))
