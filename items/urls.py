from django.urls import path
from . import views

urlpatterns=[

    path('create-add/',views.create_item,name='create-add'),
    path('update_ad/<int:pk>/',views.update_item,name='update_ad'),
    path('manage-items/',views.manage_items,name='manage-items'),
    path('request-item/<int:pk>/',views.request_item,name='request-item'),
    path('all_requests/<int:pk>/',views.all_requests,name='all_requests'),
    path('requested_items/',views.requested_items,name='requested_items'),
    path('item-approval/', views.item_approval, name='item_approval'),  # URL for item approval list
    path('approve-item/<int:item_id>/', views.approve_item, name='approve_item'),  # URL for approving item
    path('decline-item/<int:item_id>/', views.decline_item, name='decline_item'),  # URL for approving item

]

