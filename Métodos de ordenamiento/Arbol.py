# Algoritmo de ordenamiento de árbol (Tree Sort)
# Utiliza un Árbol Binario de Búsqueda (BST) para almacenar los elementos en un orden natural
# y luego realiza un recorrido en orden (in-order traversal) para obtener la lista ordenada.

class NodoBST:
    """
    Clase que representa un nodo en el Árbol Binario de Búsqueda.
    Cada nodo tiene un valor, un hijo izquierdo y un hijo derecho.
    """
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None  # Nodo hijo izquierdo
        self.derecha = None  # Nodo hijo derecho

class ArbolBST:
    """
    Clase que representa el Árbol Binario de Búsqueda (BST).
    Permite insertar elementos y realizar un recorrido en orden para obtener la lista ordenada.
    """
    def __init__(self):
        self.raiz = None  # Inicialmente el árbol está vacío

    def insertar(self, valor):
        """
        Inserta un valor dentro del árbol de manera recursiva.
        """
        if self.raiz is None:
            self.raiz = NodoBST(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        """
        Función auxiliar para insertar valores recursivamente en el árbol.
        """
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = NodoBST(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        else:
            if nodo.derecha is None:
                nodo.derecha = NodoBST(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)

    def recorrer_en_orden(self):
        """
        Realiza un recorrido en orden (In-Order Traversal) para obtener los valores en orden creciente.
        """
        resultado = []
        self._recorrer_en_orden_recursivo(self.raiz, resultado)
        return resultado

    def _recorrer_en_orden_recursivo(self, nodo, resultado):
        """
        Función auxiliar para recorrer recursivamente el árbol en orden.
        """
        if nodo is not None:
            self._recorrer_en_orden_recursivo(nodo.izquierda, resultado)
            resultado.append(nodo.valor)
            self._recorrer_en_orden_recursivo(nodo.derecha, resultado)

def tree_sort(arr):
    """
    Implementación del algoritmo Tree Sort utilizando un Árbol Binario de Búsqueda.
    :param arr: Lista desordenada.
    :return: Lista ordenada.
    """
    arbol = ArbolBST()
    for num in arr:
        arbol.insertar(num)  # Insertamos cada número en el árbol
    
    return arbol.recorrer_en_orden()  # Obtenemos la lista ordenada recorriendo el árbol

# Ejemplo de uso
numeros = [7, 3, 10, 1, 5, 8]
print("Lista original:", numeros)
print("Lista ordenada:", tree_sort(numeros))
