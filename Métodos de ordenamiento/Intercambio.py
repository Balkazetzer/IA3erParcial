# Algoritmo de ordenamiento por intercambio (Bubble Sort)
# Compara pares de elementos adyacentes y los intercambia si están en el orden incorrecto.

def bubble_sort(arr):
    """
    Función que implementa el ordenamiento por intercambio.
    :param arr: Lista de números desordenada.
    :return: Lista ordenada.
    """
    n = len(arr)
    
    for i in range(n):
        # Bucle interno para comparar los elementos adyacentes
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:  
                # Intercambiamos los elementos si están desordenados
                arr[j], arr[j+1] = arr[j+1], arr[j]  
    
    return arr

# Ejemplo de uso
numeros = [5, 3, 8, 6, 2]
print("Lista original:", numeros)
print("Lista ordenada:", bubble_sort(numeros))
