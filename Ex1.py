import tkinter as tk
import random

WIDTH = 600
HEIGHT = 600
POINT_RADIUS = 5
PADDING = 0.1

class Point:
    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
def delaunay_triangulation(points):
    triangles = []
    for i in range(len(points)-2):
        triangles.append(Triangle(points[i], points[i+1], points[i+2]))
    return triangles
def euclidean_distance(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5
def compute_voronoi(points, width, height):
    colors = {}
    for i, _ in enumerate(points):
        colors[i] = f"#{random.randint(0, 0xFFFFFF):06x}"
    grid = [[None for _ in range(width)] for _ in range(height)]
    for y in range(height):
        for x in range(width):
            distances = [euclidean_distance((x, y), point) for point in points]
            nearest_site = distances.index(min(distances))
            grid[y][x] = colors[nearest_site]
    return grid
def draw_voronoi(canvas, grid, width, height):
    for y in range(height):
        for x in range(width):
            color = grid[y][x]
            canvas.create_line(x, y, x + 1, y, fill=color)
def visualize(canvas, triangulation, points):
    for triangle in triangulation:
        canvas.create_line(triangle.p1.x, triangle.p1.y, triangle.p2.x, triangle.p2.y, fill="black")
        canvas.create_line(triangle.p2.x, triangle.p2.y, triangle.p3.x, triangle.p3.y, fill="black")
        canvas.create_line(triangle.p3.x, triangle.p3.y, triangle.p1.x, triangle.p1.y, fill="black")
    for point in points:
        canvas.create_oval(point.x - POINT_RADIUS, point.y - POINT_RADIUS, point.x + POINT_RADIUS,
                           point.y + POINT_RADIUS, fill="red", outline="red")
        canvas.create_text(point.x + 10, point.y - 10, text=point.name, fill="black")
def adjust_points_for_canvas(points, width, height, min_val=-20, max_val=20, padding=0.1):
    padding_x = width * padding
    padding_y = height * padding
    usable_width = width - 2 * padding_x
    usable_height = height - 2 * padding_y
    min_x = min(p.x for p in points)
    max_x = max(p.x for p in points)
    min_y = min(p.y for p in points)
    max_y = max(p.y for p in points)
    x_scale = usable_width / (max_val - min_val)
    y_scale = usable_height / (max_val - min_val)
    x_offset = -min_x * x_scale + padding_x
    y_offset = -min_y * y_scale + padding_y
    for point in points:
        point.x = point.x * x_scale + x_offset
        point.y = point.y * y_scale + y_offset
def main():
    points = [
        Point(3, -5, 'A'),
        Point(-6, 6, 'B'),
        Point(6, -4, 'C'),
        Point(5, -5, 'D'),
        Point(9, 10, 'E')
    ]
    adjust_points_for_canvas(points, WIDTH, HEIGHT, min_val=-20, max_val=20, padding=PADDING)
    triangulation = delaunay_triangulation(points)
    voronoi_grid = compute_voronoi([(p.x, p.y) for p in points], WIDTH, HEIGHT)
    root = tk.Tk()
    root.title("Voronoi Diagram and Delaunay Triangulation")
    canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
    canvas.pack()
    draw_voronoi(canvas, voronoi_grid, WIDTH, HEIGHT)
    visualize(canvas, triangulation, points)
    root.mainloop()
if __name__ == "__main__":
    main()
