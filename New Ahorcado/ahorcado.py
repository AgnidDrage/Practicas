from repository import GuardarPartida
from servicesPartidas import ServicesPartidas


class Ahorcado():
    def menu(self):
        print("Seleccione 1 para un jugador, 2 para dos jugadores o cualquier otra tecla para salir")
        return int(input("Elija una opcion: "))

    def un_jugador(self):
        try:
            services = ServicesPartidas
            nombre = input("Ingrese su nombre: ")
            dificultad = int(input("Ingrese la dificultad: "))
            partidaUno = services.iniciar_partida(nombre, dificultad)
            res == "Continua"
            while res == "Continua":
                letra = input("Ingrese una letra: ")
                if letra == "Salir":
                    return True
                res = services.intentar_letra(partidaUno, letra.upper())
                print(partidaUno.palabra_aciertos)
            if res == "Gano":
                print("Ganaste", nombre)