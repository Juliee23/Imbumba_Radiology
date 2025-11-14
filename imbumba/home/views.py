from django.shortcuts import render, redirect
from .forms import AppointmentForm

def home(request):
    return render(request, 'home/index.html')

def services(request):
    return render(request, 'home/services.html')

def appointments_success(request):
    return render(request, 'home/appointments_success.html')



def appointments(request):
    if request.method == "POST":
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/appointments_success.html')
    else:
        form = AppointmentForm()

    return render(request, 'home/appointments.html', {'form': form})

def contact(request):
    return render(request, 'home/contact.html')


# Create your views here.
