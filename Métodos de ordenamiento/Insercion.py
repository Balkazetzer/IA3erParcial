# Algoritmo de ordenamiento por inserción (Insertion Sort)
# Este algoritmo ordena un arreglo de manera ascendente 
# Comparando cada elemento con los anteriores e insertándolo en su posición correcta.

def insertion_sort(arr):
    """
    Función que implementa el algoritmo de ordenamiento por inserción.
    :param arr: Lista de números desordenada.
    :return: Lista ordenada.
    """
    # Recorremos la lista desde el segundo elemento hasta el último
    for i in range(1, len(arr)):
        # Guardamos el valor actual que queremos insertar en el lugar correcto
        valor_actual = arr[i]  
        j = i - 1  
        
        # Desplazamos los elementos que sean mayores al valor_actual hacia la derecha
        while j >= 0 and arr[j] > valor_actual:
            arr[j + 1] = arr[j]  
            j -= 1  
        
        # Insertamos el valor en la posición correcta
        arr[j + 1] = valor_actual  

    return arr

# Ejemplo de uso
numeros = [5, 2, 9, 1, 5, 6]
print("Lista original:", numeros)
print("Lista ordenada:", insertion_sort(numeros))
