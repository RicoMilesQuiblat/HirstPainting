from turtle import Turtle, Screen
import random
# import colorgram
# colors = colorgram.extract('hirst.jpg',30)
#
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     color_list.append(new_color)

color_list = [(250, 247, 244), (248, 245, 246), (213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99), (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64), (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77), (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158), (235, 166, 171), (177, 204, 185), (49, 62, 84)]
screen = Screen()
tim = Turtle()
screen.colormode(255)
tim.up()
tim.hideturtle()
tim.speed(0)
tim.setposition(-300,-300)

y = -300


def change_color():
    new_color = random.choice(color_list)
    return new_color


def create_dots():
    for i in range(int(600 / 20)):
        temp_color = change_color()
        tim.pencolor(temp_color)
        tim.dot(10)
        tim.forward(20)


while y <= 300:
    create_dots()
    y += 20
    tim.setposition(-300, y)

print(screen)
screen.exitonclick()