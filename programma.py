import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox
import numpy as np
import magpylib as magpy
from scipy.spatial.transform import Rotation as R


def magnet_movement(magnet, orio_plot, x_movement):
    #checks if the grid needs to increase, to have the magnets on screen and then moves the magnet
    ax.clear()
    if (magnet.position[0] + x_movement > orio_plot) or (magnet.position[0] + x_movement < -1*orio_plot):
            
        orio_plot += (x_movement ** 2) ** 0.5

    magnet.move((x_movement, 0, 0))
    return orio_plot

    

def rotate_magnet(magnet, rotation):
    #rotates the magnet
    magnet.rotate_from_angax(angle = rotation, axis = 'z')
    
def make_grid(magnets, orio_plot, grid, current_angle1, current_angle2):

    #reset the figures grid and plot it with the given magnets rotation and/or movement
    #shows the magnets north pole (red) and south pole (blue and green)

    ax.clear()

    grid = np.mgrid[-1 * orio_plot:orio_plot:100j, -1 * orio_plot:orio_plot:100j, 0:0:1j].T[0]
    X, Y, _ = np.moveaxis(grid, 2, 0)
    B = magnets.getB(grid)
    Bx, By, _ = np.moveaxis(B, 2, 0)
    normB = np.linalg.norm(B, axis=2)
    splt = ax.streamplot(X, Y, Bx, By, color="k", density=1.5, linewidth=1)

    #first magnets corner coordinates
    x_sin1 = rod_shaped_magnet_1.position[0] + rod_shaped_magnet_1.dimension[0]/2
    x_plin1 = rod_shaped_magnet_1.position[0] - rod_shaped_magnet_1.dimension[0]/2
    y_sin1 = rod_shaped_magnet_1.position[1] + rod_shaped_magnet_1.dimension[1]/2
    y_plin1 = rod_shaped_magnet_1.position[1] - rod_shaped_magnet_1.dimension[1]/2

    #second magnets corner coordinates
    x_sin2 = rod_shaped_magnet_2.position[0] + rod_shaped_magnet_2.dimension[0]/2
    x_plin2 = rod_shaped_magnet_2.position[0] - rod_shaped_magnet_2.dimension[0]/2
    y_sin2 = rod_shaped_magnet_2.position[1] + rod_shaped_magnet_2.dimension[1]/2
    y_plin2 = rod_shaped_magnet_2.position[1] - rod_shaped_magnet_2.dimension[1]/2

    #split each in 4 rectangles so the rotation is applied from the middle of the magnet,
    #if it was one or 2 "patches" it whould rotate each "patch" from the bottom left corner as the anchor
    #the only way i could show the rotation correctly, i might have missed a better/correct way
    magnet1_north_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2,
                                            rod_shaped_magnet_1.dimension[1]/2, color = "r",angle = current_angle1)
    ax.add_patch(magnet1_north_right)

    magnet1_north_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2,
                                        rod_shaped_magnet_1.dimension[1]/2, color = "r",angle = current_angle1)
    ax.add_patch(magnet1_north_left)

    magnet1_south_left = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), rod_shaped_magnet_1.dimension[0]/2,
                                        rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180)
    ax.add_patch(magnet1_south_left)

    magnet1_south_right = plt.Rectangle(((x_sin1+x_plin1)/2, (y_sin1+y_plin1)/2), -1*rod_shaped_magnet_1.dimension[0]/2,
                                            rod_shaped_magnet_1.dimension[1]/2, color = "b", angle = current_angle1 + 180)
    ax.add_patch(magnet1_south_right)


    magnet2_north_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2,
                                            rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2)
    ax.add_patch(magnet2_north_right)

    magnet2_north_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2,
                                        rod_shaped_magnet_2.dimension[1]/2, color = "r", angle = current_angle2)
    ax.add_patch(magnet2_north_left)

    magnet2_south_left = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), rod_shaped_magnet_2.dimension[0]/2,
                                        rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180)
    ax.add_patch(magnet2_south_left)

    magnet2_south_right = plt.Rectangle(((x_sin2+x_plin2)/2, (y_sin2+y_plin2)/2), -1*rod_shaped_magnet_2.dimension[0]/2,
                                            rod_shaped_magnet_2.dimension[1]/2, color = "g", angle = current_angle2 + 180)
    ax.add_patch(magnet2_south_right)


    # Figure styling
    ax.set(
    title = "Μαγνητικό πεδίο 2 μαγνητών (2D)",
    xlabel="x",
    ylabel="y",
    aspect=1,
    )

    return magnets, B

