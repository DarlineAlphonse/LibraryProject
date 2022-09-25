"""LibraryProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# from Library.views import BooksView,BookDetailView
from Library.views import ListBooksView,BookCreateView,UpdateBookView,BookDetailView,BookDeleteView,NewStudentView
from rest_framework.routers import DefaultRouter
from Library import views



router = DefaultRouter()
# router.register('books', BooksViewSet, basename='books'),
# router.register('booksop',BooksViewSetRestrictedView,basename='bookspop')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/',ListBooksView.as_view()),
    path('books/new/',BookCreateView.as_view()),
    path('books/edit/<int:pk>',UpdateBookView.as_view()),
    path('books/detail/<int:pk>',BookDetailView.as_view()),
    path('books/delete/',BookDeleteView.as_view()),
    path('users/',views.ListAllStudents.as_view()),
    path('users/new/',views.NewStudentView.as_view()),
    path('users/detail/<int:pk>',views.UserDetailView.as_view()),
    path('users/edit/<int:pk>',views.UpdateUserView.as_view()),

    path('books/issue/create/',views.CreateBookIssue.as_view()),
    path('books/issue/list/',views.IssuedBooksView.as_view()),
    path('books/issue/update/',views.IssuedBookUpdateView.as_view())



]+router.urls