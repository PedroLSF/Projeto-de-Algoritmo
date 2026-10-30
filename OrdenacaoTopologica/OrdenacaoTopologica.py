def topological_sort(graph):
    vertices = list(graph.keys())
    for neighbors in graph.values():
        for v in neighbors:
            if v not in graph and v not in vertices:
                vertices.append(v)

    visited = {v: False for v in vertices}
    order = []

    def dfs_visit(u):
        visited[u] = True
        vizinhos = graph.get(u, [])
        for i in range(len(vizinhos)):
            v = vizinhos[i]
            if (not visited[v]):
                dfs_visit(v)
        order.append(u)

    for u in vertices:
        if (not visited[u]):
            dfs_visit(u)

    order.reverse()

    pos = {v: i for i, v in enumerate(order)}
    for u in graph:
        for v in graph[u]:
            if (pos[u] >= pos[v]):
                raise ValueError("Graph contains a cycle")

    return order
