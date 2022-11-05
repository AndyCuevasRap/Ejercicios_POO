class Datos:
  
    def __init__(self):
        self.N1=int(input("Ingrese su primer número: "))
        self.N2=int(input("Ingrese su segundo número: "))
 
    def mostrar(self):
        print("Número 1: ",self.N1)
        print("Número 2: ",self.N2)
 

class Calculadora(Datos):
 
    def Suma(self):
      self.suma = self.N1 + self.N2
      print("Suma: ",self.suma)

    def Resta(self):
      self.resta = self.N1 - self.N2
      print("Resta: ",self.resta)

    def Multiplicación(self):
      self.multiplicación = self.N1 * self.N2
      print("Multiplicación: ",self.multiplicación)

    def División(self):
      self.división = self.N1 / self.N2
      print("División: ",self.división)
          
Datos1=Datos()
Datos1.mostrar()
Calculadora1=Calculadora()
Calculadora1.Suma()
Calculadora1.Resta()
Calculadora1.Multiplicación()
Calculadora1.División()