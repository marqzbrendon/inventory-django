from django.urls import path
from .views import inventory_list, increase_quantity, decrease_quantity, delete_item, add_item

urlpatterns = [
    path('', inventory_list, name='inventory_list'),
    path('increase/<int:item_id>/', increase_quantity, name='increase_quantity'),
    path('decrease/<int:item_id>/', decrease_quantity, name='decrease_quantity'),
    path('delete/<int:item_id>/', delete_item, name='delete_item'),
    path('add_item/', add_item, name='add_item'),
]
