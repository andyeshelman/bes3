import shutil

def line_break():
    terminal_width = shutil.get_terminal_size().columns
    line = '=' * terminal_width
    print(line)

# Implementing a Book Inventory Linked List in Python

# Objective: The aim of this assignment is to reinforce understanding
# of the linked list data structure and its implementation in Python.

# Problem Statement: You are tasked with building an inventory management system for a bookstore.
# The system should allow adding new books to the inventory and removing books based on their ISBN.
# You'll implement this system using a linked list data structure.

# Task 1
#   Create a class named Book with attributes for title, author, genre, ISBN, and quantity.

# Task 2
#   Create a class named Node to represent nodes in the linked list. Each node will store a book object.

# Task 3
#   Implement a class named InventoryManager to manage the inventory using a linked list.

# Task 4
#   Implement the following methods in the **`InventoryManager`** class:
#       add_book(title, author, genre, isbn, quantity): Adds a new book to the inventory.
#       remove_book(isbn): Removes a book from the inventory based on its ISBN.
#       display_inventory(): Displays the current inventory.

class Book:
    def __init__(self, title, author, genre, isbn, quantity):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.quantity = quantity

    def __str__(self):
        return f"{self.title} by {self.author}\n\t{self.genre}, {self.isbn}\n\t{self.quantity} available"
    
class Node:
    def __init__(self, book):
        self.book = book
        self.next = None
    
    def __str__(self):
        return str(self.book)
    
class Inventory:
    def __init__(self):
        self.head = None

    def __iter__(self):
        def gen():
            current = self.head
            while current:
                yield current
                current = current.next
        return gen()

    def add_book(self, title, author, genre, isbn, quantity):
        new_node = Node(Book(title, author, genre, isbn, quantity))
        new_node.next = self.head
        self.head = new_node
    
    def remove_book(self, isbn_to_del):
        """Raises ValueError if isbn not found"""
        try:
            if self.head.book.isbn == isbn_to_del:
                self.head = self.head.next
                return
            for node in self:
                if node.next.book.isbn == isbn_to_del:
                    node.next = node.next.next
                    return
        except AttributeError: # None has no attribute `book`
            raise ValueError
        
    def display(self):
        for node in self:
            line_break()
            print(node)

books = Inventory()
# books.remove_book(7) # ValueError
books.add_book("Cat's Cradle", "Kurt Vonnegut", "Sci-Fi", 1010101, 3)
books.add_book("Snow Crash", "Neal Stephenson", "Sci-Fi", 2020202, 3)
books.add_book("The Magicians", "Lev Grossman", "Fantasy", 3030303, 3)
books.add_book("Pirc Alert!", "Alexander Chernin and Lev Alburt", "Nonfiction", 4040404, 3)
#books.display()
books.remove_book(3030303)
# books.remove_book(3030303) # ValueError
books.display()