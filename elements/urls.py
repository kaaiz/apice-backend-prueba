from django.urls import path
from .views import CategoryList, CategoryDetail, ElementList, ElementDetail, TypeList, TypeDetail, ProductList, ProductDetail, UserList, UserDetail, Login, Logout, Register

urlpatterns = [
    path('category/<int:pk>/', CategoryDetail.as_view()),
    path('category/', CategoryList.as_view()),
    path('element/<int:pk>/', ElementDetail.as_view()),
    path('element/', ElementList.as_view()),
    path('type/<int:pk>/', TypeDetail.as_view()),
    path('type/', TypeList.as_view()),
    path('product/<int:pk>/', ProductDetail.as_view()),
    path('product/', ProductList.as_view()),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('user/', UserList.as_view()),
    path('login/', Login.as_view()),
    path('logout/', Logout.as_view()),
    path('register/', Register.as_view()),
]