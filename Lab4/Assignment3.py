'''Question 1: Create a Python program that manages a list of books available 
in the library by performing operations such as creating, adding, removing, 
and displaying book titles.
a.	Create a list of book titles: ["The Alchemist", "1984", "The Kite Runner", "Pride and Prejudice"].
b.	Add two more books to the list using append().
c.	Remove one book that has been damaged using remove().
d.	Sort the list alphabetically and display the final list using sort().'''

books = ["The Alchemist", "1984", "The Kite Runner", "Pride and Prejudice"]

print("Original list:")
print(books)

books.append("To Kill a Mockingbird")
books.append("The Great Gatsby")

print("\nAfter adding two books:")
print(books)

books.remove("1984")

print("\nAfter removing damaged book:")
print(books)

books.sort()

print("\nFinal list:")
print(books)



'''
Question 2: Write a Python code snippet that creates a tuple to store one borrower’s immutable personal details.
a.	Create a tuple, e.g., ("John Doe", "B1023", "2025-10-15") representing a borrower’s name, library ID, and membership date.
b.	Modify one element in the tuple, observe the result, and discuss your observation.
c.	Print the length of the tuple using the len() function to show how many data fields it contains and display each element using a loop.

'''

borrower = ("John Doe", "B1023", "2025-10-15")

print("Borrower details:")
print(borrower)

try:
    borrower[0] = "Sanjeev"
except TypeError as te:
    print("\nModification error:")
    print(te)

print("\nLength of tuple:")
print(len(borrower))

print("\nBorrower details using loop:")
for detail in borrower:
    print(detail)
    
    
'''
Question 3: Perform tuple packing and unpacking in a Python program to demonstrate how book information can be stored and accessed efficiently.
a.	Pack a book title, author, and publication year into a tuple called book_info.
b.	Unpack the tuple into separate variables and print them in a readable format (for example: “Title: The Alchemist”).
c.	Explain how tuple packing and unpacking make code more organized and easier to understand.

'''

book_info = ("The Alchemist", "Paulo Coelho", 1988)

print("Packed tuple:")
print(book_info)

title, author, year = book_info

print("\nBook Information:")
print("Title:", title)
print("Author:", author)
print("Publication Year:", year)


'''Question 4: Use indexing and slicing to manage weekly borrowing statistics.
a.	Given a list borrowed_books = [23, 19, 31, 27, 22, 30, 25] representing the number of books borrowed each week, extract the records from week 2 to week 5 using slicing.
b.	Replace the number of books borrowed in week 1 with 20 using indexing.
c.	Display the updated list and the sliced portion.

'''

borrowed_books = [23, 19, 31, 27, 22, 30, 25]

print("Original list:")
print(borrowed_books)

week_2_to_5 = borrowed_books[1:5]

borrowed_books[0] = 20

print("\nBooks borrowed from week 2 to week 5:")
print(week_2_to_5)

print("\nUpdated list:")
print(borrowed_books)



