from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=225)




    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=225,default="Default Title")
    publication_year= models.IntegerField(null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)