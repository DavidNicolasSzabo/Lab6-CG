import itertools
import math

def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    return 1 if val > 0 else -1
def do_intersect(p1, q1, p2, q2):
    o1 = orientation(p1, q1, p2)
    o2 = orientation(p1, q1, q2)
    o3 = orientation(p2, q2, p1)
    o4 = orientation(p2, q2, q1)
    if o1 != o2 and o3 != o4:
        return True
    if o1 == 0 and on_segment(p1, q1, p2): return True
    if o2 == 0 and on_segment(p1, q1, q2): return True
    if o3 == 0 and on_segment(p2, q2, p1): return True
    if o4 == 0 and on_segment(p2, q2, q1): return True
    return False
def on_segment(p, q, r):
    return min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and min(p[1], r[1]) <= q[1] <= max(p[1], r[1])
def convex_hull(points):
    points = sorted(points)
    lower = []
    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) != -1:
            lower.pop()
        lower.append(p)
    upper = []
    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) != -1:
            upper.pop()
        upper.append(p)
    return lower[:-1] + upper[:-1]
def triangulate(points):
    hull = convex_hull(points)
    triangles = set()
    for p1, p2, p3 in itertools.combinations(hull, 3):
        if orientation(p1, p2, p3) != 0:
            triangles.add(frozenset([p1, p2, p3]))
    return triangles
def count_edges(triangles):
    edges = set()
    for triangle in triangles:
        # Generate all pairs of points (edges) from the triangle
        edges.update([frozenset([p1, p2]) for p1, p2 in itertools.combinations(triangle, 2)])
    return len(edges)
def triangulation_count(points):
    triangles = triangulate(points)
    num_triangles = len(triangles)
    num_edges = count_edges(triangles)
    return num_triangles, num_edges
def get_points(lambda_value):
    A = (1, 1)
    B = (1, -1)
    C = (-1, -1)
    D = (-1, 1)
    E = (0, -2)
    M = (0, lambda_value)
    return [A, B, C, D, E, M]
lambda_value = 0.5
points = get_points(lambda_value)
num_triangles, num_edges = triangulation_count(points)
print(f"Number of triangles: {num_triangles}")
print(f"Number of edges: {num_edges}")
