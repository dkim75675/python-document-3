
def house():
    length = int(input("Enter the length of the house in feet: "))
    width = int(input("Enter the width of the house in feet: "))
    area = length * width
    print(f'The size of the house is {area} square feet.')

from math import pi

def circle():
    radius = int(input("Enter the length of the radius of the circle in feet: "))
    circumference = 2*float(radius)*pi
    print(f'The circumference of the circle is {circumference} feet')

