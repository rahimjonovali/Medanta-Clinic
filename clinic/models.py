from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone

class Appointment(models.Model):
    full_name = models.CharField(max_length=100)
    birth_year = models.IntegerField(validators=[MinValueValidator(1900), MaxValueValidator(timezone.now().year)])
    phone_number = models.CharField(max_length=20)
    appointment_date = models.DateField()
    appointment_time = models.TimeField()
    called = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    SOURCE_CHOICES = [
        ('Telegram', 'Telegram'),
        ('Instagram', 'Instagram'),
        ('doctor_recommendation', 'Doctor Recommendation'),
        ('regular_customer', 'Regular Customer'),
        ('friend_recommendation', 'Friend Recommendation'),
    ]
    source = models.CharField(max_length=30, choices=SOURCE_CHOICES)

    class Meta:
        unique_together = ('appointment_date', 'appointment_time')

    def __str__(self):
        return f"{self.full_name} - {self.appointment_date} - at {self.appointment_time}"

class ClinicSettings(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    time_interval = models.IntegerField(default=10, help_text="Time interval in minutes")
    admission_name = models.CharField(max_length=100)

