import numpy as np
import random 
from clases.individuos import Individuo
class Ruleta:
    
    def generarArray(self):
        arr=[]
        for i in range(100):
            obj = Individuo([])
            arr.append(obj)
        return arr

    def colocarProbabilidades(self,individuo,arr):
        length = round(individuo.probabilidad)
        index = 0
        while index < length:
            posicion = random.randint(0,99)
            if arr[posicion].probabilidad == 0:
                arr[posicion] = individuo
                index += 1
        return arr
    
    def rellenarCeros(self,arr):
        maximo= max(arr , key=lambda x: x.probabilidad)
        for i in range(0,99):
            if arr[i].probabilidad == 0:
                arr[i] = maximo
        return arr

    def ruletaMutacion(self):
        mutacion = np.zeros(100)
        length = 24
        index = 0
        while index < length:
            posicion = random.randint(0,99)
            if mutacion[posicion] == 0:
                mutacion[posicion] = 24
                index += 1
        return mutacion

