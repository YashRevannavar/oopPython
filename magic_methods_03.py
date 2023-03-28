# Understanding __getattribute__ and __setattr__ Magic Methods

class Book:
    """
    The Book class represents a book with its attributes such as title, price, author, and pages.
    It has three methods:
    """

    def __init__(self, title, author, price) -> None:
        """
        __init__(self, title, author) - initializes the object of class Book with 
        the given parameters: title, price, author.
        """
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1

    def __str__(self) -> str:
        """
        __str__(self) - returns a formatted string representation of 
        the Book object that contains information such as title, author and price.
        """
        return f"{self.title}, book is written by {self.author} pricing at {self.price}"

    def __getattribute__(self, name: str):
        """
        __getattribute__(self, name: str) - is called when an attribute of a Book object is accessed.
        This method checks if the attribute is "price". If it is, it gets the price using 
        super().__getattribute__("price"), and also gets the discount using 
        super().__getattribute__("_discount"). It returns the discounted price by subtracting the 
        discount from the price. If the attribute is not "price",
        it returns the value of the attribute using super().__getattribute__(name).
        """
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    def __setattr__(self, name, value) -> None:
        """
        __setattr__(self, name, value) -> None - is called when an attribute of Book object is set. 
        This method checks if the attribute being set is "price". If it is, it checks if the value 
        being set is a float. If it's not a float, a ValueError is raised. If the attribute is not 
        "price", the value is set using super().__setattr__(name,value).
        """
        if name == "price":
            if type(value) is not float:
                raise ValueError("The price attr must be a float")
        return super().__setattr__(name, value)

# Deceleration of b1 and b2
b1 = Book("Go man", "Harry", 452.03)
b2 = Book("Go girl", "Tom", 1025.00)

# Observing __getattribute__ and __setattr__:
b1.price = float(423)
print(f"{b1}")

# Outputs:
# Go man, book is written by Harry pricing at 380.7
