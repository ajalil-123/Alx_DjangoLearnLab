
# Create Operation

**Objective:** Create a Book instance with the title "1984", author "George Orwell", and publication year "1949-06-08".

**Command:**

```python
from bookshelf.models import Book

# Create the Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year="1949"  
)

**expected output**
# <Book: 1984>