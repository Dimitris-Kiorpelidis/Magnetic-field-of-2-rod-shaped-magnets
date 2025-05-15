import magpylib as magpy
import numpy as np
import matplotlib.pyplot as plt

#Δημιουργία ενός απλού style για την εμφάνιση των μαγνητών, με τη βοήθεια παραδειγμάτων από το user_guide
#https://magpylib.readthedocs.io/en/latest/_pages/user_guide/examples/examples_vis_magnet_colors.html

mstyle = dict(
    mode = "color+arrow",
    color = dict(north = "red", south = "blue"),
    arrow = dict(width = 2, color = "k")
)


rod_shaped_magnet_1 = magpy.magnet.Cylinder(

    polarization = (0, 0, 1),
    dimension = (0.1, 0.2),
    position = (0.3, 0, 0),
    style_magnetization = mstyle,                         #Δεν κατάφερα,προς το παρόν, να έχω bicolor στο dictionary mstyle
    style_magnetization_color_mode = "bicolor"

)


rod_shaped_magnet_2 = magpy.magnet.Cylinder(
    polarization = (0, 0, 1),
    dimension = (0.1, 0.2),
    position = (0.8, 0 ,0),
    style_magnetization = mstyle,
    style_magnetization_color_mode = "bicolor"
    )



magpy.show(rod_shaped_magnet_1,rod_shaped_magnet_2)