# Understanding Dataclass.
from dataclasses import dataclass, field
import random

def price_function():
    """
    This function generates a random float between 20 to 400.
    """
    return float(random.randrange(20,400))

@dataclass
class Book:
    """
    A data class representing a Book object.
    Attributes:
    title (str): The title of the book.
    author (str): The author of the book.
    pages (int): The number of pages in the book.
    price (float): The price of the book. Defaults to a value returned by `price_function`.
    """
    title: str
    author: str
    pages: int
    price: float = field(default_factory=price_function) 

    def __post_init__(self):
        """
        __post_init__(self): A method that runs after the object is initialized.
        Sets the `description` attribute.
        """
        self.description = f"{self.title} by {self.author} at {self.price}"

# Deceleration of b1.
b1 = Book("Go Girl", "Ram", 234,)
b2 = Book("Go Girl", "Ram", 234,)
b3 = Book("Go Man", "Tom", 23, 34.99)

# Observing dataclass's built-in __repr__ and __eq__:
print(b1)
print(b2)
print(b3)
print(f"If b1 is equal to b2 with build-in __eq__ method in dataclass: {b1==b2}")
print(f"If b1 is equal to b3 with build-in __eq__ method in dataclass: {b1==b3}")
print(f"New Attribute description for b1: {b1.description}")
print(f"New Attribute description for b3: {b3.description}")

# Outputs:
# Book(title='Go Girl', author='Ram', pages=234, price=266.0)
# Book(title='Go Girl', author='Ram', pages=234, price=231.0)
# Book(title='Go Man', author='Tom', pages=23, price=34.99)
# If b1 is equal to b2 with build-in __eq__ method in dataclass: False
# If b1 is equal to b3 with build-in __eq__ method in dataclass: False
# New Attribute description for b1: Go Girl by Ram at 266.0
# New Attribute description for b3: Go Man by Tom at 34.99