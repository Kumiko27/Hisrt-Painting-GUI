# This package receives an image and a value that indicates the number of colors rgb values
# You want to extract from the image.
# Then the colors are stored in a list in a tuple format (r, g, b)
# Once we get the colors we copy and paste the values to create a list to use in the project
# The code is commented out because we only need to run it once to get the color list.

#import colorgram

#colors = colorgram.extract('image.jpg', 30)
#colors_list = []
#for i in range(0, 30):
#    r = colors[i].rgb[0]
#    g = colors[i].rgb[1]
#    b = colors[i].rgb[2]
#    my_color = (r, g, b)
#    colors_list.append(my_color)

#print(colors_list)

import random
import turtle as t
t.colormode(255)
tim = t.Turtle()

color_list = [(0, 0, 0), (142, 176, 208), (25, 32, 48), (24, 107, 160), (208, 163, 113), (143, 30, 63), (235, 220, 233), (230, 211, 92), (3, 162, 197), (219, 58, 82), (229, 80, 42), (54, 167, 115), (26, 62, 118), (195, 127, 166), (170, 53, 97), (106, 181, 86), (109, 99, 87), (240, 204, 2), (193, 187, 47), (1, 103, 119), (18, 21, 20), (48, 152, 109), (173, 212, 171), (117, 37, 36), (57, 39, 64), (222, 173, 187), (154, 206, 219)]

y = -225
x = -250
tim.penup()
tim.hideturtle()
for _ in range(10):
    tim.sety(y)
    tim.setx(x)
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    x = -250
    y += 50

my_screen = t.Screen()
my_screen.exitonclick()
