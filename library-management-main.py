import random

# -------------------------------------------------------------------
# MAIN DATA STORE
# -------------------------------------------------------------------
# Using a list to store all the books.
# Each book is stored as a tuple:
# (book_id, title, author, copies)
library = []

# -------------------------------------------------------------------
# FUNCTION: Add a New Book
# -------------------------------------------------------------------
def add_book():
    # Taking details from the user
    title = input("Enter book title: ").strip().title()
    author = input("Enter author name: ").strip().title()
    copies = int(input("Enter number of copies: "))

    # Generating a random book ID like B2345
    book_id = "B" + str(random.randint(1000, 9999))

    # Creating a book tuple
    book = (book_id, title, author, copies)

    # Adding it to the library list
    library.append(book)

    print(f"Book '{title}' added successfully.\n")


# -------------------------------------------------------------------
# FUNCTION: Search Book by Title
# -------------------------------------------------------------------
def search_by_title():
    title = input("Enter title to search: ").strip().title()

    # Filtering books where book[1] (title) matches the user input
    found = list(filter(lambda b: b[1] == title, library))

    if found:
        for b in found:
            print(f"{b[1]} by {b[2]} (Copies: {b[3]})")
    else:
        print("No book found with that title.\n")


# -------------------------------------------------------------------
# FUNCTION: Count Books by Specific Author
# -------------------------------------------------------------------
def count_by_author():
    author = input("Enter author name: ").strip().title()

    # Counting how many books match b[2] (author)
    count = len(list(filter(lambda b: b[2] == author, library)))

    print(f"Total books by {author}: {count}\n")


# -------------------------------------------------------------------
# FUNCTION: Check Availability of a Book
# -------------------------------------------------------------------
def check_availability():
    title = input("Enter book title to check availability: ").strip().title()

    # Search for book with matching title
    found = list(filter(lambda b: b[1] == title, library))

    if found:
        # b[3] = number of copies
        if found[0][3] > 0:
            print("Book is Available.\n")
        else:
            print("Book is Unavailable.\n")
    else:
        print("Book not found.\n")


# -------------------------------------------------------------------
# FUNCTION: Display All Books
# -------------------------------------------------------------------
def display_books():
    if not library:
        print("No books in library.\n")
        return

    print("\nList of Books:")
    print("-" * 40)
    for b in library:
        print(f"{b[0]} | {b[1]} | {b[2]} | Copies: {b[3]}")
    print("-" * 40, "\n")


# -------------------------------------------------------------------
# FUNCTION: Summary of Library
# -------------------------------------------------------------------
def summary():
    if not library:
        print("No books to summarize.\n")
        return

    total = len(library)  # total number of book records
    available = len(list(filter(lambda b: b[3] > 0, library)))
    unavailable = total - available

    # Extract list of copy counts
    copies = list(map(lambda b: b[3], library))

    print("\n--- Library Summary ---")
    print(f"Total number of books: {total}")
    print(f"Books available: {available}")
    print(f"Books unavailable: {unavailable}")
    print(f"Highest number of copies: {max(copies)}")
    print(f"Lowest number of copies: {min(copies)}")

    # Counting books per author
    authors = list(set(map(lambda b: b[2], library)))
    print("\nAuthor-wise book count:")
    for a in authors:
        count = len(list(filter(lambda b: b[2] == a, library)))
        print(f"{a}: {count}")

    # Sorted list of books by title
    sorted_books = sorted(library, key=lambda b: b[1])
    print("\nSorted List of Books (by Title):")
    for b in sorted_books:
        print(f"{b[1]} ({b[0]}) - {b[2]}, Copies: {b[3]}")
    print("-" * 40, "\n")


# -------------------------------------------------------------------
# MAIN MENU (Using While Loop Instead of Recursion)
# -------------------------------------------------------------------
def menu():
    while True:
        print("====== Library Menu ======")
        print("1. Add Book")
        print("2. Search by Title")
        print("3. Count by Author")
        print("4. Check Availability")
        print("5. Display All Books")
        print("6. Summary")
        print("7. Exit")
        print("==========================")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            search_by_title()
        elif choice == '3':
            count_by_author()
        elif choice == '4':
            check_availability()
        elif choice == '5':
            display_books()
        elif choice == '6':
            summary()
        elif choice == '7':
            print("Exiting Library System.")
            break
        else:
            print("Invalid choice.\n")


# -------------------------------------------------------------------
# PROGRAM START
# -------------------------------------------------------------------
print("Welcome to the Library Book Management System\n")
menu()
