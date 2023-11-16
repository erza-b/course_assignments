#Task 2

#Library

#Write a class structure that implements a library. Classes:

#1) Library - name, books = [], authors = []

#2) Book - name, year, author (author must be an instance of Author class)

#3) Author - name, country, birthday, books = []

#Library class

#Methods:

#- new_book(name: str, year: int, author: Author) - returns an instance of Book class and adds the book to the books list for the current library.

#- group_by_author(author: Author) - returns a list of all books grouped by the specified author

#- group_by_year(year: int) - returns a list of all the books grouped by the specified year

#All 3 classes must have a readable __repr__ and __str__ methods.

class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __repr__(self):
        return f"Author('{self.name}', '{self.country}', '{self.birthday}')"

    def __str__(self):
        return f"Author: {self.name}, Country: {self.country}, Birthday: {self.birthday}"


class Book:
    def __init__(self, name, year, author):
        self.name = name
        self.year = year
        self.author = author
        author.books.append(self)

    def __repr__(self):
        return f"Book('{self.name}', {self.year}, {repr(self.author)})"

    def __str__(self):
        return f"Book: {self.name}, Year: {self.year}, Author: {self.author.name}"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def new_book(self, name, year, author):
        new_book = Book(name, year, author)
        self.books.append(new_book)
        return new_book

    def group_by_author(self, author):
        return [book for book in self.books if book.author == author]

    def group_by_year(self, year):
        return [book for book in self.books if book.year == year]

    def __repr__(self):
        return f"Library('{self.name}')"

    def __str__(self):
        return f"Library: {self.name}"

    