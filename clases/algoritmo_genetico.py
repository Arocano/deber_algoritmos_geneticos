from clases.ruleta import Ruleta
import random
from clases.generador_poblacion import Generar_Poblacion
from clases.individuos import Individuo
import copy
class Algortimo_Genetico:

    def __init__(self):
        self.crossover=0
        self.hijomutante=0
        self.poblacion=[]
        self.padres=[]
        self.reboot=[[1,0,2],[3,4,5],[6,7,8]]
        self.unloop=[[0,1,2],[3,4,5],[6,7,8]]
        self.loop5=[[1,2,0],[3,4,5],[6,7,8]]

    #Se obtiene los padres de la poblacion en base a la ruleta de probabilidades de los padres
    def obtenerRuleta(self):
        #Instancia de la ruleta
        rul= Ruleta()
        #Instancia de la poblacion 
        gen=Generar_Poblacion()
        #Si la poblacion esta vacia se genera una poblacion inicial randomica
        if len(self.poblacion) == 0:
            gen.generar_poblacion()
            gen.obtener_Probabilidad()
            self.poblacion=copy.deepcopy(gen.poblacion)
        gen.poblacion=copy.deepcopy(self.poblacion)
        gen.obtener_Probabilidad()
        self.poblacion=copy.deepcopy(gen.poblacion)
        #Se genera un array de 100 posiciones
        arr= rul.generarArray()
        #Se colocan los individuos en el array de acuerdo a su probabilidad
        for individuo in self.poblacion:
            arr=rul.colocarProbabilidades(individuo,arr)
        arr=rul.rellenarCeros(arr)
        return arr
    #Se obtienen los padres de la poblacion en base a la ruleta de probabilidades de los padres
    def obtenerPadres(self):
        rul= Algortimo_Genetico.obtenerRuleta(self)
        #Se obtienen dos padres randomicos
        padre1= rul[random.randint(0,99)]
        padre2= rul[random.randint(0,99)]
        #Si los padres son iguales se vuelve a obtener un padre2
        while padre1.cromosomas == padre2.cromosomas:
            padre2= rul[random.randint(0,99)]
            self.padres=[padre1,padre2]
             
        self.padres=[padre1,padre2]
        return padre1,padre2
    
    def cruce(self):
        #Se obtienen los padres
        p1,p2= self.obtenerPadres()
        #Se transforma los padres en un array de 1 dimension
        p1=[element for row in p1.cromosomas for element in row]
        p2=[element for row in p2.cromosomas for element in row]
        #Se cruzan los padres
        p1_partido1= p1[:self.crossover]
        p1_partido2= p1[self.crossover:]
        p2_partido1= p2[:self.crossover]
        p2_partido2= p2[self.crossover:]
        hijo1= p1_partido1+p2_partido2
        hijo2= p2_partido1+p1_partido2
        #Se transforman los arrays en matrices
        hijo1=[hijo1[i:i+3] for i in range(0, len(hijo1), 3)]
        hijo2=[hijo2[i:i+3] for i in range(0, len(hijo2), 3)]
        #Se arreglan los hijos para no repetir numeros
        hijo1= self.arreglarHijos(hijo1)
        hijo2= self.arreglarHijos(hijo2)
        return hijo1,hijo2
    
    def arreglarHijos(self,hijo):
        #Se crea un set para guardar los numeros que ya estan en el hijo
        numeros_usados = set()
        
        #Se comprueba que el hijo sea 3x3
        while len(hijo) < 3:
            hijo.append([0] * len(hijo[0]))
        for row in hijo:
            while len(row) < 3:
                row.append(0)
       #Se recorre el hijo para verificar que no se repitan los numeros
        for i in range(len(hijo)):
            for j in range(len(hijo)):
                # comprobar si el número esta repetido
                if hijo[i][j] in numeros_usados:
                    # encontrar un el numero que no esta en los cromosomas
                    nuevo_numero = None
                    while nuevo_numero is None or nuevo_numero in numeros_usados:
                        nuevo_numero = random.choice(range(0,9))
                    # reemplazar el numero repetido por el nuevo numero
                    hijo[i][j] = nuevo_numero
                # añadir el numero a la lista de numeros usados
                numeros_usados.add(hijo[i][j])
        return hijo
    
    #Algoritmo para mutar un hijo
    def mutacion(self):
        #Obtiene la posicion del hijo que se debe mutar
        self.hijomutante= random.randint(0,1)
        #Obitiene los hijos del cruce que seran evaluados para su mutación 
        hijos= self.cruce()
        #Se crea una lista con los hijos que acabamos de obtener
        hijos=[hijos[0],hijos[1]]
        #Se obtiene la ruleta con la probabilidad de que exita una mutación y se obtiene la probabilidad
        mutar= Ruleta.ruletaMutacion(self)
        mutar= mutar[random.randint(0,99)]
        #Si la probabilidad es diferente a 0 se muta el hijo en la posicion que se obtuvo al inicio
        #caso contrario se devuelven los hijos sin mutar
        if mutar !=0:
            #Se obtine el hijo que se debe mutar
            hijo= hijos[self.hijomutante]
            #Se obtiene las posibles direcciones en las cuales se puede mutar al cromosoma
            direcciones=self.direccionesPosibles(hijo)
            #Se obtiene una direccion aleatoria de las posibles
            direccion= random.choice(direcciones)
            #Se muta el hijo en la direccion que se obtuvo y se devulve la lista actualizada
            hijo=self.mutarCromosoma(hijo,direccion)
            hijos[self.hijomutante]=hijo
            return hijos
        return hijos

    
    def mutarCromosoma(self,hijo,direccion):
        if direccion == 'Arriba':
            matriz_nueva = self.moverArriba(hijo)
            hijo =   matriz_nueva

        elif direccion == 'Abajo':
            matriz_nueva = self.moverAbajo(hijo)
            hijo = matriz_nueva
           
        elif direccion == 'Izquierda':
            matriz_nueva = self.moverIzquierda(hijo)
            hijo = matriz_nueva

        elif direccion == 'Derecha':
            matriz_nueva = self.moverDerecha(hijo)
            hijo = matriz_nueva
        return hijo
    
    def moverArriba(self,matriz):
        posicion = self.encontrarCero(matriz)
        posicion_nueva = [posicion[0]-1, posicion[1]]
        numero_antiguo = matriz[posicion_nueva[0]][posicion_nueva[1]]
        matriz_nueva = copy.deepcopy(matriz)
        matriz_nueva[posicion_nueva[0]][posicion_nueva[1]] = 0
        matriz_nueva[posicion[0]][posicion[1]] = numero_antiguo
        return matriz_nueva

    def moverAbajo(self,matriz):
        posicion = self.encontrarCero(matriz)
        posicion_nueva = [posicion[0]+1, posicion[1]]
        numero_antiguo = matriz[posicion_nueva[0]][posicion_nueva[1]]
        matriz_nueva = copy.deepcopy(matriz)
        matriz_nueva[posicion_nueva[0]][posicion_nueva[1]] = 0
        matriz_nueva[posicion[0]][posicion[1]] = numero_antiguo
        return matriz_nueva

    def moverIzquierda(self,matriz):
        posicion = self.encontrarCero(matriz)
        posicion_nueva = [posicion[0], posicion[1]-1]
        numero_antiguo = matriz[posicion_nueva[0]][posicion_nueva[1]]
        matriz_nueva = copy.deepcopy(matriz)
        matriz_nueva[posicion_nueva[0]][posicion_nueva[1]] = 0
        matriz_nueva[posicion[0]][posicion[1]] = numero_antiguo
        return matriz_nueva

    def moverDerecha(self,matriz):
        posicion = self.encontrarCero(matriz)
        posicion_nueva = [posicion[0], posicion[1]+1]
        numero_antiguo = matriz[posicion_nueva[0]][posicion_nueva[1]]
        matriz_nueva = copy.deepcopy(matriz)
        matriz_nueva[posicion_nueva[0]][posicion_nueva[1]] = 0
        matriz_nueva[posicion[0]][posicion[1]] = numero_antiguo
        return matriz_nueva
    
    def encontrarCero(self,matriz):
        cero = []
        for i in range(3):
            for j in range(3):
                if matriz[i][j] == 0:
                    cero.append(i)
                    cero.append(j)
        return cero
    
    def direccionesPosibles(self,matriz):
        posicion = self.encontrarCero(matriz)
        fila_vacia = posicion[0]
        columna_vacia = posicion[1]
        # Buscar las direcciones posibles
        direcciones = []
        if fila_vacia > 0:  # Arriba
            direcciones.append('Arriba')
        if fila_vacia < len(matriz)-1:  # Abajo
            direcciones.append('Abajo')
        if columna_vacia > 0:  # Izquiera
            direcciones.append('Izquierda')
        if columna_vacia < len(matriz[0])-1:  # Derecha
            direcciones.append('Derecha')
        return direcciones
    
    def algoritmo_genetico(self,estado_meta):
        aux=False
        self.crossover= random.randint(1,8)
        generaciones= self.mutacion()
        hijo1= Individuo(generaciones[0])
        hijo2= Individuo(generaciones[1])
        self.quitarPadres3()
        self.poblacion.append(hijo1)
        self.poblacion.append(hijo2)
        while True:
            for individuo in self.poblacion:
                if individuo.cromosomas==estado_meta:
                    return individuo,self.poblacion
            for individuo in self.poblacion:
                individuo.funcion_heuristica=0  
                individuo.probabilidad=0
            generaciones= self.mutacion()
            hijo1= Individuo(generaciones[0])
            hijo2= Individuo(generaciones[1])
            self.quitarRepetidos()
            self.poblacion.append(hijo1)
            self.poblacion.append(hijo2)
 
                
    def quitarRepetidos(self):
        puzzle=Generar_Poblacion()
        aux=[]
        for individuo in self.poblacion:
            aux.append(individuo.cromosomas)
        for individuo in self.poblacion:
            s=aux.count(individuo.cromosomas)
            if s > 1 and s<4:
                if self.poblacion[0].funcion_heuristica==4:
                    self.poblacion.append(Individuo(self.reboot))
                if  self.poblacion[0].funcion_heuristica==3:
                    self.poblacion.append(Individuo(self.unloop))   
                if  self.poblacion[0].funcion_heuristica==5:
                    self.poblacion.append(Individuo(self.loop5)) 
                if  len(self.poblacion)<=5:
                    self.quitarPadres4()
                    self.quitarPadres4()
                    self.poblacion.append(Individuo(puzzle.generar_8puzzle()))
                    self.poblacion.append(Individuo(puzzle.generar_8puzzle()))
                    return True
                self.quitarPadres3()
                self.quitarPadres3()
                
                return True
            elif s>=4 and s<7:
                self.poblacion.remove(individuo)
                self.quitarPadres2()
                return True
            elif s>=7 and s<15:
                self.poblacion.remove(individuo)
            elif s>=15:
                self.poblacion.remove(individuo)
                self.quitarPadres4()
                return True

    
    def quitarPadres(self):
        if self.padres[0]  in self.poblacion:
            self.poblacion.remove(self.padres[0])
        if self.padres[1]  in self.poblacion:
            self.poblacion.remove(self.padres[1])
        return self.poblacion
    
    def quitarPadres2(self):
        max_indices = sorted(range(len(self.poblacion)), key=lambda i: -self.poblacion[i].funcion_heuristica)[:2]
        for index in sorted(max_indices, reverse=True):
            del self.poblacion[index]

    def quitarPadres3(self):
        lowest_fitness_index = 0
        for i in range(1, len(self.poblacion)):
            if self.poblacion[i].funcion_heuristica > self.poblacion[lowest_fitness_index].funcion_heuristica:
                lowest_fitness_index = i
        del self.poblacion[lowest_fitness_index]

    def quitarPadres4(self):
        lowest_fitness_index = 0
        for i in range(1, len(self.poblacion)):
            if self.poblacion[i].funcion_heuristica < self.poblacion[lowest_fitness_index].funcion_heuristica:
                lowest_fitness_index = i
        del self.poblacion[lowest_fitness_index]
    
                

    




            
    

