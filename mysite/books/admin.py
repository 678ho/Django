from django.contrib import admin
from books.models import Books, Author, Publisher
# Register your models here.
admin.site.register(Books)
admin.site.register(Author)
admin.site.register(Publisher)