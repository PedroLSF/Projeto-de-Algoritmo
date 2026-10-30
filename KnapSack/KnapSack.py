def knapsack(values, weights, capacity):
    qtd_itens = len(values)

    melhor_valor = [[0] * (capacity + 1) for _ in range(qtd_itens + 1)]

    for i in range(1, qtd_itens + 1):
        valor_item = values[i - 1]
        peso_item = weights[i - 1]

        for capacidade_atual in range(capacity + 1):
            sem_item = melhor_valor[i - 1][capacidade_atual]
            melhor_valor[i][capacidade_atual] = sem_item

            if peso_item <= capacidade_atual:
                capacidade_restante = capacidade_atual - peso_item
                com_item = melhor_valor[i - 1][capacidade_restante] + valor_item
                melhor_valor[i][capacidade_atual] = max(sem_item, com_item)

    return melhor_valor[qtd_itens][capacity]