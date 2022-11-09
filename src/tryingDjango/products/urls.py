from django.urls import path
from .views import product_detailed_view, product_create_view, product_delete_view, product_list_view, render_initial_data

app_name= 'products'

urlpatterns= [
    path('viewgbuynauwckicu/<int:my_id>/', product_detailed_view, name='viewItem' ), # since reverse url this will also work
    path('create/', product_create_view, name='createItem'),
    path('update/', render_initial_data, name='updateItem'),
    path('delete/<int:my_id>/', product_delete_view, name='deleteItem'),
    path('list/', product_list_view, name='listItem'),
]