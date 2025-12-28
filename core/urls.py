from library import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('books',views.getBooks ,name='getBooks'),
    path('authors',views.getAuthors,name='getAuthors'),
    path('authors/add',views.addAuthors,name="addAuthors"),
    path('books/add',views.addBooks,name="addBooks"),
    path('books/delete/<int:book_id>/', views.deleteBook, name='deleteBook'),
    path('authors/delete/<int:authors_id>/', views.deleteAuthors, name='deleteAuthors'),
    path('authors/details/<int:authors_id>/',views.detailsAuthors,name='detailsAuthors'),
    path('books/details/<int:book_id>/',views.detailsBooks,name='detailsBooks'),
    path('books/update',views.updateBooks,name='updateBooks'),
    path('author/update',views.updateAuthors,name='updateAuthors')
]
