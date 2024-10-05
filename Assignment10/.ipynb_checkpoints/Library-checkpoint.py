class Book:
    """This class contains information about some books"""
    
    def __init__(self, title, author, year, price, stoplist, genre):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist
        self.genre = genre
    def get_info(self):
        return (f"We know that about this book: {self.author}, {self.title}, {self.year}, {self.price}, {self.stoplist}")
    def most_expensive(self, prices):
        most_exp = None
        price_most_exp = 0
        for i in prices:
            if i.price > price_most_exp:
                price_most_exp = i.price
                most_exp = i
        if most_exp is not None:
            return f"The most expensive book in the list is {most_exp.title} by {most_exp.author}"
        else:
            return "You provided an empty list in your input. Please, denote the prices"
    def set_stoplist(self, boolean):
        self.stoplist = boolean
    def censor(self, author_name, boolean):
        if author_name == self.author:
            self.set_stoplist(boolean)