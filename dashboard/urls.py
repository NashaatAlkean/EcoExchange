from django.urls import path
from . import views
#from this dirctory import views file

urlpatterns=[
    # path('',views.proxy,name='proxy'),
    # path('seeker-dashboard/',views.seeker_dashboard,name='seeker-dashboard'),
    # path('donor-dashboard/',views.donor_dashboard,name='donor-dashboard'),
    path('',views.dashboard,name='dashboard'),

]