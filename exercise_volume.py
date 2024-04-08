"""Write a program that prompts the user to enter the length (L), width (W), and height (H) of a box.
The program will then compute and display the volume and surface area of the box. 
(Hint: Volume = L × W × H; Surface area = 2×[(L × W) + (L × H) + (H × W)].)

Example output:

length? 10
width? 10
height? 10

The volume is 1000 and the surface is 600.
"""

#Function to calculate the volume of the box
def calculate_volume(l, w, h):
    volume =  l * w * h
    return volume

#Function to calculate the surface of the box
def calculate_surface(l, w, h):
    surface = 2*((l * w) + (l * h) + (h * w))
    return surface

#Input length
l = int(input("length? "))

#Input width
w = int(input("width? "))

#Input Height
h = int(input("height? "))

#variable box_volume
box_volume = calculate_volume(l, w, h)

#Variable surface_box
surface_box = calculate_surface(l, w, h)

#Print the resutlts to the screen
print("The volume is",box_volume, "and the surface is ",surface_box,".")