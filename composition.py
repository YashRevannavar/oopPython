# Understanding concept of composition in object-oriented programming.

class Books:
    """
    The Books class represents a book with its attributes such as title, price, author
    and a list of chapters. It has three methods.
    """
    def __init__(self, title, price, author=None) -> None:
        """
        __init__(self, title, price, author=None) - initializes the object of class Books with 
        the given parameters: title, price, and author (optional). It also initializes an 
        empty list of chapters.
        """
        self.title = title
        self.price = price
        self.author = author
        self.chapters = []

    def add_chapters(self, chapter):
        """
        add_chapters(self, chapter) - adds the given chapter object to the list of chapters 
        for the Books object.
        """
        self.chapters.append(chapter)

    def get_page_count(self):
        """
        get_page_count(self) - returns the total number of pages in the book by adding up the 
        number of pages of each chapter in the list of chapters.
        """
        result = 0
        for chap in self.chapters:
            result += chap.page_count
        return result

class Author:
    """
    The Author class represents an author with its attributes such as first_name and last_name.
    It has one method:    
    """
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        """
        __str__(self) - returns a formatted string representing the first name and last name 
        of the author.
        """
        return f"First name is {self.first_name}\nLast name is {self.last_name}"

class Chapter:
    """
    The Chapter class represents a chapter with its attributes such as name and page_count.
    It has one method:
    """
    def __init__(self, name, page_count) -> None:
        """
        __init__(self, name, page_count) - initializes the object of class Chapter with the 
        given parameters: name and page_count.
        """
        self.name = name
        self.page_count = page_count

auth =  Author("Yash","Revannavar")
b1 = Books("Oops Python",896,auth)
b1.add_chapters(Chapter("Introduction", 40))
b1.add_chapters(Chapter("Chapter 1", 89))
b1.add_chapters(Chapter("Chapter 2", 189))
b1.add_chapters(Chapter("Chapter 3", 291))


print(f"{auth}")
print(f">>> Total number of pages in b1: {b1.get_page_count()}")


# Output:
# First name is Yash
# Last name is Revannavar
# >>> Total number of pages in b1: 609