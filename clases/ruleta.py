import numpy as np
import random 
from individuos import Individuo
class Ruleta:
    arr =[]
    def generarArray(self):
        for i in range(100):
            obj = Individuo([])
            Ruleta.arr.append(obj)

    def colocarProbabilidades(self,individuo):
        self.generarArray()
        length = round(individuo.probabilidad)
        index = 0
        while index < length:
            posicion = random.randint(0,99)
            if Ruleta.arr[posicion].probabilidad == 0:
                Ruleta.arr[posicion] = individuo
                index += 1
    
    def rellenarCeros(self):
        maximo= max(Ruleta.arr , key=lambda x: x.probabilidad)
        for i in range(0,99):
            if Ruleta.arr[i] == 0:
                Ruleta.arr[i] = maximo

