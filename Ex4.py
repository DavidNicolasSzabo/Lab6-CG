import numpy as np
from scipy.spatial import Voronoi
A_points = [(1 - i, i - 1) for i in range(6)]
B_points = [(i, -i) for i in range(6)]
C_points = [(0, i) for i in range(6)]
points = np.array(A_points + B_points + C_points)
vor = Voronoi(points)
half_lines = 0
for ridge in vor.ridge_vertices:
    if -1 in ridge:
        half_lines += 1
print(f"Number of half-lines in the Voronoi diagram: {half_lines}")
