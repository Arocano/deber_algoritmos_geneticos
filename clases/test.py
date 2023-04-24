from algoritmo_genetico import Algortimo_Genetico

alg= Algortimo_Genetico()

#p1,aux= alg.cruce()
estado_objetivo=[[0,1,2],[3,4,5],[6,7,8]]
p,s= alg.algoritmo_genetico(estado_objetivo)

print(p.cromosomas)
for x in s:
    print(x.cromosomas)



