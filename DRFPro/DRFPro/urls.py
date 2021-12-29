"""DRFPro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from BookStore.views import *
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', BookList,name='book_list'),
    path('userbooks/', UserBooks.as_view(),name='user_book_list'),
    path('books_api/', BookAPIView.as_view(),name='book_list_api'),
    path('books_api2/', AdvanceBookView.as_view(),name='book_list_api2'),
    path('book_detail/<int:pk>/', BookDetailView.as_view(),name='book'),
    path('create_book/', BookCreateView.as_view(),name='create_book'),
    path('cat_detail/<int:pk>', CategoryWiseBook.as_view(),name='cat'),
    path('book_delete/<int:pk>', BookDeleteView.as_view(),name='delete'),
    path('create_user/', RegisterUserView.as_view(), name='create_user'),
    path('category/', CategoryList.as_view(), name='category'),
    path('update_book/<int:pk>/', BookUpdateView.as_view(),name='book_update'),


    ## Generate JWT Token
    path('login/', obtain_jwt_token,name='login'),



]
