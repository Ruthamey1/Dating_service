import math 

print('This program will help you plan your garden.')
print('First, w need some information about the dimensions you want.')
side_length = int(input('Please enter the side length for your garden (in feet): '))
distance = int(input('Please enter the distance between the plants (in inches): '))
depth_flower = float(input('Please enter the depth of the flower beds (in feet): '))
depth_fill = float(input('Please enter the depth for the fill (in feet): '))

area_triangular_bed = (side_length**2) * 0.25
area_circular_bed = math.pi * (0.125 * (side_length)**2)
triangular_plants = int(area_triangular_bed / (distance/12))
circle_plants = int(area_circular_bed / (distance/12))
total_plants = int((4*triangular_plants) + circle_plants)
print('Summary of your plant needs.')
print(f'Each outer triangular bed: {triangular_plants} plants.')
print(f'The center circular bed: {circle_plants} plants')
print(f'Total {total_plants} plants')
print()
triangle_soil = (area_triangular_bed * depth_flower)/ 54
circle_soil = (area_circular_bed * depth_flower)/54
total_soil = (4*triangle_soil) + circle_soil
print('Summary of your soil needs.')
print(f'Each outer triangular bed: {round(triangle_soil, 1)} cu. yd.')
print(f'Each outer cirular bed: {round(circle_soil, 1)} cu. yd.')
print(f'Total: {round(total_soil, 1)} cu. yd.')
print()
area_of_square = side_length * 2
fill_area = area_of_square - (area_circular_bed + (4 * area_triangular_bed))
fill_cubic = (fill_area * depth_fill)/54
print('Summary of your fill needs.')
print(f'Total: {round(fill_cubic, 1)} cu. yd.')
