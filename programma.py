import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import numpy as np
import magpylib as magpy

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize =(7,7.5),)

# Create an observer grid in the xy-symmetry plane - using pure numpy
orio_plot = 10.0
grid = np.mgrid[-1 * orio_plot:orio_plot:100j, -1 * orio_plot:orio_plot:100j, 0:0:1j].T[0]
X, Y, _ = np.moveaxis(grid, 2, 0)

x_1 = 2.0
x_2 = -2.0
y_1 = 0.0
y_2 = 0.0

rod_shaped_magnet_1 = magpy.magnet.Cuboid(

    position = (x_1, y_1, 0),
    dimension = (0.8, 3, 0.5),
    polarization = (0, -50, 0),
)

rod_shaped_magnet_2 = magpy.magnet.Cuboid(

    position = (x_2, y_2, 0),
    dimension = (0.8, 3, 0.5),
    polarization = (0, 50, 0),
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

    lw = 2,
)


def recreate1(expression):
    global orio_plot, grid, X, Y
    if expression !=0:
        ax.clear()
        current_orio_plot = orio_plot
        if (rod_shaped_magnet_1.position[0] + float(expression) > orio_plot):
            while(current_orio_plot + float(expression) > orio_plot):
                orio_plot +=5

            grid = np.mgrid[-1 * orio_plot:orio_plot:100j, -1 * orio_plot:orio_plot:100j, 0:0:1j].T[0]
            X, Y, _ = np.moveaxis(grid, 2, 0)

        magnets[0].move((expression,0,0))
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

            lw = 2,
        )
        plt.show()

    

def recreate2(expression):
    global orio_plot, grid, X, Y
    if expression !=0:
        ax.clear()
        current_orio_plot = orio_plot
        if (rod_shaped_magnet_2.position[0] + float(expression) > orio_plot):
            while(current_orio_plot + float(expression) > orio_plot):
                orio_plot +=5

            grid = np.mgrid[-1 * orio_plot:orio_plot:100j, -1 * orio_plot:orio_plot:100j, 0:0:1j].T[0]
            X, Y, _ = np.moveaxis(grid, 2, 0)

        magnets[1].move((expression,0,0))
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

            lw = 2,
        )
        plt.show()
    
    
# Figure styling
ax.set(
    title = "Μαγνητικό πεδίο 2 μαγνητών (2D)",
    xlabel="x (m)",
    ylabel="y (m)",
    aspect=1,
)


axbox1 = plt.axes([0.8, 0.001, 0.05, 0.03])
axbox2 = plt.axes([0.3, 0.001, 0.05, 0.03])
text_box1 = TextBox(axbox1, 'Μετακίνηση του δεξιά μαγνήτη', initial = 0, textalignment='center', label_pad=0.2)
text_box2 = TextBox(axbox2, 'Μετακίνηση του αριστερά μαγνήτη', initial = 0, textalignment='center', label_pad=0.2)

text_box1.on_submit(recreate1)
text_box2.on_submit(recreate2)

plt.show()