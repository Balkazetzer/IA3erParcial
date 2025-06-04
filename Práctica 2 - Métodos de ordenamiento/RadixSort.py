# Algoritmo de ordenamiento Radix Sort
# Ordena los números revisando cada dígito individualmente desde el menos significativo hasta el más significativo.

def radix_sort(arr):
    """
    Implementación del algoritmo Radix Sort.
    :param arr: Lista de números desordenada.
    :return: Lista ordenada.
    """
    max_val = max(arr)  # Encontramos el número más grande para determinar la cantidad de dígitos
    exp = 1  # Inicializamos el dígito menos significativo

    while max_val // exp > 0:
        counting_sort(arr, exp)  # Aplicamos Counting Sort por cada dígito
        exp *= 10  # Pasamos al siguiente dígito

    return arr

def counting_sort(arr, exp):
    """
    Función auxiliar para Radix Sort que implementa Counting Sort basado en un dígito específico.
    :param arr: Lista de números desordenada.
    :param exp: Factor de orden (unidad, decena, centena, etc.).
    """
    n = len(arr)
    output = [0] * n  # Lista ordenada temporal
    count = [0] * 10  # Contador de frecuencia de cada dígito (0-9)

    # Contamos cuántos elementos tienen cada dígito
    for i in range(n):
        index = arr[i] // exp % 10
        count[index] += 1

    # Ajustamos las posiciones en la lista final
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construimos la lista ordenada
    i = n - 1
    while i >= 0:
        index = arr[i] // exp % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copiamos los elementos ordenados a la lista original
    for i in range(n):
        arr[i] = output[i]

# Ejemplo de uso
numeros = [170, 45, 75, 90, 802, 24, 2, 66]
print("Lista original:", numeros)
print("Lista ordenada:", radix_sort(numeros))
