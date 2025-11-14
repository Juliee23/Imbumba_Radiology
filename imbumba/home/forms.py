from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'email', 'phone', 'notes']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'w-full border p-3 rounded-md'}),
            'email': forms.EmailInput(attrs={'class': 'w-full border p-3 rounded-md'}),
            'phone': forms.TextInput(attrs={'class': 'w-full border p-3 rounded-md'}),
            'notes': forms.Textarea(attrs={'class': 'w-full border p-3 rounded-md'}),
        }
