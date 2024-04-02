from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_issue, name='report_issue'),
    path('reports/', views.view_reports, name='view_reports'),
    
]
