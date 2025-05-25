import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import numpy as np
import magpylib as magpy
from scipy.spatial.transform import Rotation as R

# Create a Matplotlib figure
fig, ax = plt.subplots(figsize =(7,7.5),)


rod_shaped_magnet_1 = magpy.magnet.Cuboid(

    position = (2, 0, 0),
    dimension = (0.8, 3, 0.5),
    polarization = (0, 100, 0),
)

rod_shaped_magnet_2 = magpy.magnet.Cuboid(

    position = (-2, 0, 0),
    dimension = (0.8, 3, 0.5),
    polarization = (0, 100, 0),
)

magnets = rod_shaped_magnet_1 + rod_shaped_magnet_2

current_angle1 = 0
current_angle2 = 0

# Create an observer grid in the xy-symmetry plane - using pure numpy
orio_plot = 10.0
grid = np.mgrid[-1 * orio_plot:orio_plot:100j, -1 * orio_plot:orio_plot:100j, 0:0:1j].T[0]
X, Y, _ = np.moveaxis(grid, 2, 0)


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
x_sin2 = rod_shaped_magnet_2.position[0] + rod_shaped_magnet_2.dimension[0]/2
x_plin2 = rod_shaped_magnet_2.position[0] - rod_shaped_magnet_2.dimension[0]/2
y_sin2 = rod_shaped_magnet_2.position[1] + rod_shaped_magnet_2.dimension[1]/2
y_plin2 = rod_shaped_magnet_2.position[1] - rod_shaped_magnet_2.dimension[1]/2


magnet1_north_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "r", angle = current_angle1)
ax.add_patch(magnet1_north_right)

magnet1_north_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "r", angle = current_angle1)
ax.add_patch(magnet1_north_left)

magnet1_south_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180)
ax.add_patch(magnet1_south_left)

magnet1_south_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180)
ax.add_patch(magnet1_south_right)



magnet2_north_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2)
ax.add_patch(magnet2_north_right)

magnet2_north_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2)
ax.add_patch(magnet2_north_left)

magnet2_south_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180)
ax.add_patch(magnet2_south_left)

magnet2_south_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180)
ax.add_patch(magnet2_south_right)

# Figure styling
ax.set(
    title = "Μαγνητικό πεδίο 2 μαγνητών (2D)",
    xlabel="x (m)",
    ylabel="y (m)",
    aspect=1,
)


def move_x_1(expression):           #Μετακίνηση του 1ου μαγνήτη στον άξονα Χ και υπολογισμός του μαγνητικού πεδίου
    global orio_plot, grid, X, Y
    if float(expression) !=0:
        ax.clear()
        
        if (rod_shaped_magnet_1.position[0] + float(expression) > orio_plot) or (rod_shaped_magnet_1.position[0] + float(expression) < -1 * orio_plot): #expanding the plot if the movement exceeds the limit
            orio_plot += (float(expression)**2)** 0.5

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
        x_sin2 = rod_shaped_magnet_2.position[0] + rod_shaped_magnet_2.dimension[0]/2
        x_plin2 = rod_shaped_magnet_2.position[0] - rod_shaped_magnet_2.dimension[0]/2
        y_sin2 = rod_shaped_magnet_2.position[1] + rod_shaped_magnet_2.dimension[1]/2
        y_plin2 = rod_shaped_magnet_2.position[1] - rod_shaped_magnet_2.dimension[1]/2

        magnet1_north_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "r", angle = current_angle1)
        ax.add_patch(magnet1_north_right)

        magnet1_north_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "r", angle = current_angle1)
        ax.add_patch(magnet1_north_left)

        magnet1_south_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180)
        ax.add_patch(magnet1_south_left)

        magnet1_south_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180)
        ax.add_patch(magnet1_south_right)



        magnet2_north_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2)
        ax.add_patch(magnet2_north_right)

        magnet2_north_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2)
        ax.add_patch(magnet2_north_left)

        magnet2_south_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180)
        ax.add_patch(magnet2_south_left)

        magnet2_south_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180)
        ax.add_patch(magnet2_south_right)


        # Figure styling
        ax.set(
        title = "Μαγνητικό πεδίο 2 μαγνητών (2D)",
        xlabel="x (m)",
        ylabel="y (m)",
        aspect=1,
        )

        plt.show()

    

def move_x_2(expression):               #Μετακίνηση του 2ου μαγνήτη στον άξονα Χ και υπολογισμός του μαγνητικού πεδίου
    global orio_plot, grid, X, Y
    if float(expression) !=0:
        ax.clear()

        if (rod_shaped_magnet_2.position[0] + float(expression) > orio_plot) or (rod_shaped_magnet_2.position[0] + float(expression) < -1 * orio_plot): #expanding the plot if the movement exceeds the limit
            orio_plot += (float(expression)**2)** 0.5

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
        x_sin2 = rod_shaped_magnet_2.position[0] + rod_shaped_magnet_2.dimension[0]/2
        x_plin2 = rod_shaped_magnet_2.position[0] - rod_shaped_magnet_2.dimension[0]/2
        y_sin2 = rod_shaped_magnet_2.position[1] + rod_shaped_magnet_2.dimension[1]/2
        y_plin2 = rod_shaped_magnet_2.position[1] - rod_shaped_magnet_2.dimension[1]/2

        magnet1_north_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "r", angle = current_angle1)
        ax.add_patch(magnet1_north_right)

        magnet1_north_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "r", angle = current_angle1)
        ax.add_patch(magnet1_north_left)

        magnet1_south_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180)
        ax.add_patch(magnet1_south_left)

        magnet1_south_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180)
        ax.add_patch(magnet1_south_right)



        magnet2_north_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2)
        ax.add_patch(magnet2_north_right)

        magnet2_north_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2)
        ax.add_patch(magnet2_north_left)

        magnet2_south_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180)
        ax.add_patch(magnet2_south_left)

        magnet2_south_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180)
        ax.add_patch(magnet2_south_right)


        ax.set(
        title = "Μαγνητικό πεδίο 2 μαγνητών (2D)",
        xlabel="x (m)",
        ylabel="y (m)",
        aspect=1,
        )
        
        plt.show()

