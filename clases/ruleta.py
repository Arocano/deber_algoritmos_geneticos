
import numpy as np
import random 
class Ruleta:
    arr = np.zeros(100)

    def colocarProbabilidades(probabilidad):
        length = round(probabilidad)
        index = 0
        while index < length:
            posicion = random.randint(0,99)
            if Ruleta.arr[posicion] == 0:
                Ruleta.arr[posicion] = probabilidad
                index += 1

