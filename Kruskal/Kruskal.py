class DisjointSet:
    def __init__(self, vertices):
        self.pai = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, v):
        if self.pai[v] != v:
            self.pai[v] = self.find(self.pai[v])
        return self.pai[v]

    def union(self, u, v):
        raiz_u = self.find(u)
        raiz_v = self.find(v)

        if raiz_u == raiz_v:
            return False

        if self.rank[raiz_u] < self.rank[raiz_v]:
            self.pai[raiz_u] = raiz_v
        elif self.rank[raiz_u] > self.rank[raiz_v]:
            self.pai[raiz_v] = raiz_u
        else:
            self.pai[raiz_v] = raiz_u
            self.rank[raiz_u] += 1
        return True


def kruskal(vertices, edges):
    conjuntos = DisjointSet(vertices)
    mst_edges = []
    total_weight = 0

    for u, v, peso in sorted(edges, key=lambda aresta: aresta[2]):
        if conjuntos.union(u, v):
            mst_edges.append((u, v, peso))
            total_weight += peso
            if len(mst_edges) == len(vertices) - 1:
                break

    return mst_edges, total_weight