def rotate_1(expression):       #rotation of 1st magnet
    if float(expression) != 0:

        global current_angle1

        ax.clear()

        rod_shaped_magnet_1.rotate_from_angax(angle=float(expression), axis='z')
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
        x_sin2 = rod_shaped_magnet_2.position[0] + rod_shaped_magnet_2.dimension[0]/2
        x_plin2 = rod_shaped_magnet_2.position[0] - rod_shaped_magnet_2.dimension[0]/2
        y_sin2 = rod_shaped_magnet_2.position[1] + rod_shaped_magnet_2.dimension[1]/2
        y_plin2 = rod_shaped_magnet_2.position[1] - rod_shaped_magnet_2.dimension[1]/2

        magnet1_north_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "r", angle = current_angle1 + float(expression))
        ax.add_patch(magnet1_north_right)

        magnet1_north_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "r", angle = current_angle1 + float(expression))
        ax.add_patch(magnet1_north_left)

        magnet1_south_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180 + float(expression))
        ax.add_patch(magnet1_south_left)

        magnet1_south_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180 + float(expression))
        ax.add_patch(magnet1_south_right)



        magnet2_north_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2)
        ax.add_patch(magnet2_north_right)

        magnet2_north_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2)
        ax.add_patch(magnet2_north_left)

        magnet2_south_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180)
        ax.add_patch(magnet2_south_left)

        magnet2_south_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180)
        ax.add_patch(magnet2_south_right)


        ax.set(
        title = "Μαγνητικό πεδίο 2 μαγνητών (2D)",
        xlabel="x (m)",
        ylabel="y (m)",
        aspect=1,
        )

        current_angle1 += float(expression)

        plt.show()

def rotate_2(expression):       #rotation of 2nd magnet
    if float(expression) !=0:

        global current_angle2
        
        ax.clear()

        rod_shaped_magnet_2.rotate_from_angax(angle=float(expression), axis='z')
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
        x_sin2 = rod_shaped_magnet_2.position[0] + rod_shaped_magnet_2.dimension[0]/2
        x_plin2 = rod_shaped_magnet_2.position[0] - rod_shaped_magnet_2.dimension[0]/2
        y_sin2 = rod_shaped_magnet_2.position[1] + rod_shaped_magnet_2.dimension[1]/2
        y_plin2 = rod_shaped_magnet_2.position[1] - rod_shaped_magnet_2.dimension[1]/2

        magnet1_north_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "r", angle = current_angle1)
        ax.add_patch(magnet1_north_right)

        magnet1_north_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "r", angle = current_angle1)
        ax.add_patch(magnet1_north_left)

        magnet1_south_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180)
        ax.add_patch(magnet1_south_left)

        magnet1_south_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2, rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180)
        ax.add_patch(magnet1_south_right)



        magnet2_north_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2 + float(expression))
        ax.add_patch(magnet2_north_right)

        magnet2_north_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2 + float(expression))
        ax.add_patch(magnet2_north_left)

        magnet2_south_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180 + float(expression))
        ax.add_patch(magnet2_south_left)

        magnet2_south_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2, rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180 + float(expression))
        ax.add_patch(magnet2_south_right)


        ax.set(
        title = "Μαγνητικό πεδίο 2 μαγνητών (2D)",
        xlabel="x (m)",
        ylabel="y (m)",
        aspect=1,
        )
        
        current_angle2 += float(expression)

        plt.show()

axbox_x_1 = plt.axes([0.94, 0.045, 0.05, 0.03])
axbox_x_2 = plt.axes([0.44, 0.045, 0.05, 0.03])
axbox_rotate_1 = plt.axes([0.94, 0.001, 0.05, 0.03])
axbox_rotate_2 = plt.axes([0.44, 0.001, 0.05, 0.03])

text_box_x_1 = TextBox(axbox_x_1, 'Μετακίνηση του μπλε μαγνήτη', initial = 0, textalignment='center', label_pad=0.2)
text_box_x_2 = TextBox(axbox_x_2, 'Μετακίνηση του πράσινου μαγνήτη', initial = 0, textalignment='center', label_pad=0.2)
text_box_rotate_1 = TextBox(axbox_rotate_1, 'Περιστορφή του μπλε μαγνήτη (μύρες)', initial = 0, textalignment='center', label_pad=0.2)
text_box_rotate_2 = TextBox(axbox_rotate_2, 'Περιστορφή του πράσινου μαγνήτη (μύρες)', initial = 0, textalignment='center', label_pad=0.2)


text_box_x_1.on_submit(move_x_1)
text_box_x_2.on_submit(move_x_2)
text_box_rotate_1.on_submit(rotate_1)
text_box_rotate_2.on_submit(rotate_2)

plt.show()