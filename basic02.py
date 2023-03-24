# Understanding class inheritance

class Publications:
    """
    This class will be inherited in the Periodical class.
    As the Title and the price will be constant in the Books, Magazine and Newspaper classes.
    """
    def __init__(self, title, price) -> None:
        self.title = title
        self.price = price

class Periodical(Publications):
    """
    This class will be inherited in the Books, Magazine and Newspaper classes.
    As the period and the publisher will be constant in the Magazine and Newspaper classes.
    This class also inherits Publication as a super class as it has title and price attributes.
    """
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publications):
    """
    This is a Book class inherits Publication class as it needs only title and price.
    Also has its independent attributes such as author and pages. 
    """
    def __init__(self, title, price, author, pages) -> None:
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Periodical):
    """
    This is a Magazine class inherits Periodical class as it needs all the attributes.
    """
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price, period, publisher)

class Newspaper(Periodical):
    """
    This is a Newspaper class inherits Periodical class as it needs all the attributes.
    """
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price, period, publisher)

# Deceleration of the classes.
b1 = Book("Raven Claw", 2569, "John Wick", 2548)
m1 = Magazine("Red Lines", 879, "monthly","Rote Linien")
n1 = Newspaper("The Rise", 23, "daily", "Der Aufgang")

# Observing classes.
print(f">>> Book b1: Title:{b1.title}, author: {b1.author}, pages: {b1.pages}, price: {b1.price}")
print(f">>> Magazine m1: Title:{m1.title}, publisher: {m1.publisher}, period: {m1.period}, price: {m1.price}")
print(f">>> Newspaper n1: Title:{n1.title}, publisher: {n1.publisher}, period: {n1.period}, price: {n1.price}")
