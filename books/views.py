from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count, F
from .models import Book, BookPage

def dashboard_view(request):
    q = request.GET.get('q', '').strip()
    selected_category = request.GET.get('category', '').strip()
    books = Book.objects.all().order_by('-id')

    if q:
        books = books.filter(Q(title__icontains=q) | Q(author__icontains=q) | Q(description__icontains=q))
    if selected_category:
        books = books.filter(category=selected_category)

    categories = Book.objects.values('category').annotate(count=Count('id')).order_by('category')
    top_books = Book.objects.order_by('-views_count', '-id')[:3]

    return render(request, "books/dashboard.html", {
        "books": books,
        "categories": categories,
        "selected_category": selected_category,
        "top_books": top_books,
        "q": q,
        "total_books": Book.objects.count(),
    })

def book_detail_view(request, pk):
    Book.objects.filter(pk=pk).update(views_count=F('views_count') + 1)
    book = get_object_or_404(Book, pk=pk)
    pages = book.book_pages.all()
    page_param = request.GET.get('page')
    page_num = int(page_param) if page_param and page_param.isdigit() else 1

    current_page = pages.filter(page_num=page_num).first() or pages.first()
    cur_num = current_page.page_num if current_page else 1
    total_count = pages.count()

    return render(request, "books/detail.html", {
        "book": book,
        "page": current_page,
        "current_page_num": cur_num,
        "total_pages": total_count,
        "prev_page": cur_num - 1 if cur_num > 1 else None,
        "next_page": cur_num + 1 if cur_num < total_count else None,
        "all_pages": pages,
    })
