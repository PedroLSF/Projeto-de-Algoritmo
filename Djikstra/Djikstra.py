import heapq

def dijkstra(graph, source):
    distancia = {vertice: float('inf') for vertice in graph}
    for vertice in graph:
        for vizinho, _ in graph[vertice]:
            distancia.setdefault(vizinho, float('inf'))
    distancia[source] = 0

    fila = [(0, source)]

    while fila:
        distancia_na_fila, atual = heapq.heappop(fila)

        if distancia_na_fila > distancia[atual]:
            continue

        for vizinho, peso in graph.get(atual, []):
            nova_distancia = distancia_na_fila + peso
            if nova_distancia < distancia[vizinho]:
                distancia[vizinho] = nova_distancia
                heapq.heappush(fila, (nova_distancia, vizinho))

    return distancia