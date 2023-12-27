import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from scipy.special import comb

# Define a function to calculate points on a Bezier curve
def bezier_curve(control_points, t):
    n = len(control_points) - 1
    curve_point = np.zeros(3)
    for i, point in enumerate(control_points):
        curve_point += comb(n, i) * ((1 - t) ** (n - i)) * (t ** i) * point
    return curve_point

# Create a figure and 3D axis
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Generate some sample data for mesh (you can replace this with your data)
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# Plot the mesh
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)

# Define control points for Bezier curve
control_points = np.array([[0, 0, 0], [2, 3, 1], [4, -1, 2], [6, 2, 3]])

# Generate points on the Bezier curve
t_values = np.linspace(0, 1, 100)
curve_points = np.array([bezier_curve(control_points, t) for t in t_values])

# Plotting the Bezier curve on the mesh
ax.plot(curve_points[:, 0], curve_points[:, 1], curve_points[:, 2], color='red', linewidth=2)

# Set labels and show plot
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
plt.title('Bezier Curve on a 3D Mesh')
plt.show()