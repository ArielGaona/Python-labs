Задание 1

a = [3,2,5,5,5,9,6,5,8,4,8,7,1,9,0]

b = a[1::2]
print(b)

Задание 2


list = [1,3,2,0,4,2,7,8,9]
new = []
b = 0
def order(list):
    for i in range(len(list)):
        if list[i] > list[i-1]:
            b = list[i]
            new.append(b)
        else:
            continue
    return new
    
    
    
print(order(list))


Задание 3

A = [1,0,4,7,1,9,5,3]

def swap_min(A):
    a = max(A)
    b = min(A)
    A[A.index(a)] = b
    A[A.index(b)] = a
    
    print (A)
    
    
swap_min(A)


Задание 4

A = {'name': "Ariel",
 'networth': "$32B",
 'company':"Aerobabel"}

def slavar(dict, key):
    
    b = dict[key]
    print(b)
    
    return
    
    
    
    
slavar(A, 'name')


Задание 5

from figure import *

circle_area()
circle_area(12)

circle_perimeter()
circle_perimeter(11)

triangle_perimeter()
triangle_perimeter(2,2,7)

triangle_area()
triangle_area(5,9,6)

square_perimeter()
square_perimeter(4)

square_area()
square_area(4)