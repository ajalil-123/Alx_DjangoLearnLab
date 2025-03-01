
# Create Operation

**Objective:** Create a Book instance with the title "1984", author "George Orwell", and publication year "1949-06-08".

**Command:**

```python
from bookshelf.models.models import Book

# Create the Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year="1949"  
)

**expected output**
# <Book: 1984>


## **retrieve.md**

```markdown
# Retrieve Operation

**Objective:** Retrieve and display all attributes of the book created in the previous step.

**Command:**

```python
from bookshelf.models import Book

# Retrieve the Book instance with title "1984"
book = Book.objects.get(title="1984")

# Display all attributes of the retrieved book
print("Title:", book.title)
print("Author:", book.author)
print("Published year:", book.publication_year)

#Expected output
#Title: 1984
#Author: George Orwell
#Published year: 1949


## **update.md**

```markdown
# Update Operation

**Objective:** Update the title of the book from "1984" to "Nineteen Eighty-Four".

**Command:**

```python
from book_storebookshelf.models import Book

# Retrieve the Book instance with title "1984"
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()  # Save the changes to the database

# Retrieve the updated book to verify the change
updated_book = Book.objects.get(id=book.id)
print("Updated Title:", updated_book.title)

# output for the updated command
# Updated Title: Nineteen Eighty-Four





## **delete.md**

```markdown
# Delete Operation

**Objective:** Delete the book with the updated title and confirm the deletion.

**Command:**

```python
from bookshelf.models import Book

# Retrieve the Book instance with the updated title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the Book instance
book.delete()

# Confirm deletion by retrieving all books
books = Book.objects.all()

#expected output
# <QuerySet []>
