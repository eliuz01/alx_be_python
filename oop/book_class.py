class Book:
    def __init__(self, title, author, year):
        # Initialize the book with title, author, and year
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        # Destructor: Print a message when the book object is deleted
        print(f"Deleting {self.title}")

    def __str__(self):
        # String representation for informal use
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        # Official string representation that could recreate the object
        return f"Book('{self.title}', '{self.author}', {self.year})"
