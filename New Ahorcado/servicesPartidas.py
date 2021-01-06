from partida import Partida
from repository import GuardarPartida
from repository import Repository
import random


class ServicesPartidas():
    def __init__(self):
        self.repositorio = Repository.repositorioPalabras
        self.guardar = GuardarPartida
        self.random = random
    
    def iniciar_partida(self, nombre_jugador, dificultad, palabra, tipo_palabra):
        if dificultad < 1 and dificultad > 10:
            raise ValueError("La dificultad debe comprender entre 1 y 10")
        key = ServicesPartidas.getKey
        palabra = self.repositorio[key]['palabra']
        tipo_palabra = self.repositorio[key]['tipo_palabra']


    def get_random_palabra(self):
        randomKey = random.choice(list(self.repositorio.keys()))
        return self.repositorio[randomKey]
    
    def getKey(self):
        randomKey = random.choice(list(self.repositorio.keys()))
        return randomKey