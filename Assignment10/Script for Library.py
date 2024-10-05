import Library as lib
my_books = []
my_books.append (lib.Book("Leviathan", "Hobbes", 1651, 2000, False, "philosophy"))
my_books.append (lib.Book("De Coelesti Hierarchia", "Dionysius the Areopagite", 500, 4000, True, "religion"))
my_books.append (lib.Book("Summa Theologica", "Thomas Aquinas", 1274, 5000, False, "religion"))
my_books.append (lib.Book("Anecdota", "Procopius Caesariensis", 558, 1000, True, "history"))
my_books.append (lib.Book("Confessiones", "Augustine of Hippo", 400, 6000, False, "philosophy, religion"))
my_books.append (lib.Book("Antiquitates Iudaicae", "Flavius Josephus", 94, 7000, True, "history"))
my_books.append (lib.Book("Omnia Hebraicolatina", "Flavius Josephus", 75, 8000, False, "history"))
my_books.append (lib.Book("Patrologia Graeca", "Church Fathers", 1857, 4000, True, "religion"))
my_books.append (lib.Book("De consolatione philosophiae", "	Boethius", 524, 3000, False, "philosophy"))
#censor(author_name, boolean) method
my_books[0].censor("Hobbes", False)
my_books[0].stoplist
#censor(author_name, boolean) method
my_books[1].censor("Justinian", True)
my_books[1].stoplist
#censor(author_name, boolean) method
my_books[2].censor("Thomas Aquinas", False)
my_books[2].stoplist
#set_stoplist(boolean) method
my_books[0].set_stoplist(True)
my_books[0].stoplist
#set_stoplist(boolean) method
my_books[1].censor(False)
my_books[1].stoplist
#set_stoplist(boolean) method
my_books[2].censor(True)
my_books[2].stoplist
#get_info() method
my_books[0].get_info()
#get_info() method
my_books[1].get_info()
#get_info() method
my_books[2].get_info()
#most_expensive() method
my_books[0].most_expensive(my_books)