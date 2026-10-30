def cut_rod(prices, n):
    r = list(range(n+1))
    rounds = 0
    for j in range(1, n + 1):
        q = float("-inf")
        for i in range(1, j + 1):
            rounds += 1
            q = max(q, prices[i - 1] + r[j - i])
        r[j] = q
    final_price = r[n]

    return final_price, rounds


if __name__ == "__main__":
    testes = [
        ([2, 3, 6, 7, 10], 4, 8, 10),
        ([21], 1, 21, 1),
        ([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 10, 30, 55),
        ([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 4, 10, 10),
        ([5], 0, 0, 0),
    ]

    for prices, n, esperado, ops_esperado in testes:
        final_price, rounds = cut_rod(prices, n)
        status = "OK" if (final_price, rounds) == (esperado, ops_esperado) else "ERRO"
        print(f"{status}: n={n} -> Bottom-Up Result: {final_price} | Ops: {rounds}")
