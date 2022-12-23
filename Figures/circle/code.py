from math import pi 

default_radius = 5

def circle_perimeter(r = default_radius):
    peri = 2 * pi * r 
    return peri
    
    
def circle_area(r = default_radius):
    area = pi * (r ** 2)
    return area
