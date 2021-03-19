import math

# Basisklass Shape
class Shape:
    def __init__(self, xOrigin, yOrigin):
        self.__xOrigin = xOrigin
        self.__yOrigin = yOrigin

        def getArea(self):
            return self.__xOrigin * self.__yOrigin

        def getCircumference(self):
            return (self.__xOrigin + self.__yOrigin) * 2
        
        def getOrigin(self):
            position = 'The position of xOrigin is ' + str(self.__xOrigin) +\
                  'and the position of yOrigin is ' + str(self.__yOrigin)
            return position

        def getToString():
            formType = 'This is '
            return formType


# Subklasse Circle
class Circle(Shape):
    def __init__(self, xOrigin, yOrigin, radius):
        super().__init__(xOrigin, yOrigin)
        self.__radius = xOrigin * 2

    def getArea(self):
        return math.pi*(self.__radius**2)

    def getCircumference(self):
        return 2 * math.pi * self.__radius


# Subklasse Rectangle
class Rectangle(Shape):
    def __init__(self, x, y):
        self.__x = int(x)
        self.__y = int(y)

    def getArea(self):
            return self.__x * self.__y

    def getCircumference(self):
        return (self.__x + self.__y) * 2

    def getOrigin(self):
        return 'The position of xOrigin is ' + str(self.__x) +\
    '\nand the position of yOrigin is ' + str(self.__y)
    

# Subklasse Square
class Square(Shape):
    def __init__(self, x):
        self.__x = int(x)

    def getArea(self):
        return self.__x * self.__x

    def getCircumference(self):
        return self.__x * 4

    def getOrigin(self):
        return 'The position of xOrigin is ' + str(self.__x)

    def toString(self):
        shapeType = 'This is a square.'
        return shapeType


# ShapeTester
class ShapeTester:
    pass

