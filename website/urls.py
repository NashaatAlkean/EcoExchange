from django.urls import path
from . import views


urlpatterns=[

    path('',views.home,name='home'),
    path('items-listing/',views.items_listing,name='items-listing'),
    path('item-details/<int:pk>',views.item_details,name='item-details'),
    path('reviews/', views.reviews, name='reviews'),  # Add this line for reviews
    path('admin-homepage/', views.admin_homepage, name='admin-homepage'),
    # path('item-approval/', views.item_approval, name='item_approval'),
    # path('item-approval/',views.approve_item,name='approve_item'),
   
]