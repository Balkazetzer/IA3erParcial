# Algoritmo de ordenamiento rápido (QuickSort)
# Divide la lista en dos partes alrededor de un pivote y ordena cada parte recursivamente.

def quicksort(arr):
    """
    Implementación del algoritmo QuickSort.
    :param arr: Lista desordenada.
    :return: Lista ordenada.
    """
    if len(arr) <= 1:
        return arr  # Caso base: una lista con 1 o menos elementos ya está ordenada

    pivot = arr[len(arr) // 2]  # Seleccionamos el pivote como el elemento central
    left = [x for x in arr if x < pivot]  # Elementos menores al pivote
    middle = [x for x in arr if x == pivot]  # Elementos iguales al pivote
    right = [x for x in arr if x > pivot]  # Elementos mayores al pivote

    # Aplicamos QuickSort recursivamente en las listas izquierda y derecha
    return quicksort(left) + middle + quicksort(right)

# Ejemplo de uso
numeros = [10, 7, 8, 9, 1, 5]
print("Lista original:", numeros)
print("Lista ordenada:", quicksort(numeros))
