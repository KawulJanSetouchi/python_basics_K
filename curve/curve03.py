import matplotlib.pyplot as plt
import numpy as np

# Bézier curve function
def bezier_curve(control_points, num_points=100):
    t = np.linspace(0, 1, num_points)
    n = len(control_points) - 1
    curve = np.zeros((num_points, 2))

    for i in range(num_points):
        curve[i] = sum(comb(n, i) * (1 - t[i]) ** (n - i) * t[i] ** i * control_points[i] for i in range(n + 1))

    return curve

# Control points for the Bézier curve
control_points = np.array([[1, 1], [2, 3], [4, 5], [6, 2]])

# Generate Bézier curve points
curve_points = bezier_curve(control_points)

# Plotting the Bézier curve
plt.figure(figsize=(6, 6))
plt.plot(control_points[:, 0], control_points[:, 1], 'ro-', label='Control Points')
plt.plot(curve_points[:, 0], curve_points[:, 1], 'b-', label='Bézier Curve')
plt.title('Bézier Curve')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True)
plt.show()
