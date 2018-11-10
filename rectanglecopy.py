'''Program with rectangle class with its own unique starting upper-left point,
width, height and color.
homework_08
Fall 2018
@author: Caleb Vredevoogd (chv5)'''

import turtle
class Lab_rectangle:
    '''Rectangle class with upper-left starting point, height, 
    width and color.'''
    
    def __init__(self, point, h, w, c):
        '''Constructor for the rectangle object that constructs a rectangle
        from a given starting point, hieght, width and color. 
        Uses absolute values of h and w 
        to avoid negative height and width.'''
        self.start = point
        if w >= 0:
            self.width = w
        else:
            print("Invalid width. Set to absolute value.")
            self.width = abs(w)
        if h >= 0:
            self.height = h
        else:
            print("Invalid height. Set to absolute value.")
            self.height = abs(h)
            
        self.color = c
    
    def __str__(self):
        '''Overloaded string function to print internal state of the
        rectangle object'''
        print("Starting point" + str(self.start))
        print("Height: " + str(self.height))
        print("Width: " + str(self.width))
        print("Color: " + self.color)
        print("Perimeter: " + str(self.get_perimeter()))
        print("Area: " + str(self.get_area()))
    
    def get_start(self):
        '''Accessor function returns the starting point of a rectangle object'''
        return self.start
    
    def get_width(self):
        '''Accessor function returns width of a rectangle object'''
        return self.width
    
    def get_height(self):
        '''Accessor function returns height of a rectangle object'''
        return self.height
    
    def get_perimeter(self):
        '''Accessor function returns the perimeter of a rectangle object'''
        perimeter = (2*self.height) + (2*self.width)
        return perimeter
    
    def get_area(self):
        '''Accessor function returns the area of a rectangle object.'''
        area = self.get_height * self.get_width
        return area
    
    def modify_width(self, delta):
        '''Mutator function modifies the width of the rectangle object by a 
        difference of delta. Will accept negative delta values so long as
        width stays positive'''
        if delta > 0:
            self.width += delta
        if delta < 0 and abs(delta) < self.width:
            self.width += delta
        else:
            print("Delta's negative value is too large")
                        
        
    def modify_height(self, delta):
        '''Mutator function modifies the height of the rectangle object by a 
        difference of delta. Will accept negative delta values so long as
        height stays positive'''
        if delta > 0:
            self.height += delta
        if delta < 0 and abs(delta) < self.height:
            self.height += delta
        else:
            print("Delta's negative value is too large")
        
    def overlaps(self, other):
        '''Comparator function takes in two rectangle objects and returns True
        if they overlap in any way. Otherwise, return false.'''
        overlap = True
        if (self.get_width() + self.get_start()[0] < other.get_start()[0] or
            self.get_start()[0] > other.get_width() + other.get_start()[0]):
            overlap = False
        elif (self.get_height() + self.get_start()[1] < other.get_start()[1] or
            self.get_start()[1] > other.get_height() + other.get_start()[1]):
            overlap = False
            
        return overlap
    
    def render(self, pen):
        '''Function that calls a Turtle object to draw a rectangle object'''
        pen = turtle.Turtle()
        pen.color(self.color)
        pen.up()
        pen.goto(self.start)
        pen.seth(270)
        pen.down()
        pen.forward(self.get_height())
        pen.right(90)
        pen.forward(self.get_width())
        pen.right(90)
        pen.forward(self.get_height())
        pen.right(90)
        pen.forward(self.get_width())
        
#Test cases
if __name__ == ("__main__"):
    test_window = turtle.Screen()
    
    #Test case 1 (valid)
    print("Test case 1 (blue): ")
    test_pen1 = turtle.Turtle()
    test_pen1.hideturtle()
    test_rect1 = Lab_rectangle((-12,45), 45, 30, "blue")
    test_rect1.render(test_pen1)
    
    #Test case 2 (invalid height and width, should use absolute values; 
    #also modify rectangle height by a negative delta and width by a positive delta )
    print("Test case 2 (red): ")
    test_pen2 = turtle.Turtle()
    test_pen2.hideturtle()
    test_rect2 = Lab_rectangle((-12,45), -51, 30, "red")
    
    test_rect2.render(test_pen2)
    test_rect2.modify_height(-30)
    test_rect2.modify_width(30)
    test_rect2.render(test_pen2)
    
    #Test case 3 (2 disjoint rectangles)
    print("Test case 3 (orange and violet): ")
    test_pen3a = turtle.Turtle()
    test_pen3a.hideturtle()
    test_rect3a = Lab_rectangle((35, 47), 30, 30, "orange")
    
    test_pen3b = turtle.Turtle()
    test_pen3b.hideturtle()
    test_rect3b = Lab_rectangle((100, 70), 30, 30, "violet")
    
    test_rect3a.render(test_pen3a)
    test_rect3b.render(test_pen3b)
    print("Overlap is: " +str(test_rect3a.overlaps(test_rect3b)))
    
    #Test case 4 (2 overlapping rectangles)
    print("Test case 4 (green and black): ")
    test_pen4a = turtle.Turtle()
    test_pen4a.hideturtle()
    test_rect4a = Lab_rectangle((35, 47), 30, 30, "green")
    
    test_pen4b = turtle.Turtle()
    test_pen4b.hideturtle()
    test_rect4b = Lab_rectangle((36, 46), 24, 50, "black")
    
    test_rect4a.render(test_pen4a)
    test_rect4b.render(test_pen4b)
    print("Overlap is: " + str(test_rect4a.overlaps(test_rect4b)))
    
    test_window.exitonclick
    
    
    
