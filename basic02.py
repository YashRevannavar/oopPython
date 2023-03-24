# Understanding class inheritance

class Publications:
    def __init__(self, title, price) -> None:
        self.title = title
        self.price = price

class Periodical(Publications):
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher

class Book(Publications):
    def __init__(self, title, price, author, pages) -> None:
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Periodical):
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price, period, publisher)

class Newspaper(Periodical):
    def __init__(self, title, price, period, publisher) -> None:
        super().__init__(title, price, period, publisher)
