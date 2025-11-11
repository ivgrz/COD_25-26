def matrices_suma(A, B):
    """
    Esta funcion calcula la suma de dos matrices ateriormente inicializadas
    :param A: Primera matriz
    :type A: 
    :param B:
    :return: La lista con la suma de matrices
    :rtype: list[int]
    """

    filas_A = len(A)
    cols_A = len(A[0]) if filas_A > 0 else 0
    filas_B = len(B)
    cols_B = len(B[0]) if filas_B > 0 else 0
    if filas_A != filas_B or cols_A != cols_B:
        return None
    matriz_suma = []
    for i in range(filas_A):
        fila = []
        for j in range(cols_A):
            elemento_suma = A[i][j] + B[i][j]
            fila.append(elemento_suma)
        matriz_suma.append(fila)
    return matriz_suma

def transponer_matriz(M):
    filas = len(M)
    cols = len(M[0])
    M_traspuesta = [[0] * filas for _ in range(cols)]
    for i in range(filas):
        for j in range(cols):
            M_traspuesta[j][i] = M[i][j]
    return M_traspuesta

def multiplicar_matrices(A, B):
    filas_A = len(A)
    if filas_A == 0:
        return None
    cols_A = len(A[0])
    filas_B = len(B)
    if filas_B == 0:
        return None
    cols_B = len(B[0])
    if cols_A != filas_B:
        return None
    matriz_producto = [[0] * cols_B for _ in range(filas_A)]
    for i in range(filas_A):
        for j in range(cols_B):
            suma_productos = 0
            for k in range(cols_A):
                suma_productos += A[i][k] * B[k][j]
            matriz_producto[i][j] = suma_productos
    return matriz_producto

MATRIZ_A = [[1, 2],
            [3, 4]]
MATRIZ_B = [[5, 6],
            [7, 8]]
MATRIZ_C = [[10, 20, 30],
            [40, 50, 60]]
MATRIZ_D = [[1], [2], [3]]

suma_resultado = matrices_suma(MATRIZ_A, MATRIZ_B)
print("Suma (A + B):\n", suma_resultado)

producto_resultado = multiplicar_matrices(MATRIZ_A, MATRIZ_B)
print("\nProducto (A * B):\n", producto_resultado)

producto_diferente = multiplicar_matrices(MATRIZ_C, MATRIZ_D)
print("\nProducto (C * D):\n", producto_diferente)

producto_fallido = multiplicar_matrices(MATRIZ_A, MATRIZ_C)
print("\nProducto fallido (A * C):\n", producto_fallido)