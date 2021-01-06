class Coche():

    #La clase Coche tiene 4 propiedades, largo, ancho, ruedas y enmarcha

    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    #La clase Coche tiene 2 comportamientos, arrancar y estado (2 metodos)

    def arrancar(self, arrancamos):
        self.enmarcha = arrancamos

        if self.enmarcha:
            return "El coche esta en marcha"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene:",self.ruedas,"ruedas, un ancho de",self.anchoChasis,
              "y un largo de",self.largoChasis)

#miCoche es una instancia de la clase Coche (Un objeto)

miCoche = Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("-----------------------------A continuacion creamos nuestro segundo objeto------------------------------")

miCoche2 = Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()
