def floyd_warshall(matrix):
    n = len(matrix)
    predMatrix = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] != float('inf'):
                predMatrix[i][j] = i

    for k in range(n):
        for i in range(n):
            for j in range(n):
                distancia_via_k = matrix[i][k] + matrix[k][j]
                if distancia_via_k < matrix[i][j]:
                    matrix[i][j] = distancia_via_k
                    predMatrix[i][j] = predMatrix[k][j]

    return matrix
