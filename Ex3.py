import math
A = (-1, 6)
B = (-1, -1)
C = (4, 7)
D = (6, 7)
E = (1, -1)
F = (-5, 3)
P = (-2, 3)
def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1
def kruskal(points):
    n = len(points)
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            dist = distance(points[i], points[j])
            edges.append((dist, i, j))
    edges.sort()
    uf = UnionFind(n)
    mst_weight = 0
    for dist, u, v in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_weight += dist

    return mst_weight
def compute_mst_for_lambda(lambda_value):
    Q = (2 - lambda_value, 3)
    points = [A, B, C, D, E, F, P, Q]
    return kruskal(points)
def find_optimal_lambda():
    min_mst_length = float('inf')
    optimal_lambda = 0
    for lambda_value in [i * 0.1 for i in range(0, 21)]:
        mst_length = compute_mst_for_lambda(lambda_value)
        print(f"Lambda: {lambda_value}, MST length: {mst_length}")
        if mst_length < min_mst_length:
            min_mst_length = mst_length
            optimal_lambda = lambda_value
    return optimal_lambda
optimal_lambda = find_optimal_lambda()
print(f"Optimal lambda for minimal MST length: {optimal_lambda}")
