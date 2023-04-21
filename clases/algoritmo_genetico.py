from ruleta import Ruleta
import random
from generador_poblacion import Generar_Poblacion
import copy
class Algortimo_Genetico:

    def __init__(self):
        self.crossover=0
        self.mutacion=0
        self.poblacion=[]

    def obtenerRuleta(self):
        rul= Ruleta()
        gen=Generar_Poblacion()
        gen.generar_poblacion()
        gen.obtener_Probabilidad()
        self.poblacion=copy.deepcopy(gen.poblacion)
        for individuo in self.poblacion:
            rul.colocarProbabilidades(individuo)
        rul.rellenarCeros()
        return rul
    
    def obtenerPadres(self):
        rul= Algortimo_Genetico.obtenerRuleta(self)
        padre1= rul.arr[random.randint(0,99)]
        padre2= rul.arr[random.randint(0,99)]
        while padre1.cromosomas == padre2.cromosomas:
            padre2= rul.arr[random.randint(0,99)]
            return padre1,padre2
        return padre1,padre2
    
    def tomar_cafe(self):
        p1,p2= self.obtenerPadres()
        self.crossover= random.randint(0,len(p1.cromosomas)-1)
        aux=self.poblacion
        p1_partido1= p1.cromosomas[0:self.crossover]
        return p1_partido1,aux


    
    

