from django.urls import path
from . import views


urlpatterns=[

    path('',views.home,name='home'),
    path('items-listing/',views.items_listing,name='items-listing'),
    path('item-details/<int:pk>',views.item_details,name='item-details')

]