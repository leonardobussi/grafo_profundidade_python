
grafo = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0', '5', '6']),
         '3': set(['1']),
         '4': set(['1']),
         '5': set(['2']),
         '6': set(['2'])
         }
 
def dfs(grafo, comeco):
  visitado, rota = set(), [comeco]
  while rota:
      vertice = rota.pop()
      if vertice not in visitado:
          visitado.add(vertice)
          rota.extend(grafo[vertice] - visitado)
  return visitado

roda = dfs(grafo, '0') 
print(roda)

