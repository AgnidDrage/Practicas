from partida import Partida
from repository import GuardarPartida
from repository import Repository
import random


class ServicesPartidas():
    def __init__(self):
        self.repositorio = Repository.repositorioPalabras
        self.guardar = GuardarPartida
        self.random = random
    
    def iniciar_partida(self, nombre_jugador, dificultad, palabra="", tipo_palabra=""):
        if dificultad < 1 or dificultad > 10:
            raise ValueError("La dificultad debe comprender entre 1 y 10")
        randomKey = self.getKey()
        if (len(palabra)==0 or palabra is None and len(tipo_palabra)==0 or tipo_palabra is None):
            palabra = self.repositorio[randomKey]['palabra']
            tipo_palabra = self.repositorio[randomKey]['tipo_palabra']
        intentos = dificultad * len(palabra)
        partidaUno = Partida(palabra, intentos, tipo_palabra, nombre_jugador)
        self.guardar.saves[randomKey] = partidaUno.nombre_jugador
        return partidaUno

    def get_random_palabra(self):
        randomKey = random.choice(list(self.repositorio.keys()))
        return self.repositorio[randomKey]
    
    def getKey(self):
        randomKey = random.choice(list(self.repositorio.keys()))
        return randomKey
    
    def intentar_letra(self, partida, letra):
        partida.intentos = partida.intentos - 1
        if partida.intentos < 0:
            raise ValueError("Te has quedado sin intentos")
        for i in range(len(partida.palabra)):
            if letra == partida.palabra[i]:
                partida.palabra_aciertos[i] = letra
        if None in partida.palabra_aciertos:
            if partida.intentos == 0:
                return 'Perdio'
            else:
                return 'Continua'
        else:
            return 'Gano'