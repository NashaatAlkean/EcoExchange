from django.urls import path
from . import views


urlpatterns=[

    path('create-add/',views.create_item,name='create-add'),
    path('update_ad/<int:pk>/',views.update_item,name='update_ad')

]