import heapq

# Grafo como diccionario de adyacencia
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 3},
    'Z': {'D': 6, 'E': 3}
}

def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    camino = {nodo: [] for nodo in grafo}
    camino[inicio] = [inicio]
    
    cola_prioridad = [(0, inicio)]
    visitados = set()
    
    print(f"Iniciando desde el nodo: {inicio}\n")
    
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        if nodo_actual in visitados:
            continue
        
        print(f"Visitando nodo: {nodo_actual} con distancia acumulada: {distancia_actual}")
        visitados.add(nodo_actual)
        
        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                camino[vecino] = camino[nodo_actual] + [vecino]
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
                print(f"  Actualizando nodo: {vecino} → nueva distancia: {nueva_distancia}, camino: {camino[vecino]}")
        print()
    
    return distancias, camino

# Ejecutar el algoritmo
distancias, caminos = dijkstra(grafo, 'A')

# Mostrar resultados
print("Resultados finales:\n")
for nodo in grafo:
    print(f"Distancia más corta hasta {nodo}: {distancias[nodo]} → Camino: {' -> '.join(caminos[nodo])}")
