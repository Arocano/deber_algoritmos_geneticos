
import math
class Individuo:
    def __init__(self, cromosomas):
        self.cromosomas=cromosomas
        self.funcion_heuristica=0
        self.probabilidad=0

    def calcularHerustica(self, estado_objetivo):
        for i in range(3):
            for j in range(3):
                if self.cromosomas[i][j] != estado_objetivo[i][j]:
                    self.funcion_heuristica += 1 

    def obtenerPosibles(self, totalHeuristica):
        posibles=totalHeuristica-self.funcion_heuristica
        return posibles
    
    def obtenerProbabilidad(self, totalHeuristica,totalPosibles):
        probabilidad= self.obtenerPosibles(totalHeuristica)/totalPosibles
        self.probabilidad=math.floor((round(probabilidad,3)*100))
    