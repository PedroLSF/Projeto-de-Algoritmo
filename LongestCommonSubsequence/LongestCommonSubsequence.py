def lcs(X, Y):
    tamanho_x = len(X)
    tamanho_y = len(Y)

    comprimento = [[0] * (tamanho_y + 1) for _ in range(tamanho_x + 1)]

    for i in range(1, tamanho_x + 1):
        for j in range(1, tamanho_y + 1):
            if X[i - 1] == Y[j - 1]:
                comprimento[i][j] = comprimento[i - 1][j - 1] + 1
            else:
                comprimento[i][j] = max(comprimento[i - 1][j], comprimento[i][j - 1])

    return comprimento[tamanho_x][tamanho_y], backtracking(X, Y, comprimento)


def backtracking(X, Y, comprimento):
    subsequencia = ""
    i = len(X)
    j = len(Y)

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            subsequencia += X[i - 1]
            i -= 1
            j -= 1
        else:
            if comprimento[i - 1][j] >= comprimento[i][j - 1]:
                i -= 1
            else:
                j -= 1

    return subsequencia[::-1]
