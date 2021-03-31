from django.contrib import admin
from .models import Books, Readers, Donor

# Register your models here.

class BooksAdmin(admin.ModelAdmin):
    list_display = ('ISBN_NUM','BOOKS_NAME','AVAILABLE_COPIES')

admin.site.register(Books, BooksAdmin)
admin.site.register(Readers)
admin.site.register(Donor)
