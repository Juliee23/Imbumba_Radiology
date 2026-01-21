from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
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
            appointment = form.save()
          
            # Send email
            send_mail(
                subject=f"New Appointment – {appointment.branch}",
                message=f"""

    New Appointment Request

    Name: {appointment.full_name}
    Email: {appointment.email}
    Phone: {appointment.phone}
    Branch: {appointment.branch}
    Service: {appointment.service}
    Preferred Date: {appointment.preferred_date}
    Preferred Time: {appointment.preferred_time}
    Additional Notes: {appointment.notes}
""",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["reception.voslo@imbumbaradiology.com"],
                fail_silently=False,
            )

            return redirect( 'appointments_success')

    else:
        form = AppointmentForm()

    return render(request, "home/appointments.html", {"form": form})

def contact(request):
    return render(request, 'home/contact.html')


# Create your views here.
