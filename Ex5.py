import numpy as np
from scipy.spatial import Delaunay, Voronoi
def count_half_lines(voronoi):
    half_lines = 0
    for ridge in voronoi.ridge_vertices:
        if -1 in ridge:
            half_lines += 1
    return half_lines
def triangulate_and_voronoi(points):
    delaunay = Delaunay(points)
    edges = set()
    for simplex in delaunay.simplices:
        edges.update({tuple(sorted((simplex[i], simplex[j]))) for i in range(3) for j in range(i + 1, 3)})
    voronoi = Voronoi(points)
    half_lines = count_half_lines(voronoi)
    return len(edges), half_lines
M1 = np.array([(0, 0), (1, 0), (0, 1)])
M2 = np.array([(0, 0), (1, 0), (0, 1), (0.5, 0.5)])
edges_M1, half_lines_M1 = triangulate_and_voronoi(M1)
print(f"Set M1: {M1}")
print(f"Edges in triangulation: {edges_M1}")
print(f"Half-lines in Voronoi diagram: {half_lines_M1}")
print()
edges_M2, half_lines_M2 = triangulate_and_voronoi(M2)
print(f"Set M2: {M2}")
print(f"Edges in triangulation: {edges_M2}")
print(f"Half-lines in Voronoi diagram: {half_lines_M2}")
