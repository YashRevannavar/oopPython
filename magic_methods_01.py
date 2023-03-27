# Understanding str and repr Magic Methods:

class Book:
    """
    The Book class represents a book with its attributes such as title, price, author, and pages.
    It has three methods:
    """

    def __init__(self, title, price, author, pages) -> None:
        """
        __init__(self, title, price, author, pages) - initializes the object of class Book with 
        the given parameters: title, price, author, and pages.
        """
        self.title = title
        self.price = price
        self.author = author
        self.pages = pages

    def __str__(self) -> str:
        """
        __str__(self) - returns a formatted string representation of 
        the Book object that contains information such as title, author, pages, and price.
        """
        return f"{self.title}, book is written by {self.author} with {self.pages} pricing at {self.price}"

    def __repr__(self) -> str:
        """
        __repr__(self) - returns a string representation of the Book object that is used 
        for debugging purposes. 
        It contains information such as title, author, pages, and price.
        """
        return f"Title = {self.title}, Author = {self.author}, Pages = {self.pages}, Price = {self.price}"


# Deceleration of b1 and b2
b1 = Book("Go man", 890, "Harry", 452)
b2 = Book("Go girl", 856, "Tom", 1025)

# Observing __str__ and __repr__:
print(f"\n>>> b1 with __str__ magic method: {str(b1)}")
print(f">>> b2 with __str__ magic method: {str(b2)}\n")
print(f">>> b1 with __repr__ magic method:{repr(b1)}")
print(f">>> b2 with __repr__ magic method:{repr(b2)}")

# Outputs:

# >>> b1 with __str__ magic method: Go man, book is written by Harry with 452 pricing at 890
# >>> b2 with __str__ magic method: Go girl, book is written by Tom with 1025 pricing at 856

# >>> b1 with __repr__ magic method:Title = Go man, Author = Harry, Pages = 452, Price = 890
# >>> b2 with __repr__ magic method:Title = Go girl, Author = Tom, Pages = 1025, Price = 856
