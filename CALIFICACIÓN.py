class Alumno:
    def __init__(self):
        self.Nombre=input("Hola, ¿Cómo te llamas? ")
 
    def mostrar(self):
        print("Hola ",self.Nombre)
 
class Nota():

    def __init__(self):
      super().__init__()
      self.Nota=float(input("¿Cuál es tu nota? "))

    def mostrar(self):
      print("Nota: ",self.Nota)
  
    def Aprobación(self):
      
        if self.Nota >=3:
            print("Felicidaes, haz aprobado")  
        else:
            print("Lamentablemente, haz sido reprobado")

          
Alumno1=Alumno()
Alumno1.mostrar()
Nota1=Nota()
Nota1.mostrar()
Nota1.Aprobación()