from django.shortcuts import render

# Create your views here.

def error_404_view(request):
    return render(request, '404.html')

def about_page_view(request):
    return render(request, 'about.html')

def appointment_page_view(request):
    return render(request, 'appointment.html')

def contact_page_view(request):
    return render(request, 'contact.html')

def feature_page_view(request):
    return render(request, 'feature.html')

def index_page_view(request):
    return render(request, 'index.html')

def service_page_view(request):
    return render(request, 'service.html')

def team_page_view(request):
    return render(request, 'team.html')

def testimonial_page_view(request):
    return render(request, 'testimonial.html')