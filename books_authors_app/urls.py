from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),	  
    path('addbook', views.add_book),
    path('books/<int:id>', views.book_dis, name='book_page'),
    path('addaurthorto/<int:id>', views.add_aurthor_to),
    path('authors', views.auth_index),
    path('addauthor',views.add_author),
    path('authors/<int:id>', views.author_dis, name='author_page'),
    path('addbookto/<int:id>', views.add_book_to),
]