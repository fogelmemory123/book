from .models import Book,Genre,Author
from django.contrib import admin

# רישום מודלים לפאנל האדמין

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
