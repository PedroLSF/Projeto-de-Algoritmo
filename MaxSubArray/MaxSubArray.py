def max_crossing(A, lo, mid, hi):
    soma = 0
    soma_esq = float("-inf")
    idx_esq = mid
    for i in range(mid, lo - 1, -1):
        soma += A[i]
        if soma > soma_esq:
            soma_esq = soma
            idx_esq = i

    soma = 0
    soma_dir = float("-inf")
    idx_dir = mid + 1
    for j in range(mid + 1, hi + 1):
        soma += A[j]
        if soma > soma_dir:
            soma_dir = soma
            idx_dir = j

    return idx_esq, idx_dir, soma_esq + soma_dir


def max_subarray(A, lo=0, hi=None):
    if len(A) == 0:
        return 0
    if hi is None:
        hi = len(A) - 1
    if lo == hi:
        return lo, hi, A[lo]

    mid = (lo + hi) // 2
    esq = max_subarray(A, lo, mid)
    dir_ = max_subarray(A, mid + 1, hi)
    cruz = max_crossing(A, lo, mid, hi)

    return max(esq, dir_, cruz, key=lambda t: t[2])


A = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
print(max_subarray(A))