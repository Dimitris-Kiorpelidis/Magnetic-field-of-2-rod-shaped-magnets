import matplotlib.pyplot as plt
import numpy as np
import magpylib as magpy

# Create a Matplotlib figure
fig, ax = plt.subplots()

# Create an observer grid in the xy-symmetry plane - using pure numpy
grid = np.mgrid[-5:5:100j, -5:5:100j, 0:0:1j].T[0]
X, Y, _ = np.moveaxis(grid, 2, 0)


x_1 = 2
x_2 = -2
y_1 = 0
y_2 = 0

rod_shaped_magnet_1 = magpy.magnet.Cuboid(

    position = (x_1, y_1, 0),
    dimension = (1.5, 3, 0.5),
    polarization = (-50, 0, 0),
)

rod_shaped_magnet_2 = magpy.magnet.Cuboid(

    position = (x_2, y_2, 0),
    dimension = (1.5, 3, 0.5),
    polarization = (50, 0, 0),
)



magnets = rod_shaped_magnet_1 + rod_shaped_magnet_2

# Compute magnetic field on grid - using the functional interface
B = magnets.getB(grid)
Bx, By, _ = np.moveaxis(B, 2, 0)
normB = np.linalg.norm(B, axis=2)

splt = ax.streamplot(X, Y, Bx, By, color="k", density=1.5, linewidth=1)

#outline toy prwtoy magnhth
x_sin1 = rod_shaped_magnet_1.position[0] + rod_shaped_magnet_1.dimension[0]/2
x_plin1 = rod_shaped_magnet_1.position[0] - rod_shaped_magnet_1.dimension[0]/2
y_sin1 = rod_shaped_magnet_1.position[1] + rod_shaped_magnet_1.dimension[1]/2
y_plin1 = rod_shaped_magnet_1.position[1] - rod_shaped_magnet_1.dimension[1]/2

#outline toy deyteroy magnhth
x_sin2 = rod_shaped_magnet_2.position[0] + rod_shaped_magnet_1.dimension[0]/2
x_plin2 = rod_shaped_magnet_2.position[0] - rod_shaped_magnet_1.dimension[0]/2
y_sin2 = rod_shaped_magnet_2.position[1] + rod_shaped_magnet_1.dimension[1]/2
y_plin2 = rod_shaped_magnet_2.position[1] - rod_shaped_magnet_1.dimension[1]/2


ax.plot(
    [x_sin1, x_sin1, x_plin1, x_plin1, x_sin1],
    [y_sin1, y_plin1, y_plin1, y_sin1, y_sin1],

    [x_sin2, x_sin2, x_plin2, x_plin2, x_sin2],
    [y_sin2, y_plin2, y_plin2, y_sin2, y_sin2],
    lw = 2
)

# Figure styling
ax.set(
    xlabel="x-position (m)",
    ylabel="y-position (m)",
    aspect=1,
)

plt.tight_layout()
plt.show()