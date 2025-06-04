# Algoritmo de ordenamiento por fusión natural (Natural Merging)
# Identifica subsecuencias ordenadas en la lista y las fusiona hasta que toda la lista esté ordenada.

def natural_merge_sort(arr):
    """
    Implementación de Natural Merge Sort.
    :param arr: Lista desordenada.
    :return: Lista ordenada.
    """
    def find_runs(arr):
        """
        Identifica segmentos ya ordenados dentro de la lista.
        """
        runs = []
        temp_run = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]:
                temp_run.append(arr[i])
            else:
                runs.append(temp_run)
                temp_run = [arr[i]]
        
        runs.append(temp_run)
        return runs

    while True:
        runs = find_runs(arr)
        if len(runs) == 1:
            return runs[0]  # Si solo hay una sublista ordenada, terminamos
        
        new_arr = []
        for i in range(0, len(runs) - 1, 2):
            new_arr += merge(runs[i], runs[i + 1])  # Fusionamos las secuencias ordenadas
        
        if len(runs) % 2 == 1:
            new_arr += runs[-1]  # Agregamos la última lista si queda sin fusionar
        arr = new_arr

# Ejemplo de uso
numeros = [2, 3, 6, 5, 8, 10, 1, 4, 9, 7]
print("Lista original:", numeros)
print("Lista ordenada:", natural_merge_sort(numeros))
