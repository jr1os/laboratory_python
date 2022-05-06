# abstract base class work

from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")


class Pentagon(Polygon):
    def noofsides(self):
        print("I have 5 sides")


class Hexagon(Polygon):
    def noofsides(self):
        print("I have 6 sides")


if __name__ == "__main__":
    R = Triangle()
    R.noofsides()

    k = Pentagon()
    k.noofsides()
