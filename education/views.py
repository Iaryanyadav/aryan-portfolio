from django.shortcuts import render
from .models import Education

def education(request):
    education_list = Education.objects.all()
    return render(request, 'education.html', {'education_list': education_list})