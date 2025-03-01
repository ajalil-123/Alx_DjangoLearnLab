from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    # Display fields in the admin list view
    list_display = ('title', 'author', 'publication_year')

    # Add filter options for publication_year and author
    list_filter = ('publication_year', 'author')

    # Enable search functionality for title and author fields
    search_fields = ('title', 'author')

    # Enable ordering by published date
    ordering = ('publication_year',)

    # Enable pagination (Optional)
    list_per_page = 20



# Register your models here.
admin.site.register(Book)