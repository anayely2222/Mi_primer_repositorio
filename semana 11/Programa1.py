#Se define una matriz 3x3
matriz= [
         [2,7,18],
         [40,32,24],
         [5,19,44]
]
def buscar_matriz(matriz, val_buscado):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==val_buscado:
                return i, j

    return None
buscar_val=7
#Se busca el valor en la matriz
resultado= buscar_matriz(matriz,buscar_val)

#se muestra el resultado
if resultado:
    print(f"El valor{buscar_val} fue encontrado en la posicion{resultado}.")
else:
    print(f"El valor {buscar_val} no se encontro en la matriz dada")