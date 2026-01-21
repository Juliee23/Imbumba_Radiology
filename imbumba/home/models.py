from django.db import models
from django.utils import timezone

class Appointment(models.Model):
    BRANCH_CHOICES = [
        ("Ladysmith", "KwaZulu-Natal – Ladysmith(Main Branch)"),
        ("Richards Bay", "KwaZulu-Natal – Richards Bay"),
        ("Katlehong", "Gauteng – Katlehong"),
        ("Vosloorus", "Gauteng – Vosloorus"),
    ]

    SERVICE_CHOICES = [
        ("General X-Ray", "General X-Ray"),
        ("CT Scan", "CT Scan"),
        ("Ultrasound", "Ultrasound"),
        ("Theatre", "Theatre Imaging"),
    ]
        

    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    service = models.CharField(max_length=500, choices=SERVICE_CHOICES)
    preferred_date = models.DateField(default=timezone.now)
    preferred_time = models.TimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.service}"
