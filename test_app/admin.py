from django.contrib import admin

from test_app.models import Book, Author

admin.site.register(Book)
admin.site.register(Author)
