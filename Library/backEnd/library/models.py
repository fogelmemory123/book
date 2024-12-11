from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Author)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()



    def clean(self):
        from django.core.exceptions import ValidationError
        if self.rating < 1 or self.rating > 5:
            raise ValidationError("Rating must be between 1 and 5.")

    def __str__(self):
        return self.title


# Create your models here.
