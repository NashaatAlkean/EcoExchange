from django.urls import path
from . import views

urlpatterns=[
    path('register-seeker/',views.register_seeker,name='register-seeker'),
    path('register-donor/',views.register_donor,name='register-donor'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    # path('submit_review/',views.submit_review,name='submit_review'),

]