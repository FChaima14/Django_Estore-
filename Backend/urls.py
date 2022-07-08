from django.urls import path
from .views import *

urlpatterns=[
    path('', get_Product_list, name='Product_List'),
    path('dtaill/<int:pk>',get_Product_detaill , name='Product_detail'),
    path('cart', cart, name='cart'),
    path('checkout', checkout, name='checkout'),
    path('updateItem',updateItem, name='updateItem' ),
    path('processOrder', processOrder, name='processOredr'),
    path('search', search, name='search'),
    path('signIn', signIn, name='signIn'),
    path('register', signUp, name='register'),
    path('logout', signOut, name='logout'),
]