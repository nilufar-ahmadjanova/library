from django.urls import path
from .views import dashboard_view, book_detail_view

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('book/<int:pk>/', book_detail_view, name='book_detail'),
]
