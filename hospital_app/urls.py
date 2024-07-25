from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page_view, name='home'),
    path('about/', views.about_page_view, name='home'),
    path('contact/', views.contact_page_view, name='home'),
    path('service/', views.service_page_view, name='home'),
    path('team/', views.team_page_view, name='home'),
    path('feature/', views.feature_page_view, name='home'),
    path('appointment', views.appointment_page_view, name='home'),
    path('testimonial/', views.testimonial_page_view, name='home'),
    path('error/', views.error_404_view, name='home')
]