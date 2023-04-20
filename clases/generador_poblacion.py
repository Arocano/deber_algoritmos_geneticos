import random
from individuos import Individuo
class Generar_Poblacion:
    estado_objetivo=[[0,1,2],[3,4,5],[6,7,8]]
    totalHeuristica=0
    totalPosibles=0
    poblacion=[]
    def generar_8puzzle(self):
        numbers = list(range(1, 9)) + [0] 
        random.shuffle(numbers) 
        puzzle = [numbers[:3], numbers[3:6], numbers[6:]] 
        return puzzle
    
    def generar_poblacion(self):
        for i in range(0,4):
            individuo=Individuo(self.generar_8puzzle())
            self.poblacion.append(individuo)
    
    def obtener_Probabilidad(self):
        for individuo in self.poblacion:
            individuo.calcularHerustica(self.estado_objetivo)
            self.totalHeuristica+=individuo.funcion_heuristica
        for individuo in self.poblacion:
            self.totalPosibles+=individuo.obtenerPosibles(self.totalHeuristica)
        for individuo in self.poblacion:
            individuo.obtenerProbabilidad(self.totalHeuristica,self.totalPosibles)
        return self.poblacion


