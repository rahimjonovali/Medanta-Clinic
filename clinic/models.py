from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    birth_year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)])
    phone_number = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    SOURCE_CHOICES = [
        ('Telegram', 'Telegram'),
        ('Instagram', 'Instagram'),
        ('doctor_recommendation', 'Doctor Recommendation'),
        ('regular_customer', 'Regular Customer'),
        ('friend_recommendation', 'Friend Recommendation'),
    ]
    source = models.CharField(max_length=30, choices=SOURCE_CHOICES)

class ClinicSettings(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    time_interval = models.IntegerField(default=10, help_text="Time interval in minutes")
