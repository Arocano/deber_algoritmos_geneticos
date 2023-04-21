from generador_poblacion import Generar_Poblacion
from ruleta import Ruleta
rul= Ruleta()
gen=Generar_Poblacion()
gen.generar_poblacion()
print(gen.obtener_Probabilidad())

for individuo in gen.poblacion:
    rul.colocarProbabilidades(individuo)
rul.rellenarCeros()

print(rul.arr)

