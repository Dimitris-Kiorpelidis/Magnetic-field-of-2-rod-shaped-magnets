import matplotlib.pyplot as plt
import numpy as np
import magpylib as magpy

# Create an observer grid in the xy-symmetry plane - using pure numpy
grid = np.mgrid[-5:5:100j, -5:5:100j, 0:0:1j].T[0]
X, Y, _ = np.moveaxis(grid, 2, 0)

mstyle = dict(
    mode = "color",
    color = dict(north = "red", south = "blue"),

)

rod_shaped_magnet_1 = magpy.magnet.Cuboid(

    position = (2, 0, 0),
    dimension = (1, 2, 0.5),
    polarization = (0, 990, 0),
    style_magnetization = mstyle,
    style_magnetization_color_mode = "bicolor",
)

rod_shaped_magnet_2 = magpy.magnet.Cuboid(

    position = (-2, 0, 0),
    dimension = (1, 2, 0.5),
    polarization = (0, 990, 0),
    style_magnetization = mstyle,
    style_magnetization_color_mode = "bicolor",
)

magnets = rod_shaped_magnet_1 + rod_shaped_magnet_2

# Compute magnetic field on grid - using the functional interface
B = magnets.getB(grid)
# B = B.reshape(grid.shape)
Bx, By, _ = np.moveaxis(B, 2, 0)
normB = np.linalg.norm(B, axis=2)


magpy.show(magnets)