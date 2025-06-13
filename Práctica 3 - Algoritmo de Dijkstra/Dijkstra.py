import heapq  # Módulo para trabajar con colas de prioridad (min-heaps)

# Definición del grafo como un diccionario de adyacencia
# Cada nodo tiene como valor un diccionario con sus vecinos y el peso de las aristas
grafo = {
    'A': {'B': 4, 'C': 2},
    'B': {'A': 4, 'C': 1, 'D': 5},
    'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
    'D': {'B': 5, 'C': 8, 'E': 2, 'Z': 6},
    'E': {'C': 10, 'D': 2, 'Z': 3},
    'Z': {'D': 6, 'E': 3}
}

# Implementación del algoritmo de Dijkstra para encontrar el camino más corto desde un nodo origen
def dijkstra(grafo, inicio):
    # Inicializa todas las distancias como infinitas, excepto el nodo de inicio que tiene distancia 0
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0

    # Diccionario para registrar el camino más corto a cada nodo
    camino = {nodo: [] for nodo in grafo}
    camino[inicio] = [inicio]
    
    # Cola de prioridad para seleccionar el siguiente nodo con menor distancia conocida
    cola_prioridad = [(0, inicio)]

    # Conjunto para llevar el control de los nodos ya visitados
    visitados = set()
    
    print(f"Iniciando desde el nodo: {inicio}\n")
    
    # Mientras queden nodos por visitar en la cola de prioridad
    while cola_prioridad:
        # Extraer el nodo con menor distancia acumulada
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si ya fue visitado, se omite
        if nodo_actual in visitados:
            continue
        
        print(f"Visitando nodo: {nodo_actual} con distancia acumulada: {distancia_actual}")
        visitados.add(nodo_actual)
        
        # Explora los vecinos del nodo actual
        for vecino, peso in grafo[nodo_actual].items():
            nueva_distancia = distancia_actual + peso
            # Si se encuentra un camino más corto al vecino, se actualiza
            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                camino[vecino] = camino[nodo_actual] + [vecino]
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
                print(f"  Actualizando nodo: {vecino} → nueva distancia: {nueva_distancia}, camino: {camino[vecino]}")
        print()
    
    # Devuelve el diccionario de distancias y caminos
    return distancias, camino

# Ejecutar el algoritmo desde el nodo 'A'
distancias, caminos = dijkstra(grafo, 'A')

# Mostrar los resultados finales: distancia más corta y camino seguido hasta cada nodo
print("Resultados finales:\n")
for nodo in grafo:
    print(f"Distancia más corta hasta {nodo}: {distancias[nodo]} → Camino: {' -> '.join(caminos[nodo])}")
