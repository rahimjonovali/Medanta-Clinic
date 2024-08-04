from django import forms
from .models import Appointment, ClinicSettings
import datetime
class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['full_name', 'birth_year', 'phone_number', 'appointment_date', 'appointment_time', 'source']
        widgets = {
            'appointment_date': forms.DateInput(attrs={'type': 'date'}),
            'appointment_time': forms.Select(choices=[]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['appointment_time'].widget.choices = self.get_time_choices()

    def get_time_choices(self):
        settings = ClinicSettings.objects.first()
        if not settings:
            return []

        start = settings.start_time
        end = settings.end_time
        interval = settings.time_interval

        choices = []
        current = start
        while current <= end:
            choices.append((current.strftime('%H:%M'), current.strftime('%I:%M %p')))
            current = (datetime.datetime.combine(datetime.date.today(), current) +
                       datetime.timedelta(minutes=interval)).time()

        return choices