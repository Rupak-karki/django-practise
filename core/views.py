from django.shortcuts import render, redirect

from .models import Medicine

def home(request):
    medicines = Medicine.objects.all()
    return render(request, 'home.html', {'medicines': medicines})
def about(request):
    return render(request, 'about.html')

def add_medicine(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        stock = request.POST.get('stock')

        Medicine.objects.create(
            name=name,
            price=price,
            stock=stock
        )

        return redirect('/')   # go back to home

    return render(request, 'add_medicine.html')