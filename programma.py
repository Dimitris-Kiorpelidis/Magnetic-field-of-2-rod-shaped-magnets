import magpylib as magpy
import numpy as np
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

#Δημιουργία μαγνητών
rod_shaped_magnet_1 = magpy.magnet.Cuboid(

    position = (-3, 0, 0),
    dimension = (1, 0.3, 2.5),
    polarization = (0, 0, 550),

)

rod_shaped_magnet_2 = magpy.magnet.Cuboid(

    position = (3, 0, 0),
    dimension = (1, 0.3, 2.5),
    polarization = (0, 0, 550),
)

magnets = magpy.Collection(rod_shaped_magnet_1, rod_shaped_magnet_2)


ts = np.linspace(-5, 5, 40)
#grid = np.mgrid[-.05:.05:100j, -.05:.05:100j, 0:0:1j].T[0]
grid = np.array([[(x, 0, z) for x in ts] for z in ts])
X, _, Z = np.moveaxis(grid, 2, 0)


B = magnets.getB(grid)
Bx, _, Bz = np.moveaxis(B, 2, 0)
log10_norm_B = np.log10(np.linalg.norm(B, axis = 2))
normB = np.linalg.norm(B, axis=2)

#cp = ax.contourf(X, Z, normB, cmap="rainbow", levels=100)
splt = ax.streamplot(X, Z, Bx, Bz,
                     density = 1.5,
                     color = log10_norm_B,
                     linewidth = log10_norm_B,
                     cmap = "autumn",
                     )


ax.set(
    xlabel="x-position (mm)",
    ylabel="z-position (mm)",
)

plt.tight_layout()
plt.show()