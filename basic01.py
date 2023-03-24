class Book():
    """
    This is a Book class for the practice of the OOP.
    """
    BOOK_TYPE = ("Hardcover","Paperback","Comic","eBook")
    __book_list = None # private variable.
    @classmethod # Class Method
    def get_book_type(cls):
        """
        This classmethod returns BOOK_TYPE's values
        """
        return cls.BOOK_TYPE

    @staticmethod
    def get_book_list():
        """
        This staticmethod returns a list of books and appends if any new variant of books is created
        """
        if not Book.__book_list:
            Book.__book_list = []
        return Book.__book_list

    def __init__(self ,title ,author, pages, price, book_type) -> None:
        """
        This is a Book class with self ,title ,author, pages, price attribute.
        """
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        if not book_type in Book.BOOK_TYPE:
            raise ValueError(f"{book_type} is not a valid book type.\nChoose any one of the {Book.BOOK_TYPE}")
        else:
            self.book_type = book_type

    def get_price(self):
        """
        This is a get_price method which calculates the discount when the _discount attribute is 
        available or else returns the same value.
        """
        if hasattr(self,"_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self,amount):
        """
        This is a set_discount method which collects the discount in the range of [0.00 - 1.00].
        """
        self._discount = amount


class Newspaper():
    """
    This is a Newspaper class with just name attribute.
    """
    def __init__(self,name) -> None:
        self.name = name

# Deceleration of the classes.
b1 = Book("Go man","Harry",890,452,"Hardcover")
b2 = Book("Go girl","Tom",856,1025,"Comic")
n1 = Newspaper("The rise")
n3 = Newspaper("The Empire")

# class attribute
print(f"\n>>> Class attribute: {Book.get_book_type()}\n") # Class Method
THE_BOOKS = Book.get_book_list()
THE_BOOKS.append(b1.title)
THE_BOOKS.append(b2.title)
print(f">>> The books list using static method: {THE_BOOKS}\n")


# Observing the b1 class.
print(f">>> Class b1: {b1}")
print(f">>> Title: {b1.title}")
print(f">>> Author: {b1.author}")
print(f">>> Pages: {b1.pages}")
print(f">>> Price: {b1.price}")
priceB1 = b1.get_price()
print(f">>> Price with get_price: {priceB1}")
b1.set_discount(.50)
print(f">>> Price with get_price with discount: {b1.get_price()}\n")

# Observing the b2 class.
print(f">>> Class b2: {b2}")
print(f">>> Class type: {type(b2)}\n")

# isinstance function:
print(f">>> if b1 is a book class: {isinstance(b1,Book)}")
print(f">>> if n1 is a book class: {isinstance(n1,Book)}")
print(f">>> if n1 is a Newspaper class: {isinstance(n1,Newspaper)}")
