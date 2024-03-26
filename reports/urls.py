from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.report_issue, name='report_issue'),
    path('reports/', views.view_reports, name='view_reports'),
    path('delete_report/<int:report_id>/', views.delete_report, name='delete_report'),
    path('resolve_report/<int:report_id>/', views.resolve_report, name='resolve_report'),

]