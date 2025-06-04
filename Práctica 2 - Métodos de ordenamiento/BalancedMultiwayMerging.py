# Algoritmo de ordenamiento Balanced Multiway Merging
# Divide la lista en múltiples partes y las fusiona utilizando múltiples archivos o arreglos.

def balanced_multiway_merge_sort(arr, num_ways=3):
    """
    Implementación de Balanced Multiway Merging Sort.
    :param arr: Lista desordenada.
    :param num_ways: Número de partes en las que se dividirá.
    :return: Lista ordenada.
    """
    sublists = [arr[i::num_ways] for i in range(num_ways)]  # Dividimos la lista en partes
    sublists = [sorted(sublist) for sublist in sublists]  # Ordenamos cada parte
    
    result = []
    while any(sublists):  # Mientras haya elementos en alguna sublista
        min_vals = [sublist[0] if sublist else float('inf') for sublist in sublists]
        min_index = min_vals.index(min(min_vals))  
        result.append(sublists[min_index].pop(0))  # Tomamos el menor elemento disponible

    return result

# Ejemplo de uso
numeros = [9, 7, 2, 8, 5, 4, 6, 1, 3]
print("Lista original:", numeros)
print("Lista ordenada:", balanced_multiway_merge_sort(numeros))
