# home/forms.py
from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'

        widgets = {
            
            'full_name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 p-3 rounded-md focus:ring focus:ring-blue-300 focus:outline-none'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full border border-gray-300 p-3 rounded-md focus:ring focus:ring-blue-300 focus:outline-none'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 p-3 rounded-md focus:ring focus:ring-blue-300 focus:outline-none'
            }),
            'branch': forms.Select(attrs={
                'class': 'w-full border border-gray-300 p-3 rounded-md focus:ring focus:ring-blue-300 focus:outline-none'
            }),
            'service': forms.Select(attrs={
                'class': 'w-full border border-gray-300 p-3 rounded-md focus:ring focus:ring-blue-300 focus:outline-none'
            }),
            'preferred_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full border border-gray-300 p-3 rounded-md focus:ring focus:ring-blue-300 focus:outline-none'
            }),
            'preferred_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'w-full border border-gray-300 p-3 rounded-md focus:ring focus:ring-blue-300 focus:outline-none'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 p-3 rounded-md focus:ring focus:ring-blue-300 focus:outline-none',
                'rows': 4,
                'placeholder': 'Any additional information (optional)'
            }),
        }

