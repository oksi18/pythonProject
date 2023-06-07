# 1


class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __add__(self, other):
        self.other = other
        if isinstance(other, Rectangle):
            return self.area() + other.area()

    def __sub__(self, other):
        self.other = other
        if isinstance(other, Rectangle):
            return self.area() - other.area()

    def __eq__(self, other):
        self.other = other
        if isinstance(other, Rectangle):
            return self.area() == other.area()

    def __ne__(self, other):
        self.other = other
        if isinstance(other, Rectangle):
            return self.area() != other.area()

    def __lt__(self, other):
        self.other = other
        if isinstance(other, Rectangle):
            return self.area() < other.area()

    def __gt__(self, other):
        self.other = other
        if isinstance(other, Rectangle):
            return self.area() > other.area()

    def __len__(self):
        return self.x + self.y


rec1 = Rectangle(2, 7)
rec2 = Rectangle(5, 9)

print(rec1 + rec2)
print(rec1 - rec2)
print(rec1 == rec2)
print(rec1 != rec2)
print(rec1 > rec2)
print(rec1 < rec2)
print(len(rec1))
print(len(rec2))

# 2
from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    count = 0

    def __init__(self, name, age, foot):
        super().__init__(name, age)
        self.foot = foot
        Cinderella.count += 1

    def get(cls):
        return cls.count


class Prince(Human):
    def __init__(self, name, age, footSize):
        super().__init__(name, age)
        self.footSize = footSize

    def find_cinderellas(self, cinderellas):
        for cinderella in cinderellas:
            if cinderella.foot == self.footSize:
                return cinderella


cinderella1 = Cinderella("Maria", 18, 36)
cinderella2 = Cinderella("Kate", 19, 38)
cinderella3 = Cinderella("Kate", 19, 37)

print(Cinderella.get(Cinderella))

prince = Prince("Kokos", 22, 36)
find = prince.find_cinderellas([cinderella1, cinderella2])

if find:
    print("Cinderella:", find.name, find.age, find.foot)
else:
    print("Cinderella not found")


# 3
class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("Book:", self.name)


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print("Magazine:", self.name)


class Main():
    printable_list = []

    @classmethod
    def add(cls, other):
        if isinstance(other, (Book, Magazine)):
            cls.printable_list.append(other)
        else:
            print("Ignore")

    @classmethod
    def show_all_magazines(cls):
        for magazine in cls.printable_list:
            if isinstance(magazine, Magazine):
                magazine.print()

    @classmethod
    def show_all_books(cls):
        for book in cls.printable_list:
            if isinstance(book, Book):
                book.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 40)
Main.show_all_books()

