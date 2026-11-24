from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="Kitob nomi")
    author = models.CharField(max_length=150, verbose_name="Muallif")
    category = models.CharField(max_length=100, verbose_name="Janr")
    pages = models.PositiveIntegerField(default=0, verbose_name="Sahifalar")
    year = models.PositiveIntegerField(default=2024, verbose_name="Yili")
    description = models.TextField(blank=True, verbose_name="Tavsif")
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True, verbose_name="Muqova rasmi")
    cover_color = models.CharField(max_length=50, default="from-blue-600 to-indigo-800")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Mutolaalar soni")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

class BookPage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_pages')
    page_num = models.PositiveIntegerField(verbose_name="Sahifa raqami")
    chapter = models.CharField(max_length=150, blank=True, verbose_name="Bob nomi")
    content = models.TextField(verbose_name="Sahifa matni")

    class Meta:
        ordering = ['page_num']
        unique_together = ('book', 'page_num')

    def __str__(self):
        return f"{self.book.title} - {self.page_num}-bet"
