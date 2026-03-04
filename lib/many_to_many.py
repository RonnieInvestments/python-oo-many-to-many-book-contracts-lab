class Author:
    # The list will store all Author objects created
    all = []

    def __init__(self, name):
        self.name = name # Attribute to store author's name
        Author.all.append(self) # Add author object to Author.all

    def contracts(self):
        # return all contracts that belong to this author
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        # return all books written by this author (no duplicates)
        return list({contract.book for contract in self.contracts()})

    def sign_contract(self, book, date, royalties):
        # create and return a new Contract object
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        # Add up all royalties from this author's contracts
        return sum(contract.royalties for contract in self.contracts())


class Book:
    # Store all book objects created
    all = []

    def __init__(self, title):
        self.title = title # Save book title
        Book.all.append(self) # Add this book object to the Book all

    def contracts(self):
        # All contracts that belong to this book
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        # All connected authors
        return list({contract.author for contract in self.contracts()})


class Contract:
    # Store all Contract objects
    all = []

    def __init__(self, author, book, date, royalties):
        # Set values using property setters -> validation purposes
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)

    # Get the author
    @property
    def author(self):
        return self._author

    # Set the author -> with validation
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value

    # Get the book
    @property
    def book(self):
        return self._book

    # Set the book
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value

    # Get the date
    @property
    def date(self):
        return self._date

    # Set the date
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value

    # Get the royalties
    @property
    def royalties(self):
        return self._royalties

    # Set the royalties
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value

    # Class Method 
    @classmethod
    def contracts_by_date(cls, date):
        # Return all contracts that match the given date
        return [contract for contract in cls.all if contract.date == date]