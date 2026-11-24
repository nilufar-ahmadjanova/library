from django.contrib import admin
from .models import Book, BookPage

class BookPageInline(admin.TabularInline):
    model = BookPage
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'year', 'pages')
    search_fields = ('title', 'author')
    inlines = [BookPageInline]

@admin.register(BookPage)
class BookPageAdmin(admin.ModelAdmin):
    list_display = ('book', 'page_num', 'chapter')
    list_filter = ('book',)
