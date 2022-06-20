from graphics import *

class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

class Rectangle: 
    def __init__(self, posn, w, h): 
        self.corner = posn 
        self.width = w 
        self.height = h 

def __str__(self): 
    return "({0}, {1}, {2})".format(self.corner, self.width, self.height) 
    
def create_rectangle(x, y, width, height): 
    posn = Point(x,y) 
    rect = Rectangle(posn, width, height) 
    return rect 

def str_rectangle(rect): 
    return (rect.corner.x, rect.corner.y, rect.width, rect.height) 

def shift_rectangle(rect, dx, dy): 
    rect.corner.x += dx 
    rect.corner.y += dy 

def offset_rectangle(rect, dx, dy): 
    x = rect.corner.x + dx 
    y = rect.corner.y + dy 
    return(create_rectangle(x, y, rect.width, rect.height)) 


#Code Test for Assignment 5
r1 = create_rectangle(10, 20, 30, 40) 
print(str_rectangle(r1))

shift_rectangle(r1, -10, -20)
print(str_rectangle(r1)) 

r2 = offset_rectangle(r1, 100, 100) 
print(str_rectangle(r2)) 

print(str_rectangle(r1)) 
