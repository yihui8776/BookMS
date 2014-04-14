from django.contrib import admin
from bookapp.models import *
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ('isbn', 'title')

admin.site.register(Book)