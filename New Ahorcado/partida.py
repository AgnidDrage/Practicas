class Partida():
    def __init__ (self, palabra, intentos, tipo_palabra, nombre_jugador, palabra_aciertos=[None]):
        self.palabra = palabra
        self.intentos = intentos
        self.tipo_palabra = tipo_palabra
        self.nombre_jugador = nombre_jugador
        self.palabra_acierto = palabra_aciertos

    @property
    def palabra (self):
        return self._palabra

    @palabra.setter
    def palabra (self, palabra):
        if palabra is None:
            raise ValueError("La palabra no puede ser vacia.")
        else:
            self._palabra = list(palabra.upper())

    @property
    def intentos (self):
        return self._intentos

    @intentos.setter
    def intentos (self, intentos):
        if intentos < 0:
            raise ValueError("El valor de los intentos no puede ser negativo.")
        else:
            self._intentos = intentos

    @property
    def tipo_palabra(self):
        return self._tipo_palabra

    @tipo_palabra.setter
    def tipo_palabra(self, tipo_palabra):
        if tipo_palabra is None:
            raise ValueError("El tipo de palabra no puede ser vacio.")
        else:
            self._tipo_palabra = tipo_palabra

    @property
    def nombre_jugador(self):
        return self._nombre_jugador

    @nombre_jugador.setter
    def nombre_jugador(self, nombre_jugador):
        if nombre_jugador is None:
            raise ValueError("El nombre del jugador no puede ser vacio.")
        else:
            self._nombre_jugador = nombre_jugador

    @property
    def palabra_aciertos(self):
        return self._palabra_aciertos

    @palabra_aciertos.setter
    def palabra_aciertos(self, palabra_aciertos):
        self._palabra_aciertos = palabra_aciertos * len(self._palabra)
