# Understanding the abstract base class.
from abc import ABC, abstractclassmethod
class GraphicShape(ABC):
    """
    This is a base class GraphicShape which is been called in the following shape classes.
    """
    def __init__(self) -> None:
        super().__init__()

    @abstractclassmethod
    def cal_area(self):
        """
        This is a abstract class method so when a base class inherits the GraphicShape then it has 
        to use the cla_area method.
        """
        pass


class Circle(GraphicShape):
    """
    This is a sub class that inherits GraphicShape base class with the abstract class method
    """
    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius

    def cal_area(self):
        return 3.14 * (self.radius ** 2)

class Square(GraphicShape):
    """
    This is a sub class that inherits GraphicShape base class with the abstract class method
    """
    def __init__(self, side) -> None:
        super().__init__()
        self.side = side
    def cal_area(self):
        return self.side * self.side

c1 = Circle(2)
sq1 = Square(23)

print(f">>> Area of the circle c1 🟢: {c1.cal_area()}")
print(f">>> Area of the square sq1 🟩: {sq1.cal_area()}")

# Output:
# >>> Area of the circle c1 🟢: 12.56
# >>> Area of the square sq1 🟩: 529