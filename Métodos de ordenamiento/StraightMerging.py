# Algoritmo de ordenamiento por fusión directa (Straight Merging)
# Divide la lista en sublistas de tamaño fijo, las ordena y luego las fusiona.

def straight_merge_sort(arr, block_size=2):
    """
    Implementación de Straight Merging Sort.
    :param arr: Lista desordenada.
    :param block_size: Tamaño inicial de los bloques para fusionar.
    :return: Lista ordenada.
    """
    n = len(arr)
    while block_size < n:
        new_arr = []
        for i in range(0, n, block_size * 2):
            left = arr[i:i + block_size]  # Primera mitad
            right = arr[i + block_size:i + block_size * 2]  # Segunda mitad
            new_arr += merge(left, right)  # Fusionamos
        arr = new_arr
        block_size *= 2  # Doblamos el tamaño del bloque

    return arr

def merge(left, right):
    """
    Función auxiliar para fusionar dos listas ordenadas.
    """
    sorted_list = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Ejemplo de uso
numeros = [42, 20, 17, 13, 8, 5, 3, 1]
print("Lista original:", numeros)
print("Lista ordenada:", straight_merge_sort(numeros))
