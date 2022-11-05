class Persona:

    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        self.edad=int(input("Ingrese la edad: "))
 
    def mostrar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
 

class Empleado(Persona):

    def __init__(self):
        super().__init__()
        self.sueldo=float(input("Ingrese el sueldo: "))
 
    def mostrar(self):
        super().mostrar()
        print("Sueldo: ",self.sueldo)
 
    def pagar_impuestos(self):

        self.descuento = self.sueldo*0.035
        self.total = self.sueldo - self.descuento

      
        if self.sueldo >= 3600000: #Tres millones seicientos
            print("El descuento que se hizo fue de ",self.descuento, )  
            print("El neto sera de ",self.total)

        elif self.sueldo >= 2300000: #Dos millones trecientos
            print("El empleado debe pagar solo retefuente")

        else:
            print("El empleado no paga impuestos.")

          
persona1=Persona()
persona1.mostrar()
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()