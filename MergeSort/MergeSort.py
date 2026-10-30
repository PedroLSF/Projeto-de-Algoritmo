def merge(left: list[int], right: list[int]):
    i = 0
    j = 0
    k = 0
    size = len(left) + len(right)
    c = list(range(size))
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            c[k] = left[i]
            i = i +1
        else:
            c[k] = right[j]
            j = j +1
        k = k + 1
    for j in range(j, len(right)):
        c[k] = right[j]
        k = k + 1
    for i in range(i, len(left)):
        c[k] = left[i]
        k = k + 1
    return c

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


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
        merged = merge_sort(arr)
        status = "OK" if merged == sorted(teste) else "ERRO"
        print(f"{status}: {teste} -> {arr}")
