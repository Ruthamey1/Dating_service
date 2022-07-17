
import math
import turtle

print('The purpose of this program is to find the angle between the co-ordinates you place in')
x_coord = int(input('What x co-ordinate would you like to go to first? '))
y_coord = int(input('What y co-ordinate would you like to go to first? '))
x_coord2 = int(input('What x co-ordinate would you like to go to next? '))
y_coord2 = int(input('What y co-ordinate would you like to go to next? '))

gradient_1 = y_coord/x_coord
gradient_2 = (y_coord2 - y_coord) / (x_coord2 - x_coord)

tan_angle = abs((gradient_2 - gradient_1)/ (1 + (gradient_1*gradient_2)))
angle_in_radians = math.atan(tan_angle)

angle_in_degrees = angle_in_radians *(180*math.pi)

turtle.goto(x_coord, y_coord)
turtle.write(x_coord)
turtle.goto(x_coord2, y_coord2)
turtle.write(x_coord2)
turtle.write(angle_in_degrees)
turtle.done()
