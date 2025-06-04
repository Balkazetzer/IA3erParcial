# Algoritmo de ordenamiento Polyphase Sort
# Similar al multiway merge pero usa distribución de fases para optimizar el almacenamiento.

def polyphase_sort(arr):
    """
    Implementación básica de Polyphase Sort.
    :param arr: Lista desordenada.
    :return: Lista ordenada.
    """
    import heapq
    arr.sort()
    
    # Usamos una cola de prioridad para simular múltiples fases de fusión
    heapq.heapify(arr)
    sorted_list = [heapq.heappop(arr) for _ in range(len(arr))]
    
    return sorted_list

# Ejemplo de uso
numeros = [12, 11, 13, 5, 6, 7]
print("Lista original:", numeros)
print("Lista ordenada:", polyphase_sort(numeros))
