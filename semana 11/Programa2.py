#Ordenación de arreglo multidimencional

# Definir una matriz 3x3 con valores numéricos
matriz = [
    [24, 5, 10],
    [12, 19, 2],
    [16, 4, 21]
]

# se ordena una fila específica utilizando la funcion de Bubble Sort
def bubble_sort_fila(matriz,fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                # Intercambiar los elementos si están en el orden incorrecto
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostrar la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

#ordenar fila
fila_a_ordenar = 2

# Ordenar la fila específica
bubble_sort_fila(matriz, fila_a_ordenar)

# Mostrar la matriz y fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)