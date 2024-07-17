class Books:
    total_books = 0
    lend_by = ""

    def __init__(self, title, author, availability=True):
        self.Title = title
        self.Author = author
        self.Available = availability

    @classmethod
    def increment_book_count(cls):
        cls.total_books += 5

    @classmethod
    def get_total_books(cls):
        return cls.total_books

    def display_details(self):
        print(f"Book info: {self.Title}, {self.Author}, {self.Available}")

    @classmethod
    def borrowed_by(cls, student):
        cls.lend_by = student
        return cls.lend_by

    @staticmethod
    def is_available(books):
        return books.Available


book1 = Books("Hunger Games","Stephen Jackson")
book2 = Books("1984", "George Orwell", False)
book3 = Books("To Kill a Mockingbird", "Harper Lee")

# book2.display_details()
# book3.display_details()

book1.display_details()
print(f"is {book1.Title} available? {'Yes' if Books.is_available(book1) else 'no'}\n"
      f"Borrowed by {book1.borrowed_by("Kallen")}")
