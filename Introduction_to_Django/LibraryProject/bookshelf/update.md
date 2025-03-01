
## **update.md**

```markdown
# Update Operation

**Objective:** Update the title of the book from "1984" to "Nineteen Eighty-Four".

**Command:**

```python
from bookshelf.models import Book

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