def move_x_1(expression):
    #moves the first magnet and remakes the grid 
    if float(expression) != 0:
        global current_angle1,current_angle2, orio_plot
        orio_plot = magnet_movement(magnets[0], orio_plot, float(expression))
        make_grid(magnets, orio_plot, grid, current_angle1, current_angle2)
        text_box_x_1.set_val("0")
        plt.show()
        

def move_x_2(expression):
    #moves the second magnet and remakes the grid
    if float(expression) != 0:
        global current_angle1,current_angle2, orio_plot
        orio_plot = magnet_movement(magnets[1], orio_plot, float(expression))
        make_grid(magnets, orio_plot, grid, current_angle1, current_angle2)
        text_box_x_2.set_val("0")
        plt.show()

def rotate_1(expression):
    #rotates the first magnet and remakes the grid
    if float(expression) != 0:
        global current_angle1,current_angle2
        current_angle1 += float(expression)
        rotate_magnet(magnets[0], float(expression))
        make_grid(magnets, orio_plot, grid, current_angle1, current_angle2)
        text_box_rotate_1.set_val("0")
        plt.show()

def rotate_2(expression):
    #rotates the second magnet adn remakes the grid
    if float(expression) != 0:
        global current_angle1,current_angle2
        current_angle2 += float(expression)
        rotate_magnet(magnets[1], float(expression))
        make_grid(magnets, orio_plot, grid, current_angle1, current_angle2)
        text_box_rotate_2.set_val("0")
        plt.show()


if __name__ == "__main__":

    #-------------------------------------------------
    #made the code cleaner than the previous one, no longer have 4 funtions with the only difference being the move and rotate
    #the program can now be imported for the same use as mine, but won't make "my" magnets, grid and textboxs
    #haven't found/made a better/cleaner/more-optimal, yet

    

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

    orio_plot = 10.0
    grid = np.mgrid[-1 * orio_plot:orio_plot:100j, -1 * orio_plot:orio_plot:100j, 0:0:1j].T[0]
    X, Y, _ = np.moveaxis(grid, 2, 0)
    make_grid(magnets, orio_plot, grid, current_angle1, current_angle2)

    axbox_x_1 = plt.axes([0.94, 0.045, 0.05, 0.03])
    axbox_x_2 = plt.axes([0.44, 0.045, 0.05, 0.03])
    axbox_rotate_1 = plt.axes([0.94, 0.001, 0.05, 0.03])
    axbox_rotate_2 = plt.axes([0.44, 0.001, 0.05, 0.03])

    text_box_x_1 = TextBox(axbox_x_1, 'Μετακίνηση του μπλε μαγνήτη', initial = 0, textalignment='center', label_pad=0.2)
    text_box_x_2 = TextBox(axbox_x_2, 'Μετακίνηση του πράσινου μαγνήτη', initial = 0, textalignment='center', label_pad=0.2)
    text_box_rotate_1 = TextBox(axbox_rotate_1, 'Περιστορφή του μπλε μαγνήτη (μύρες)', initial = 0, textalignment='center', label_pad=0.2)
    text_box_rotate_2 = TextBox(axbox_rotate_2, 'Περιστορφή του πράσινου μαγνήτη (μύρες)', initial = 0, textalignment='center', label_pad=0.2)

    #the on_submit whoulnd't let me call a funtion with more than the "expression" variable
    #made an extra function that gets the expression and calls the right fuction for the given 
    #input, either rotation or movement of a magnet
    text_box_x_1.on_submit(move_x_1)
    text_box_x_2.on_submit(move_x_2)
    text_box_rotate_1.on_submit(rotate_1)
    text_box_rotate_2.on_submit(rotate_2)

    plt.show()