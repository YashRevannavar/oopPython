# Understanding eq and ge Magic Methods:

class Book:
    """
    The Book class represents a book with its attributes such as title, price, author, and pages.
    It has three methods:
    """

    def __init__(self, title, author, price) -> None:
        """
        __init__(self, title, author) - initializes the object of class Book with 
        the given parameters: title, price, author, and pages.
        """
        self.title = title
        self.author = author
        self.price = price

    def __eq__(self, value: object) -> bool:
        """
        __eq__(self, value: object) -> bool) - compares the given value object to the Book object
        and returns True if the two objects have the same title, author, and price.
        If the value object is not an instance of Book, a ValueError is raised.
        """
        if not isinstance(value, Book):
            raise ValueError("Can't compare Book to a non-Book")
        return (self.title == value.title and
                self.author == value.author and
                self.price == value.price)

    def __ge__(self, value: object) -> bool:
        """
        __ge__(self, value: object) -> bool - compares the given value object to the Book object and
        returns True if the price of the Book object is greater than or equal to the price of the 
        value object. If the value object is not an instance of Book, a ValueError is raised.
        """
        if not isinstance(value, Book):
            raise ValueError("Can't compare Book to a non-Book")
        return self.price >= value.price

    def __lt__(self, value: object) -> bool:
        """
        __lt__(self, value: object) -> bool - compares the given value object to the Book object and
        returns True if the price of the Book object is less than the price of the value object.
        If the value object is not an instance of Book, a ValueError is raised.
        """
        if not isinstance(value, Book):
            raise ValueError("Can't compare Book to a non-Book")
        return self.price < value.price


# Deceleration of b1, b2 and b3
b1 = Book("Go man", "Harry", 123)
b2 = Book("Go man", "Harry", 123)
b3 = Book("Go girl", "Tom", 145)
b4 = Book("Go baby", "Doc", 1405)

# Sorting of books [only possible if the method __lt__ is present is class]
books = [b3, b2, b4, b1]
books.sort()

# Observing __eq__ and __ge__:
print(f">>> Checking if the b1 is equal to b2:: {b1==b2}")
print(f">>> Checking if the b1 is equal to b3: {b1==b3}")
print(
    f">> Checking if the b1.price is greater than or equal to b3.price: {b1 >= b3}\n")
print(f">>> Sorted titles for the books: {[book.title for book in books]}")
print(f">>> Sorted prices for the books: {[book.price for book in books]}")

# Outputs:
# >>> Checking if the b1 is equal to b2:: True
# >>> Checking if the b1 is equal to b3: False
# >> Checking if the b1.price is greater than or equal to b3.price: False

# >>> Sorted titles for the books: ['Go man', 'Go man', 'Go girl', 'Go baby']
# >>> Sorted prices for the books: [123, 123, 145, 1405]
