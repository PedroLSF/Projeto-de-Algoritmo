from collections import deque


def bfs(graph, source):
    vertices = set(graph.keys())
    for neighbors in graph.values():
        vertices.update(neighbors)

    d = {v: float('inf') for v in vertices}
    pi = {v: None for v in vertices}

    d[source] = 0
    queue = deque([source])

    while len(queue) > 0:
        u = queue.popleft()
        vizinhos = graph.get(u, [])
        for i in range(len(vizinhos)):
            v = vizinhos[i]
            if (d[v] == float('inf')):
                d[v] = d[u] + 1
                pi[v] = u
                queue.append(v)

    return d, pi
