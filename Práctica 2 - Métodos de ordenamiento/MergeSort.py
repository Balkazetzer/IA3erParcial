# Algoritmo de ordenamiento por mezcla (MergeSort)
# Divide el arreglo en dos mitades, ordena cada mitad recursivamente y luego las une.

def merge_sort(arr):
    """
    Implementación del algoritmo MergeSort.
    :param arr: Lista desordenada.
    :return: Lista ordenada.
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Encontramos el punto medio
        left_half = arr[:mid]  # Dividimos en dos mitades
        right_half = arr[mid:]

        merge_sort(left_half)  # Ordenamos la mitad izquierda
        merge_sort(right_half)  # Ordenamos la mitad derecha

        i = j = k = 0

        # Fusionamos las mitades ordenadas
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Agregamos los elementos restantes de la mitad izquierda
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Agregamos los elementos restantes de la mitad derecha
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Ejemplo de uso
numeros = [38, 27, 43, 3, 9, 82, 10]
print("Lista original:", numeros)
print("Lista ordenada:", merge_sort(numeros))
