import matplotlib.pyplot as plt
import numpy as np

def draw_bezier_curve(control_points):
    t = np.linspace(0, 1, 100)
    n = len(control_points) - 1

    def bernstein_poly(i, n, t):
        return np.math.comb(n, i) * (t ** i) * ((1 - t) ** (n - i))

    x_vals = []
    y_vals = []
    for time in t:
        x = 0
        y = 0
        for i, point in enumerate(control_points):
            x += point[0] * bernstein_poly(i, n, time)
            y += point[1] * bernstein_poly(i, n, time)
        x_vals.append(x)
        y_vals.append(y)

    plt.plot(x_vals, y_vals, label='Bézier Curve')
    plt.scatter(*zip(*control_points), color='red', label='Control Points')
    plt.title('Bézier Curve')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.axis('equal')
    plt.show()

def draw_circle(center, radius):
    theta = np.linspace(0, 2*np.pi, 100)
    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    plt.plot(x, y, label='Circle')
    plt.scatter(*center, color='red', label='Center')
    plt.title('Circle')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.axis('equal')
    plt.show()

# Example: Draw a Bézier curve and a circle
# Bézier curve control points
control_points = [(1, 1), (2, 4), (5, 6), (7, 3)]
draw_bezier_curve(control_points)

# Circle parameters: center and radius
center = (3, 3)
radius = 2
draw_circle(center, radius)
