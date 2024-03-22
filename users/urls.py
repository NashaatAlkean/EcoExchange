from django.urls import path
from . import views

urlpatterns=[
    path('register-seeker/',views.register_seeker,name='register-seeker'),
    path('register-donor/',views.register_donor,name='register-donor'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('user-list/', views.user_list, name='user_list'),
    path('delete-users/', views.delete_users, name='delete_users'),  # Define the URL pattern for delete_users view

]