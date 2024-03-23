from django.urls import path
from . import views

urlpatterns=[
    path('register-seeker/',views.register_seeker,name='register-seeker'),
    path('register-donor/',views.register_donor,name='register-donor'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('user-list/', views.user_list, name='user_list'),
    path('delete-users/', views.delete_users, name='delete_users'),  # Define the URL pattern for delete_users view
    path('profile/<int:pk>',views.profile,name='profile'),
    path('update_user/',views.update_user,name='update_user'),
    path('update_profile/',views.update_profile,name='update_profile'),



]