import numpy as np
import random 
class Ruleta:
    arr = np.zeros(100)

    def colocarProbabilidades(self,individuo):
        length = round(individuo.probabilidad)
        index = 0
        while index < length:
            posicion = random.randint(0,99)
            if Ruleta.arr[posicion] == 0:
                Ruleta.arr[posicion] = individuo
                index += 1
    
    def rellenarCeros(self):
        maximo= max(Ruleta.arr)
        for i in range(0,99):
            if Ruleta.arr[i] == 0:
                Ruleta.arr[i] = maximo

