from django.urls import path
from . import views


urlpatterns=[

    path('create-add/',views.create_item,name='create-add'),
    path('update_ad/<int:pk>/',views.update_item,name='update_ad'),
    path('manage-items/',views.manage_items,name='manage-items'),
    path('request-item/<int:pk>/',views.request_item,name='request-item'),
    path('all_requests/<int:pk>/',views.all_requests,name='all_requests'),


]