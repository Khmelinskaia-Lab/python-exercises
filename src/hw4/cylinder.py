__author__ = "Alena Khmelinskaia"
__email__ = "akhmelin@uw.edu"

from math import pi


class Cylinder:
    def __init__(self, ...) -> None:
        ...
    #    """Write code here to define a class Cylinder
    #
    #    Define a class Cylinder with the following features:
    #
    #    1.  a function to initialize. this should accept a radius and
    #        a height. If not specified, both should default to 1.
    #
    #    2.  a function called __str__, which is already defined for you.
    #
    #    3.  an accessor function to get the radius, and one for the height.
    #        eg: get_radius(self)
    #
    #    4.  a mutator function to change the radius, and one for the height.
    #        eg: set_height(self, h)
    #
    #    5.  a function to get the surface area of one of the bases using
    #        the formula pi * r ^ 2
    #
    #    6.  a function to get the curved surface area using the formula
    #        2 * pi * r * h
    #
    #    7.  a function to get the total surface area that calls functions
    #        in points 5 and 6 with the formula
    #        total surface area = curved surface area + 2 * base area
    #
    #    This class file does not need a main function.
    #    """

    def __str__(self) -> str:
        #    """This function is used to print details about the cylinder.
        #       This returns the radius and height when print(Cylinder()) is
        #       called.
        #       """
        ...

    def get_radius(self) -> float:
        ...

    def get_height(self) -> float:
        ...

    def set_radius(self, r: float) -> None:
        ...

    def set_height(self, h: float) -> None:
        ...

    def get_base_SA(self) -> float:
        ...

    def get_curved_SA(self) -> float:
        ...

    def get_total_SA(self) -> float:
        ...

