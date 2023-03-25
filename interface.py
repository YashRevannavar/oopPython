# Understanding the abstract base class and multiple inheritance.
from abc import ABC, abstractclassmethod

class JSONify(ABC):
    @abstractclassmethod
    def toJSON(cls, self):
        pass


class GraphicShape(ABC):
    """
    This is a base class GraphicShape which is been called in the following shape classes.
    """
    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def cal_area(cls, self):
        """
        This is a abstract class method so when a base class inherits the GraphicShape then it has 
        to use the cla_area method.
        """
        pass


class Circle(GraphicShape, JSONify):
    """
    This is a sub class that inherits GraphicShape and JSONify base class with the abstract class method.
    """
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def cal_area(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        """
        Here the sub class Circle uses the JSONify base class.
        """
        return f"{{ \"Circle\" : {str(self.cal_area())} }}"

class Square(GraphicShape,JSONify):
    """
    This is a sub class that inherits GraphicShape and JSONify base class with the abstract class method.
    """
    def __init__(self, side) -> None:
        super().__init__()
        self.side = side
    def cal_area(self):
        return self.side * self.side

    def toJSON(self):
        """
        Here the sub class Square uses the JSONify base class.
        """
        return f"{{ \"Square\" : {str(self.cal_area())} }}"

c1 = Circle(2)
sq1 = Square(23)

print(f">>> Area of the circle c1 🟢: {c1.cal_area()}")
print(f">>> Area of the circle c1 in JSON format : {c1.toJSON()}")
print(f">>> Area of the square sq1 🟩: {sq1.cal_area()}")
print(f">>> Area of the square sq1 in JSON format : {sq1.toJSON()}")

# Output:
# >>> Area of the circle c1 🟢: 12.56
# >>> Area of the circle c1 in JSON format : { "Circle" : 12.56 }
# >>> Area of the square sq1 🟩: 529
# >>> Area of the square sq1 in JSON format : { "Square" : 529 }
