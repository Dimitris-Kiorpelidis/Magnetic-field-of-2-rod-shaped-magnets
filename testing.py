import matplotlib.pyplot as plt
import numpy as np

import magpylib as magpy

# Create a Matplotlib figure
fig, ax = plt.subplots()

# Create an observer grid in the xy-symmetry plane - using pure numpy
grid = np.mgrid[-.05:.05:100j, -.05:.05:100j, 0:0:1j].T[0]
X, Y, _ = np.moveaxis(grid, 2, 0)

# Compute magnetic field on grid - using the functional interface
B = magpy.getB(
    "Cuboid",
    position = (0,0.01,0.01),
    observers=grid.reshape(-1, 3),
    dimension=(0.02, 0.03, 0.05,),
    polarization=(550,0, 0),
)
B = B.reshape(grid.shape)
Bx, By, _ = np.moveaxis(B, 2, 0)
normB = np.linalg.norm(B, axis=2)

# Combine streamplot with contourf
cp = ax.contourf(X, Y, normB, cmap="rainbow", levels=100)
splt = ax.streamplot(X, Y, Bx, By, color="k", density=1.5, linewidth=1)

# Add colorbar
fig.colorbar(cp, ax=ax, label="|B| (T)")



# Figure styling
ax.set(
    xlabel="x-position (m)",
    ylabel="z-position (m)",
    aspect=1,
)

plt.tight_layout()
plt.show()