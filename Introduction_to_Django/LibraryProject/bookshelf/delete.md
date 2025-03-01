## **delete.md**

```markdown
# Delete Operation

**Objective:** Delete the book with the updated title and confirm the deletion.

**Command:**

```python
from book_store.models import Book

# Retrieve the Book instance with the updated title
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the Book instance
book.delete()

# Confirm deletion by retrieving all books
books = Book.objects.all()

#expected output
# <QuerySet []>