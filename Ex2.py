import random
A1 = (5, -1)
A2 = (7, -1)
A3 = (9, -1)
A4 = (7, -3)
A5 = (11, -1)
A6 = (-9, 3)
def centroid(points):
    # calculates best center around which can the points A7 and A8 to be placed
    x_sum = sum([p[0] for p in points])
    y_sum = sum([p[1] for p in points])
    return (x_sum / len(points), y_sum / len(points))
def generate_A7_A8(points):
    center = centroid(points)
    A7_1 = (center[0] - random.uniform(10, 20), center[1] + random.uniform(5, 15))
    A8_1 = (center[0] + random.uniform(10, 20), center[1] - random.uniform(5, 15))
    A7_2 = (center[0] - random.uniform(10, 20), center[1] - random.uniform(5, 15))
    A8_2 = (center[0] + random.uniform(10, 20), center[1] + random.uniform(5, 15))
    return {A7_1, A8_1}, {A7_2, A8_2}
A7_A8_set_1, A7_A8_set_2 = generate_A7_A8([A1, A2, A3, A4, A5, A6])
print("Generated distinct sets of A7 and A8 that create 4 half-line edges:")
print(f"Set 1: {A7_A8_set_1}")
print(f"Set 2: {A7_A8_set_2}")
