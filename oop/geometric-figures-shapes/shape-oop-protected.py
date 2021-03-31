import math

# Basisklass Shape
class Shape:
    # def __init__(self, shape, xOrigin, yOrigin):
    def __init__(self, shape, xOrigin, yOrigin):
        self._xOrigin = xOrigin
        self._yOrigin = yOrigin
        # self._shape = shape

        def area(self):
            return self._xOrigin * self._yOrigin

        def circumference(self):
            return (self._xOrigin + self._yOrigin) * 2
        
        def origin(self):
            position = 'The position of xOrigin is ' + str(self._xOrigin) +\
                  '\nand the position of yOrigin is ' + str(self._yOrigin)
            return position

        def toString(self):
            # formType = 'This is ' + self._shape
            formType = 'This is a '
            return formType


# Subklasse Circle
class Circle(Shape):
    # def __init__(self, shape, xOrigin, yOrigin):
    def __init__(self, radius):
        # super().__init__(shape, xOrigin, yOrigin)
        self._radius = radius * 2

    def area(self):
        return math.pi*(self._radius**2)

    def circumference(self):
        return 2 * math.pi * self._radius

    def origin(self):
        position = 'The position of xOrigin is ' + str(self._radius)
        return position

    def toString(self):
        return 'This is a circle.'



# Subklasse Rectangle
class Rectangle(Shape):
    # def __init__(self, shape, xOrigin, yOrigin):
    #     super().__init__(shape, xOrigin, yOrigin)
    def __init__(self, xOrigin, yOrigin):
        super().__init__(xOrigin, yOrigin)
        self._x = int(xOrigin)
        self._y = int(yOrigin)

    def area(self):
            return self._x * self._y

    def circumference(self):
        return (self._x + self._y) * 2

    def origin(self):
            position = 'The position of xOrigin is ' + str(self._xOrigin) +\
                '\nand the position of yOrigin is ' + str(self._yOrigin)
            return position

    def toString(self):
            # shapeType = 'This is a rectangle.' + self._shape
            shapeType = 'This is a rectangle.'
            return shapeType
    

# Subklasse Square
class Square(Shape):
    def __init__(self, x):
        self._x = int(x)

    def area(self):
        return self._x * self._x

    def circumference(self):
        return self._x * 4

    def origin(self):
        position = 'The position of xOrigin is ' + str(self._x)
        return position

    def toString(self):
            shapeType = 'This is a square.'
            return shapeType



# ShapeTester
class ShapeTester:
    pass



# C1 = Circle('Circle', 2, 2)
C1 = Circle( 3)
print('Circle area:', C1.area())
print('Circle circumference:', C1.circumference())
print('Circle origin:', C1.origin())
print('Circle toStr:', C1.toString())

print('==========================')

# R1 = Rectangle('rectangle', 2, 5)
# R1 = Rectangle( 2, 5)
# print('Rectangle area:', R1.area())
# print('Rectangle circumference:', R1.circumference())
# print('Rectangle origin:', R1.origin())
# print('Rectangle toStr:', R1.toString())

print('==========================')

# S1 = Square('square', 5)
S1 = Square(5)
print('Square area:', S1.area())
print('Square circumference:', S1.circumference())
print('Square origin:', S1.origin())
print('Square toStr:', S1.toString())

