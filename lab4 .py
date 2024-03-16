# Initialize empty lists, set,and dictionary
books_list = []
authors_set = set()
books_dict = {}

# Add books
books_list.append("python programming")
authors_set.add("John smith")
books_dict["python programming"] = "John smith"

books_list.append("Data structures and Algorithms")
authors_set.add("Jane Doe")
books_dict["Data structures and Algorithms"] = "Jane Doe"

books_list.append("Machine learning basics")
authors_set.add("Alice Johnson")
books_dict["Machine learning basics"] = "Alice Johnson"

# search for a books
search_title = input("Enter the title of the book to search: ")
if search_title in books_list:
    print(f"book found! Author:{books_dict[search_title]}")
else:
    print("Book not found!")

    # Display all the books
    print("list of books:")
    for book in books_list:
        print (book)

# Remove a book
remove_title = input("Enter the title of the book to remove or elese inter to skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    authors_set.remove(remove_author)
    del books_dict[remove_title]
    print("Book removed succesfully!")
    print("Books available: ",books_list)
else:
    print("book not found!")
