from rest_framework import serializers
from .models import Appointment, ClinicSettings
from django.utils import timezone
import datetime

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['full_name', 'birth_year', 'phone_number', 'appointment_date', 'appointment_time', 'source']

    def validate_appointment_time(self, value):
        settings = ClinicSettings.objects.first()
        if not settings:
            raise serializers.ValidationError("Clinic settings not configured")

        if value < settings.start_time or value > settings.end_time:
            raise serializers.ValidationError("Appointment time must be within clinic hours")

        minutes = value.hour * 60 + value.minute
        if (minutes - settings.start_time.hour * 60 - settings.start_time.minute) % settings.time_interval != 0:
            raise serializers.ValidationError("Invalid appointment time slot")

        return value

class AppointmentTimeSerializer(serializers.Serializer):
    appointment_date = serializers.DateField()

    def validate_appointment_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("Appointment date cannot be in the past")
        return value

    def get_available_times(self):
        settings = ClinicSettings.objects.first()
        if not settings:
            return []

        start = datetime.datetime.combine(self.validated_data['appointment_date'], settings.start_time)
        end = datetime.datetime.combine(self.validated_data['appointment_date'], settings.end_time)
        delta = datetime.timedelta(minutes=settings.time_interval)

        times = []
        current = start
        while current <= end:
            times.append(current.time())
            current += delta

        return times