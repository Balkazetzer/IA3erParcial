# Algoritmo de distribución de series iniciales (Distribution of Initial Runs)
# Separa la lista en segmentos y los distribuye para su posterior ordenamiento.

def distribute_initial_runs(arr):
    """
    Implementación de Distribution of Initial Runs.
    :param arr: Lista desordenada.
    :return: Lista ordenada.
    """
    def create_initial_runs(arr):
        """ Separa la lista en pequeñas secuencias ordenadas. """
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

    runs = create_initial_runs(arr)  # Identificamos secuencias iniciales ordenadas
    sorted_arr = []
    for run in runs:
        sorted_arr += run  # Unimos las secuencias ordenadas
    
    return sorted_arr

# Ejemplo de uso
numeros = [5, 3, 6, 4, 7, 1, 2]
print("Lista original:", numeros)
print("Lista ordenada:", distribute_initial_runs(numeros))
