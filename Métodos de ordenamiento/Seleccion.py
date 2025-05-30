# Algoritmo de ordenamiento por selección (Selection Sort)
# Encuentra el elemento más pequeño en cada iteración y lo coloca en su posición correcta.

def selection_sort(arr):
    """
    Función que implementa el ordenamiento por selección.
    :param arr: Lista de números desordenada.
    :return: Lista ordenada.
    """
    n = len(arr)
    
    for i in range(n):
        min_idx = i  # Suponemos que el primer elemento es el menor
        
        # Buscamos el menor elemento en el resto de la lista
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  
        
        # Intercambiamos el menor encontrado con el actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  
    
    return arr

# Ejemplo de uso
numeros = [64, 25, 12, 22, 11]
print("Lista original:", numeros)
print("Lista ordenada:", selection_sort(numeros))
