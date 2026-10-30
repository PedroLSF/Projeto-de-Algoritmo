
def insertion_sort(arr):
    arrayToManipulate = arr
    for j in range(1, len(arrayToManipulate)):
        i = j-1
        key = arrayToManipulate[j]
        while i >= 0 and arrayToManipulate[i] > key:
            arrayToManipulate[i+1] = arrayToManipulate[i]
            i = i - 1
        arrayToManipulate[i + 1] = key

if __name__ == "__main__":
    testes = [
        [5, 2, 4, 6, 1, 3],
        [3, 1, 2],
        [1, 2, 3, 4],
        [4, 3, 2, 1],
        [7, 3, 7, 1, 3],
        [-2, 0, -5, 8],
        [42],
        [],
    ]

    for teste in testes:
        arr = teste.copy()
        insertion_sort(arr)
        status = "OK" if arr == sorted(teste) else "ERRO"
        print(f"{status}: {teste} -> {arr}")
