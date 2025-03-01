
## **retrieve.md**

```markdown
# Retrieve Operation

**Objective:** Retrieve and display all attributes of the book created in the previous step.

**Command:**

```python
from book_store.models import Book

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