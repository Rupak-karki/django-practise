from django.shortcuts import render

from .models import Medicine

def home(request):
    medicines = Medicine.objects.all()
    return render(request, 'home.html', {'medicines': medicines})
def about(request):
    return render(request, 'about.html')